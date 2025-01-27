import asyncio
import pyxel as p
from drawer import Drawer
from items import Item
from player import Player
from road import Road, Roads
import websockets

class Game:
    def __init__(self, websocket):
        self.websocket = websocket
        self.player = Player(self.websocket)
        self.players = []
        self.drawer = Drawer()
        self.road = Road()
        self.roads = Roads()
        self.track_1 = [
            [self.roads.empty, self.roads.bas_droite,  self.roads.horizontal, self.roads.horizontal,  self.roads.horizontal,  self.roads.horizontal, self.roads.horizontal, self.roads.bas_gauche,  self.roads.empty],
            [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.empty,       self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
            [self.roads.empty, self.roads.haut_droite, self.roads.horizontal, self.roads.horizontal,  self.roads.bas_gauche,  self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
            [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.empty,       self.roads.vertical,    self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
            [self.roads.empty, self.roads.bas_droite,  self.roads.horizontal, self.roads.horizontal,  self.roads.haut_gauche, self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
            [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.empty,       self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
            [self.roads.empty, self.roads.haut_droite, self.roads.horizontal, self.roads.horizontal,  self.roads.horizontal,  self.roads.horizontal, self.roads.horizontal, self.roads.haut_gauche, self.roads.empty]
        ]

        self.track_2 = [
            [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.empty,       self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.empty,       self.roads.empty],
            [self.roads.empty, self.roads.bas_droite,  self.roads.horizontal, self.roads.bas_gauche,  self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.empty,       self.roads.empty],
            [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.vertical,    self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.empty,       self.roads.empty],
            [self.roads.empty, self.roads.haut_droite, self.roads.horizontal, self.roads.carrefour,   self.roads.horizontal,  self.roads.horizontal, self.roads.horizontal, self.roads.bas_gauche,  self.roads.empty],
            [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.vertical,    self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
            [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.haut_droite, self.roads.horizontal,  self.roads.horizontal, self.roads.horizontal, self.roads.haut_gauche, self.roads.empty],
            [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.empty,       self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.empty,       self.roads.empty]
        ]

        self.track_3 = [
            [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.bas_droite,  self.roads.horizontal, self.roads.horizontal, self.roads.horizontal, self.roads.bas_gauche,  self.roads.empty],
            [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.vertical,    self.roads.empty,      self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
            [self.roads.empty, self.roads.bas_droite,  self.roads.horizontal, self.roads.carrefour,   self.roads.horizontal, self.roads.horizontal, self.roads.horizontal, self.roads.haut_gauche, self.roads.empty],
            [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.vertical,    self.roads.empty,      self.roads.empty,      self.roads.empty,      self.roads.empty,       self.roads.empty],
            [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.haut_droite, self.roads.horizontal, self.roads.horizontal, self.roads.horizontal, self.roads.bas_gauche,  self.roads.empty],
            [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
            [self.roads.empty, self.roads.haut_droite, self.roads.horizontal, self.roads.horizontal,  self.roads.horizontal, self.roads.horizontal, self.roads.horizontal, self.roads.haut_gauche, self.roads.empty]
        ]

        self.track = self.track_3
        self.items: list[Item] = []

    def update(self):
        self.player.update(self.check_hors_piste())
        for player in self.players:
            if player["id"] == self.player.infos["id"]:
                player["x"] = self.player.car.x
                player["y"] = self.player.car.y
        self.player.infos["id"]

        for item in self.items:
            item.update()

        asyncio.run(self.websocket.send(f"move/{self.player.infos["id"]}/{self.player.car.x}/{self.player.car.y}/{self.player.car.angle}"))
    
    def check_hors_piste(self):
        car_x, car_y = self.player.car.get_center()
        tile_x, tile_y = int(car_x // 32), int(car_y // 32)
        if 0 <= tile_y < len(self.track) and 0 <= tile_x < len(self.track[0]):
            return self.track[tile_y][tile_x] == self.roads.empty
        return True

    def draw(self):
        p.cls(p.COLOR_LIME)
        self.road.draw_road(self.track)
        self.player.car.draw_car()
        self.draw_players()
        self.player.item.draw_item_case()
        if self.player.item is not None:
            self.player.item.draw_item(p.width - 20, 10)
        for item in self.items:
            item.draw()

    async def run(self):
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
                try:
                    self.player.infos["id"]
                    await self.handle_message(message)
                except:
                    pass
        except websockets.ConnectionClosed:
            print("Disconnected from server.")


    async def handle_message(self, message):
        if message.startswith("move"):
            for player in self.players:
                if player["id"] != message.split("/")[1]:
                    player["x"] = int(message.split("/")[2])
                    player["y"] = int(message.split("/")[3])
                    player["angle"] = int(message.split("/")[4])
        elif message.startswith("create_player"):
            self.create_player(message)
        elif message.startswith("delete-client"):
            print(message)
            print(message.split("/")[1])
            self.players = [player for player in self.players if player["id"] != message.split("/")[1]]
        elif message.startswith("item"):
            self.items.append(Item(message.split("-")[0].split("/")[1], message.split("-")[1].split("/")[1]))
        elif message == "run":
            await self.run()
        elif message == "this room is full error":
            print("This room is full.")
            await self.websocket.close()

    def draw_car(self, color, x, y, angle):
        self.drawer.draw_car(color, x, y, angle)
    
    def draw_players(self):
        for player in self.players:
            self.draw_car(player["color"], player["x"], player["y"], player["angle"])

    def create_player(self, message):
        player_id = message.split("-")[0].split("/")[1]
        if not any(player["id"] == player_id for player in self.players):
            self.players.append({
                "id": player_id,
                "color": message.split("-")[1].split("/")[1],
                "x": 10,
                "y": 10,
                "angle": 270
            })
        print(self.players)
    
    async def send_id_request(self):
        await self.websocket.send("load")
    
