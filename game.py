import pyxel as p

class Game:
    def __init__(self):
        p.init(160, 120)
        p.run(self.update, self.draw)

    def update(self):
        pass 

    def draw(self):
        p.cls(0)
        p.rect(10, 10, 20, 20, 9)
