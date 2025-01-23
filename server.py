import asyncio
import websockets
import socket
import random
import string

connected_clients = set()
all_tokens = []
colors = [
    "blue",
    "green",
    "red",
    "yellow"
]

def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

async def handler(websocket):
    """Gestion des connexions client."""
    connected_clients.add(websocket)
    try:
        current_token = generate_token()
        async for message in websocket:
            print(f"Received from client: {message}")
            # Diffuser le message reçu à tous les clients
            disconnected_clients = []
            for client in connected_clients:
                try:
                    if message == "load":
                        if client == websocket:
                            if len(all_tokens) <= len(colors):
                                color = colors[len(all_tokens)]
                                all_tokens.append({
                                    "token": current_token,
                                    "color": color
                                })
                                await asyncio.sleep(1)
                                print("just before send id to client")
                                await websocket.send(f"id/{current_token}-color/{color}")
                                print("just after send id to client")
                            else:
                                await websocket.send("this room is full error")
                            print(current_token)
                            print(all_tokens)
                            print("send id to client")
                            print(all_tokens)

                        else:
                            for element in all_tokens:
                                if element["token"] == current_token:
                                    print(color := element['color'])
                            await client.send(f"create_player/{current_token}-color/{color}")
                            print("send create player to client")

                    elif message == "get_players":
                        if client == websocket:
                            for element in all_tokens:
                                print(token := element['token'])
                                print(color := element['color'])
                                await client.send(f"create_player/{token}-color/{color}")
                    
                    elif message == "run":
                        if client == websocket:
                            await client.send("run")

                except websockets.ConnectionClosed:
                    disconnected_clients.append(client)
            # Nettoyer les clients déconnectés
            for client in disconnected_clients:
                connected_clients.remove(client)
    except Exception as e:
        raise e

async def main():
    def get_local_ip():
        """Obtenir l'adresse IP locale de la machine."""

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
        return local_ip

    local_ip = get_local_ip()
    print(local_ip)
    print(f"WebSocket server will be accessible on ws://{local_ip}:1025")
    async with websockets.serve(handler, "127.0.0.1", 1025, ping_interval=20, ping_timeout=20):
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped.")
