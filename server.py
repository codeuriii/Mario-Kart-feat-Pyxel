import asyncio
import websockets
import socket

connected_clients: set[websockets.WebSocketClientProtocol] = set()
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

async def handler(websocket: websockets.WebSocketClientProtocol):
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
                                all_tokens[current_token] = color
                                await websocket.send(f"id/{current_token}-color/{color}")
                            else:
                                await websocket.send("this room is full error")
                        else:
                            if len(all_tokens) <= len(colors):
                                await client.send(f"create_player/{current_token}-color/{all_tokens[current_token]}")
                        print("send id to client")

                    elif message == "get_players":
                        if client == websocket:
                            for token, color in all_tokens.items():
                                await client.send(f"create_player/{token}-color/{color}")

                except websockets.ConnectionClosed:
                    disconnected_clients.append(client)
            # Nettoyer les clients déconnectés
            for client in disconnected_clients:
                connected_clients.remove(client)
    except websockets.ConnectionClosed:
        print("Client disconnected")
    finally:
        connected_clients.remove(websocket)

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
    """Point d'entrée principal pour démarrer le serveur."""
    print("WebSocket server started on ws://0.0.0.0:1025")
    # Démarrer le serveur WebSocket
    async with websockets.serve(handler, "0.0.0.0", 1025):
        # Exécuter la diffusion et la gestion des connexions en parallèle
        await asyncio.gather(
            asyncio.Future()       # Maintenir le serveur actif
        )

if __name__ == "__main__":
    asyncio.run(main())
