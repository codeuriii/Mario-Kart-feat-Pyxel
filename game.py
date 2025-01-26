import asyncio
import pyxel as p
from player import Player
from road import Road, Roads
import websockets

class Game:
    def __init__(self, websocket):
        self.websocket = websocket
        self.player = Player(self.websocket)
        self.players = []
        self.road = Road()
        roads = Roads()
        self.track_1 = [
            [roads.empty, roads.bas_droite,  roads.horizontal, roads.horizontal,  roads.horizontal,  roads.horizontal, roads.horizontal, roads.bas_gauche, roads.empty],
            [roads.empty, roads.vertical,    roads.empty,      roads.empty,       roads.empty,       roads.empty,      roads.empty,      roads.vertical,   roads.empty],
            [roads.empty, roads.haut_droite, roads.horizontal, roads.horizontal,  roads.bas_gauche,  roads.empty,      roads.empty,      roads.vertical,   roads.empty],
            [roads.empty, roads.empty,       roads.empty,      roads.empty,       roads.vertical,    roads.empty,      roads.empty,      roads.vertical,   roads.empty],
            [roads.empty, roads.bas_droite,  roads.horizontal, roads.horizontal,  roads.haut_gauche, roads.empty,      roads.empty,      roads.vertical,   roads.empty],
            [roads.empty, roads.vertical,    roads.empty,      roads.empty,       roads.empty,       roads.empty,      roads.empty,      roads.vertical,   roads.empty],
            [roads.empty, roads.haut_droite, roads.horizontal, roads.horizontal,  roads.horizontal,  roads.horizontal, roads.horizontal, roads.haut_gauche, roads.empty]
        ]

        self.track_2 = [
            [roads.empty, roads.empty,       roads.empty,      roads.empty,       roads.empty,       roads.empty,      roads.empty,      roads.empty,      roads.empty],
            [roads.empty, roads.bas_droite, roads.horizontal, roads.bas_gauche, roads.empty,       roads.empty,      roads.empty,      roads.empty,      roads.empty],
            [roads.empty, roads.vertical,    roads.empty,      roads.vertical,    roads.empty,       roads.empty,      roads.empty,      roads.empty,      roads.empty],
            [roads.empty, roads.haut_droite, roads.horizontal, roads.carrefour,   roads.horizontal,  roads.horizontal, roads.horizontal, roads.bas_gauche, roads.empty],
            [roads.empty, roads.empty,       roads.empty,      roads.vertical,    roads.empty,       roads.empty,      roads.empty,      roads.vertical,    roads.empty],
            [roads.empty, roads.empty,       roads.empty,      roads.haut_droite, roads.horizontal,  roads.horizontal, roads.horizontal, roads.haut_gauche, roads.empty],
            [roads.empty, roads.empty,       roads.empty,      roads.empty,       roads.empty,       roads.empty,      roads.empty,      roads.empty,      roads.empty]
        ]

        self.track_3 = [
            [roads.empty, roads.empty,       roads.empty,      roads.bas_droite, roads.horizontal,  roads.horizontal, roads.horizontal, roads.bas_gauche, roads.empty],
            [roads.empty, roads.empty,       roads.empty,      roads.vertical,    roads.empty,       roads.empty,      roads.empty,      roads.vertical,   roads.empty],
            [roads.empty, roads.bas_droite,  roads.horizontal,      roads.carrefour,   roads.horizontal,  roads.horizontal, roads.horizontal, roads.haut_gauche, roads.empty],
            [roads.empty, roads.vertical,    roads.empty,      roads.vertical,    roads.empty,       roads.empty,      roads.empty,      roads.empty,   roads.empty],
            [roads.empty, roads.vertical,    roads.empty,      roads.haut_droite,    roads.horizontal,       roads.horizontal,      roads.horizontal,      roads.bas_gauche,   roads.empty],
            [roads.empty, roads.vertical,    roads.empty,      roads.empty,    roads.empty,       roads.empty,      roads.empty,      roads.vertical,   roads.empty],
            [roads.empty, roads.haut_droite, roads.horizontal,      roads.horizontal,    roads.horizontal,       roads.horizontal,      roads.horizontal,      roads.haut_gauche,   roads.empty]
        ]

    def update(self):
        self.player.update()

    def draw(self):
        p.cls(p.COLOR_LIME)
        self.road.draw_road(self.track_3)
        self.player.car.draw_car()
        self.player.item.draw_item(10, 10)

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, self.start_pyxel)

    def start_pyxel(self):
        p.init(288, 224, fps=60, title="Mario Kart 8.5")
        p.load("images.pyxres")
        p.mouse(True)
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
        elif message.startswith("delete-client"):
            print(message)
            print(message.split("/")[1])
            self.players = [player for player in self.players if player["id"] != message.split("/")[1]]
        elif message == "run":
            self.run()
        elif message == "this room is full error":
            print("This room is full.")
            await self.websocket.close()


    def create_player(self, message):
        player_id = message.split("-")[0].split("/")[1]
        if not any(player["id"] == player_id for player in self.players):
            self.players.append({
                "id": player_id,
                "color": message.split("-")[1].split("/")[1]
            })
        print(self.players)
    
    async def send_id_request(self):
        await self.websocket.send("load")
    
