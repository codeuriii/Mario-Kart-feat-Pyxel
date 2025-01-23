import pyxel as p
import os

class Car:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.speed = 1
        self.angle = 270
        self.color = color

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
        p.rect(self.x, self.y, 10, 5, 7)
