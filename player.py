from car import Car

class Player:
    def __init__(self, websocket):
        self.websocket = websocket

    async def handle_message(self, message):
        if message.startswith("id"):
            self.set_id(message)
            self.parse_id()
            self.color = self.get_color()
            self.car = Car(0, 0, self.color)
            await self.websocket.send("get_players")
            await self.websocket.send("run")
            
    def set_id(self, id):
        self.id = id

    def parse_id(self):
        self.infos = {element.split("/")[0]: element.split("/")[1] for element in self.id.split("-")}

    def get_color(self):
        return self.infos['color']
    
