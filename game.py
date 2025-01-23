import asyncio
import pyxel as p
from player import Player
import websockets

class Game:
    def __init__(self, websocket):
        self.websocket = websocket
        self.player = Player(self.websocket)
        self.players = []

    def update(self):
        pass

    def draw(self):
        p.cls(0)
        p.rect(10, 10, 20, 20, 9)

    def run(self):
        print("run function")
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, self.start_pyxel)

    def start_pyxel(self):
        p.init(160, 120)
        p.run(self.update, self.draw)

    
    async def receive_message(self):
        print("receive message function")
        try:
            print("before async for")
            async for message in self.websocket:
                print(f"Received from server: {message}")
                await self.player.handle_message(message)
                await self.handle_message(message)
            print("after async for")
        except websockets.ConnectionClosed:
            print("Disconnected from server.")

        print("receive message function end")

    async def handle_message(self, message):
        print("handle message function")
        if message.startswith("create_player"):
            self.create_player(message)
        elif message == "run":
            self.run()

        print("handle message function end")

    def create_player(self, message):
        print("create player function")
        self.players.append({
            "id": message.split("-")[0].split("/")[1],
            "color": message.split("-")[1].split("/")[1]
        })
        print("create player function end")
        print(self.players)
    
    async def send_id_request(self):
        print("send load to server")
        await self.websocket.send("load")
        print("send load to server end")
    
