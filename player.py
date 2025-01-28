from car import Car
import pyxel as p
from items import Items, Item
import asyncio

class Player:
    def __init__(self, websocket):
        self.websocket = websocket
        self.item = Item(Items.carapace_verte)

    async def handle_message(self, message):
        if message.startswith("id"):
            self.set_id(message)
            self.parse_id()
            self.color = self.get_color()
            self.car = Car(10, 10, self.color)
            await self.websocket.send("get_players")
            await self.websocket.send("run")
    
    def update(self, hors_piste):
        self.car.update(hors_piste)
        self.check_use_item()
            
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
