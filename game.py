import asyncio
import random
import pyxel as p
from boxes import Box
from drawer import Drawer
from items import Item, Items
from player import Player
from road import Road, Roads
import websockets
import re

class Game:
    def __init__(self, websocket):
        self.websocket = websocket
        self.drawer = Drawer()
        self.players = []
        self.road = Road()
        self.roads = Roads()
        self.flower_bg = ["grass"] * 2 + ["flowers"]
        self.dirt_bg = ["dirt"] * 3 + ["rocks"]

        self.track_1 = {
            "track": [
                [self.roads.empty, self.roads.bas_droite,  self.roads.horizontal, self.roads.horizontal,  self.roads.horizontal,  self.roads.horizontal, self.roads.horizontal, self.roads.bas_gauche,  self.roads.empty],
                [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.empty,       self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
                [self.roads.empty, self.roads.haut_droite, self.roads.horizontal, self.roads.horizontal,  self.roads.bas_gauche,  self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
                [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.empty,       self.roads.vertical,    self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
                [self.roads.empty, self.roads.bas_droite,  self.roads.horizontal, self.roads.horizontal,  self.roads.haut_gauche, self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
                [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.empty,       self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
                [self.roads.empty, self.roads.haut_droite, self.roads.horizontal, self.roads.horizontal,  self.roads.horizontal,  self.roads.horizontal, self.roads.horizontal, self.roads.haut_gauche, self.roads.empty]
            ],
            "item boxes": [
                Box(3, 2, False),
                Box(7, 5, True)
            ],
            "damier": (3, 6, False),
            "background": self.flower_bg,
            "spawn": (4, 6, "gauche")
        }

        self.track_2 = {
            "track": [
                [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.empty,       self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.empty,       self.roads.empty],
                [self.roads.empty, self.roads.bas_droite,  self.roads.horizontal, self.roads.bas_gauche,  self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.empty,       self.roads.empty],
                [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.vertical,    self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.empty,       self.roads.empty],
                [self.roads.empty, self.roads.haut_droite, self.roads.horizontal, self.roads.carrefour,   self.roads.horizontal,  self.roads.horizontal, self.roads.horizontal, self.roads.bas_gauche,  self.roads.empty],
                [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.vertical,    self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
                [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.haut_droite, self.roads.horizontal,  self.roads.horizontal, self.roads.horizontal, self.roads.haut_gauche, self.roads.empty],
                [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.empty,       self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.empty,       self.roads.empty]
            ],
            "item boxes": [
                Box(4, 3, False)
            ],
            "damier": (4, 5, False),
            "background": self.dirt_bg,
            "spawn": (5, 5, "gauche")
        }

        self.track_3 = {
            "track": [
                [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.bas_droite,  self.roads.horizontal, self.roads.horizontal, self.roads.horizontal, self.roads.bas_gauche,  self.roads.empty],
                [self.roads.empty, self.roads.empty,       self.roads.empty,      self.roads.vertical,    self.roads.empty,      self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
                [self.roads.empty, self.roads.bas_droite,  self.roads.horizontal, self.roads.carrefour,   self.roads.horizontal, self.roads.horizontal, self.roads.horizontal, self.roads.haut_gauche, self.roads.empty],
                [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.vertical,    self.roads.empty,      self.roads.empty,      self.roads.empty,      self.roads.empty,       self.roads.empty],
                [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.haut_droite, self.roads.horizontal, self.roads.horizontal, self.roads.horizontal, self.roads.bas_gauche,  self.roads.empty],
                [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.empty,       self.roads.empty,      self.roads.empty,      self.roads.empty,      self.roads.vertical,    self.roads.empty],
                [self.roads.empty, self.roads.haut_droite, self.roads.horizontal, self.roads.horizontal,  self.roads.horizontal, self.roads.horizontal, self.roads.horizontal, self.roads.haut_gauche, self.roads.empty]
            ],
            "item boxes": [
                Box(6, 0, False),
                Box(2, 6, False)
            ],
            "damier": (4, 4, False),
            "background": self.flower_bg,
            "spawn": (5, 4, "gauche")
        }

        self.track_4 = {
            "track": [
                [self.roads.empty, self.roads.bas_droite,  self.roads.horizontal, self.roads.horizontal,  self.roads.horizontal, self.roads.horizontal,  self.roads.horizontal, self.roads.bas_gauche,  self.roads.empty],
                [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.empty,       self.roads.empty,      self.roads.empty,       self.roads.empty,      self.roads.vertical,    self.roads.empty],
                [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.bas_droite,  self.roads.horizontal, self.roads.bas_gauche,  self.roads.empty,      self.roads.vertical,    self.roads.empty],
                [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.vertical,    self.roads.empty,      self.roads.vertical,    self.roads.empty,      self.roads.vertical,    self.roads.empty],
                [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.haut_droite, self.roads.horizontal, self.roads.carrefour,   self.roads.horizontal, self.roads.haut_gauche, self.roads.empty],
                [self.roads.empty, self.roads.vertical,    self.roads.empty,      self.roads.empty,       self.roads.empty,      self.roads.vertical,    self.roads.empty,      self.roads.empty,       self.roads.empty],
                [self.roads.empty, self.roads.haut_droite, self.roads.horizontal, self.roads.horizontal,  self.roads.horizontal, self.roads.haut_gauche, self.roads.empty,      self.roads.empty,       self.roads.empty]
            ],
            "item boxes": [
                Box(1, 4, True),
                Box(6, 4, False)
            ],
            "damier": (2, 6, False),
            "background": self.dirt_bg,
            "spawn": (3, 6, "gauche")
        }

        self.current_track = self.track_4
        self.track = self.current_track["track"]
        self.item_boxes: list[Box] = self.current_track["item boxes"]
        self.damier = self.current_track["damier"]
        self.current_bg = self.current_track["background"]
        self.spawn_point = self.current_track["spawn"]

        self.player = Player(self.websocket, *self.spawn_point)

        self.bgs = []
        self.items: list[Item] = []
        self.set_backgrounds()
    
    def set_backgrounds(self):
        for _ in range(14):
            current_list = []
            for _ in range(18):
                current_list.append(self.drawer.get_random_background(random.choice(self.current_bg)))
            self.bgs.append(current_list)

    def check_hors_piste(self, x, y):
        return self.get_tile(x, y) == self.roads.empty
    
    def get_tile(self, car_x, car_y):
        tile_x, tile_y = int(car_x // 32), int(car_y // 32)
        if 0 <= tile_y < len(self.track) and 0 <= tile_x < len(self.track[0]):
            return self.track[tile_y][tile_x]
        return self.roads.empty

    def update(self):
        self.player.update(self.check_hors_piste(*self.player.car.get_center()), self.items)
        for item in self.items:
            if not item.update(self.get_tile(item.x, item.y), self.get_tile(item.svgd_x, item.svgd_y)):
                self.items.remove(item)

    def draw_background(self):
        for y in range(14):
            for x in range(18):
                tile = self.bgs[y][x]
                self.drawer.draw_background(x * 16, y * 16, tile)
    
    def draw(self):
        self.draw_background()
        self.road.draw_road(self.track)
        self.drawer.draw_damier(*self.damier)
        self.player.item.draw_item_case()
        if self.player.item.id is not Items.none:
            self.player.item.draw_item(p.width - 20, 10, self.player.item.id)
        for box in self.item_boxes:
            box.draw()
        self.player.car.draw_car()
        for item in self.items:
            item.draw()

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
        elif message.startswith("item"):
            angle_match = re.search(r'angle/(-?\d+\.?\d*)', message)
            angle = float(angle_match.group(1)) if angle_match else 0.0
            self.items.append(Item(
                message.split("-")[0].split("/")[1],
                message.split("-")[2].split("/")[1],
                message.split("-")[3].split("/")[1],
                angle,
                message.split("-")[1].split("/")[1]
            ))
        elif message == "run":
            self.run()
        elif message == "this room is full error":
            print("This room is full.")
            await self.websocket.close()
        elif message.startswith("remove_item"):
            for item in self.items:
                if item.token == message.split("/")[1]:
                    self.items.remove(item)


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
    
