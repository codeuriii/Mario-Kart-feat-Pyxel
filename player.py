from car import Car
import pyxel as p
from items import Items, Item
import asyncio

class Player:
    def __init__(self, websocket):
        self.websocket = websocket
        self.item = Item(Items.peau_de_banane, 10, 10, 270)
        self.protected = False
        self.rank = 1

    async def handle_message(self, message):
        if message.startswith("id"):
            self.set_id(message)
            self.parse_id()
            self.color = self.get_color()
            self.car = Car(10, 10, self.color)
            await self.websocket.send("get_players")
            await self.websocket.send("run")
    
    def update(self, hors_piste, items):
        self.car.update(hors_piste)
        if self.check_use_item():
            self.protected = True

        for item in items:
            if abs(self.car.x - item.x) <= 5 and abs(self.car.y - item.y) <= 5:
                if not self.protected:
                    # self.hit()
                    print('hit')
            else:
                if self.protected:
                    self.protected = False
                
            
    def set_id(self, id):
        self.id = id

    def parse_id(self):
        self.infos = {element.split("/")[0]: element.split("/")[1] for element in self.id.split("-")}

    def get_color(self):
        return self.infos['color']

    def check_use_item(self):
        if self.item.id != Items.none:
            if p.btnp(p.KEY_E):
                asyncio.run(self.websocket.send(f"item/{self.item.id}-id/{self.infos['id']}-x/{self.car.x}-y/{self.car.y}-angle/{self.car.angle}"))
                print(f"id keypress {self.item.id}")
                self.item.id = Items.none 
                return True
        return False