from car import Car
import websockets
import asyncio

class Player:
    def __init__(self, websocket):
        self.websocket = websocket

    def generate_token(self):
        return hex(id(object()))[2:]
    
    async def receive_message(self):
        try:
            async for message in self.websocket:
                if message.startwith("id"):
                    self.set_id(message)
                    self.parse_id()
                    self.color = self.get_color()
                    self.car = Car(color=self.color)
        except websockets.ConnectionClosed:
            print("Disconnected from server.")

    def set_id(self, id):
        self.id = id

    def parse_id(self):
        self.infos = {element.split("/")[0]: element.split("/")[1] for element in self.id.split("-")}

    def get_color(self):
        return self.infos['color']
    
    