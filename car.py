import pyxel as p
from drawer import Drawer

class Car:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.speed = 1
        self.angle = 270
        self.color = color
        self.drawer = Drawer()

    def move(self):
        self.x += self.speed * p.cos(self.angle)
        self.y += self.speed * p.sin(self.angle)
        self.speed *= 0.99

    def keyboard_input(self):
        if p.btnp(p.KEY_UP):
            self.speed += 100
        elif p.btnp(p.KEY_DOWN):
            self.speed -= 100
        if p.btnp(p.KEY_LEFT):
            self.angle -= 10
        if p.btnp(p.KEY_RIGHT):
            self.angle += 10

    def update(self):
        self.move()
        self.keyboard_input()

    def draw_car(self):
        p.blt(self.x, self.y, 0, 0, 0, 16, 16, p.COLOR_BLACK)
