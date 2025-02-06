from car import Car
import pyxel as p
from items import Items, Item
import asyncio

class Player:
    def __init__(self, websocket, x, y, face):
        self.websocket = websocket
        self.x = x * 32 + 8
        self.y = y * 32 + 8
        self.face = face
        self.facing = {
            "haut": 270,
            "bas": 90,
            "droite": 0,
            "gauche": 180
        }

        self.item = Item(Items.none, self.x, self.y, self.facing[self.face])
        self.protected = False
        self.spin_start_frame = None # for animation puropses
        self.rank = 1

    async def handle_message(self, message):
        if message.startswith("id"):
            self.set_id(message)
            self.parse_id()
            self.color = self.get_color()
            self.car = Car(self.x, self.y, self.color, self.face)
            await self.websocket.send("get_players")
            await self.websocket.send("run")
    
    def update(self, hors_piste, items: list[Item]):
        self.car.update(hors_piste)
        if self.check_use_item():
            self.protected = True

        for item in items:
            if abs(self.car.get_center()[0] - item.x) <= 10 and abs(self.car.get_center()[1] - item.y) <= 10:
                if not self.protected:
                    self.hit()
                    asyncio.run(self.websocket.send(f"remove_item/{item.token}"))
            else:
                if self.protected:
                    self.protected = False
                
        if self.spin_start_frame != None:
            elapsed_frames = p.frame_count - self.spin_start_frame
            if elapsed_frames < 60:
                if elapsed_frames < 5:
                    self.car.color = "white"
                else:
                    self.car.color = self.get_color()
                if elapsed_frames < 20:
                    self.car.angle += 18
                self.car.speed = 0
            else:
                self.spin_start_frame = None
            
    def set_id(self, id):
        self.id = id

    def parse_id(self):
        self.infos = {element.split("/")[0]: element.split("/")[1] for element in self.id.split("-")}

    def get_color(self):
        return self.infos['color']

    def hit(self):
        self.car.speed = 0
        self.spin_start_frame = p.frame_count

    def check_use_item(self):
        if self.item.id != Items.none:
            if p.btnp(p.KEY_E):
                asyncio.run(self.websocket.send(f"item/{self.item.id}-id/{self.item.token}-x/{self.car.get_center()[0]-4}-y/{self.car.get_center()[1]-4}-angle/{self.car.angle}"))
                print(f"id keypress {self.item.id}")
                self.item.id = Items.none 
                return True
        return False
