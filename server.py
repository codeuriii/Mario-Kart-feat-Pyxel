import asyncio
import websockets
import socket
import random
import string

connected_clients = set()
all_tokens = []
colors = [
    "blue",
    "red",
    "green",
    "yellow"
]

def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

async def handler(websocket):
    connected_clients.add(websocket)
    try:
        current_token = generate_token()
        async for message in websocket:
            print(f"Received from client: {message}")
            disconnected_clients = []
            for client in connected_clients:
                try:
                    if message == "load":
                        if client == websocket:
                            if len(all_tokens) < len(colors):
                                color = colors[len(all_tokens)]
                                all_tokens.append({
                                    "token": current_token,
                                    "color": color
                                })
                                await asyncio.sleep(1)
                                await websocket.send(f"id/{current_token}-color/{color}")
                            else:
                                await websocket.send("this room is full error")

                    elif message == "get_players":
                        for element in all_tokens:
                            token = element['token']
                            color = element['color']
                            await client.send(f"create_player/{token}-color/{color}")
                    
                    elif message == "run":
                        if client == websocket:
                            await client.send("run")
                    
                    elif message.startswith("move"):
                        await client.send(message)

                except websockets.ConnectionClosed:
                    disconnected_clients.append(client)
            # Nettoyer les clients déconnectés
            for client in disconnected_clients:
                connected_clients.remove(client)
    except websockets.ConnectionClosed:
        print("Client disconnected.")

async def main():
    def get_local_ip():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
        return local_ip

    local_ip = get_local_ip()
    print(f"Server will be accessible on ws://{local_ip}:1025")
    async with websockets.serve(handler, "127.0.0.1", 1025, ping_interval=20, ping_timeout=20):
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped.")
