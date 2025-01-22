from car import Car
import websockets
import asyncio

class Player:
    def __init__(self, websocket):
        self.websocket = websocket

    def generate_token(self):
        return hex(id(object()))[2:]
    

    def handle_message(self, message):
        if message.startwith("id"):
            self.set_id(message)
            self.parse_id()
            self.color = self.get_color()
            self.car = Car(color=self.color)
            print(f"Received id from server: {message}")
            print(self.id)
            print(self.color)
            print(self.infos)

    def set_id(self, id):
        self.id = id

    def parse_id(self):
        self.infos = {element.split("/")[0]: element.split("/")[1] for element in self.id.split("-")}

    def get_color(self):
        return self.infos['color']
    
