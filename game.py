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
        self.player.update()

    def draw(self):
        p.cls(0)
        self.player.car.draw_car()
        # p.rect(10, 10, 20, 20, 9)

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, self.start_pyxel)

    def start_pyxel(self):
        p.init(160, 120)
        p.run(self.update, self.draw)

    
    async def receive_message(self):
        try:
            async for message in self.websocket:
                print(f"Received from server: {message}")
                await self.player.handle_message(message)
                await self.handle_message(message)
        except websockets.ConnectionClosed:
            print("Disconnected from server.")


    async def handle_message(self, message):
        if message.startswith("create_player"):
            self.create_player(message)
        elif message == "run":
            self.run()


    def create_player(self, message):
        self.players.append({
            "id": message.split("-")[0].split("/")[1],
            "color": message.split("-")[1].split("/")[1]
        })
        print(self.players)
    
    async def send_id_request(self):
        await self.websocket.send("load")
    
