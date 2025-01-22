import asyncio
import websockets
import socket

connected_clients = set()
all_tokens = {}
colors = [
    "blue",
    "green",
    "red",
    "yellow"
]

def generate_token():
    """Générer un jeton unique pour chaque client."""
    return hex(id(object()))[2:]

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
                        if len(all_tokens) <= len(colors):
                            color = colors[len(all_tokens)]
                            all_tokens[current_token] = color
                            await asyncio.sleep(1)
                            await websocket.send(f"id/{current_token}-color/{color}")
                            print("just after send id to client")
                        else:
                            await websocket.send("this room is full error")
                        print(current_token)
                        print(all_tokens)
                        print("send id to client")

                        if client != websocket:
                            await client.send(f"create_player/{current_token}-color/{all_tokens[current_token]}")
                            print("send create player to client")

                    elif message == "get_players":
                        if client == websocket:
                            for token, color in all_tokens.items():
                                await client.send(f"create_player/{token}-color/{color}")

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
    async with websockets.serve(handler, "127.0.0.1", 1025):
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped.")
