import pyxel as p
from player import Player
import websockets

class Game:
    def __init__(self, websocket):
        self.websocket = websocket
        self.player = Player(self.websocket)

    def update(self):
        pass

    def draw(self):
        p.cls(0)
        p.rect(10, 10, 20, 20, 9)

    async def run(self):
        p.init(160, 120)
        p.run(self.update, self.draw)

    
    async def receive_message(self):
        print("receive message function")
        try:
            print("before async for")
            async for message in self.websocket:
                print(f"Received from server: {message}")
                self.player.handle_message(message)
            print("after async for")
        except websockets.ConnectionClosed:
            print("Disconnected from server.")

        print("receive message function end")
    
    async def send_id_request(self):
        print("send load to server")
        await self.websocket.send("load")
    
