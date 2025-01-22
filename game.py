import pyxel as p
from player import Player

class Game:
    def __init__(self, websocket):
        p.init(160, 120)
        p.run(self.update, self.draw)
        self.websocket = websocket
        self.player = Player(self.websocket)

    def update(self):
        pass

    def draw(self):
        p.cls(0)
        p.rect(10, 10, 20, 20, 9)

    async def run(self):
        p.run(self.update, self.draw)
    
    async def player_send_id_request(self):
        await self.player.send_id_request()
    
    async def player_receive_message(self):
        await self.player.receive_message()
