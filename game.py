import pyxel as p
from player import Player

class Game:
    def __init__(self):
        p.init(160, 120)
        p.run(self.update, self.draw)
        self.player = Player()

    def update(self):
        pass

    def draw(self):
        p.cls(0)
        p.rect(10, 10, 20, 20, 9)

    def run(self):
        p.run(self.update, self.draw)
    
    async def broadcast(self):
        await self.player.receive_message()