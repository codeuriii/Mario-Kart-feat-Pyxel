import pyxel as p
import asyncio
from game import Game
import websockets

async def main():
    uri = f"ws://127.0.0.1:1025"
    connected = False
    while not connected:
        try:
            async with websockets.connect(uri) as websocket:
                print("Connected to server.")
                connected = True
                game = Game(websocket)
                await asyncio.gather(
                    game.player_receive_message(),
                    game.run(),
                    game.player_send_id_request()
                )
        except (websockets.exceptions.ConnectionClosedError, ConnectionRefusedError):
            print("Connection failed, retrying in 1 seconds...")
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())