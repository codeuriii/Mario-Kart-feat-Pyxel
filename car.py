import pyxel as p
from drawer import Drawer

class Car:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.speed = 0
        self.angle = 270
        self.color = color
        self.drawer = Drawer()
        self.speed_turn = 5
        self.speed_max = 3
        self.acceleration = 0.1
        self.deceleration = 0.05

    def move(self):
        self.x += self.speed * p.cos(self.angle)
        self.y += self.speed * p.sin(self.angle)
        self.speed_turn = max(1, 5 - self.speed * 0.1)
        if self.speed > self.speed_max:
            self.speed = self.speed_max
        elif self.speed < -self.speed_max:
            self.speed = -self.speed_max
        self.speed *= 0.99

    def keyboard_input(self):
        if p.btn(p.KEY_UP):
            self.speed += self.acceleration
        elif p.btn(p.KEY_DOWN):
            self.speed -= self.deceleration
        if p.btn(p.KEY_LEFT):
            self.angle -= self.speed_turn
        if p.btn(p.KEY_RIGHT):
            self.angle += self.speed_turn

    def update(self):
        self.move()
        self.keyboard_input()

    def draw_car(self):
        self.drawer.draw_car(self.color, self.x, self.y)
