import asyncio
import websockets
from game import Game

async def connect_to_server(uri, max_retries=10, retry_delay=1):
    """Essaie de se connecter au serveur WebSocket avec des tentatives multiples."""
    retries = 0
    while retries < max_retries:
        try:
            websocket = await websockets.connect(uri)
            print("Connected to server.")
            return websocket
        except (websockets.exceptions.ConnectionClosedError, ConnectionRefusedError) as e:
            retries += 1
            print(f"Connection attempt {retries} failed: {e}. Retrying in {retry_delay} seconds...")
            await asyncio.sleep(retry_delay)
    raise ConnectionError(f"Failed to connect to server after {max_retries} attempts.")

async def main():
    uri = "ws://127.0.0.1:1025"
    try:
        websocket = await connect_to_server(uri, max_retries=10, retry_delay=1)
        game = Game(websocket)

        print("Starting game tasks...")
        await asyncio.gather(
            game.receive_message(),
            game.send_id_request()
        )
    except ConnectionError as e:
        print(f"Failed to connect to server: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Client shutting down.")

if __name__ == "__main__":
    asyncio.run(main())
