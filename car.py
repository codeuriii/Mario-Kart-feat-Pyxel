import pyxel as p
import statistics as s
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
        self.speed_max_svgd = self.speed_max
        self.acceleration = 0.1
        self.deceleration = 0.05

    def get_center(self):
        return self.x + 8, self.y + 8
    
    def draw_line(self):
        end_x = self.x + 10 * p.cos(self.angle)
        end_y = self.y + 10 * p.sin(self.angle)
        p.line(self.x + 8 , self.y + 8, end_x + 8, end_y + 8, 7)

    def correct_angle(self):
        angle = round(self.angle / 45) * 45
        liste = [self.angle for _ in range(3)]
        liste.append(angle)
        self.angle = s.mean(liste)

    def move(self, hors_piste):
        self.x += self.speed * p.cos(self.angle)
        self.y += self.speed * p.sin(self.angle)
        self.speed_turn = max(1, 5 - self.speed * 0.1)
        if hors_piste:
            self.speed_max = 1
        if self.speed > self.speed_max:
            self.speed = self.speed_max
        elif self.speed < -self.speed_max:
            self.speed = -self.speed_max
        self.speed_max = self.speed_max_svgd
        self.speed *= 0.99

    def keyboard_input(self):
        if p.btn(p.KEY_UP) or p.btn(p.KEY_Z):
            self.speed += self.acceleration
        elif p.btn(p.KEY_DOWN) or p.btn(p.KEY_S):
            self.speed -= self.deceleration
        if p.btn(p.KEY_LEFT) or p.btn(p.KEY_Q):
            self.angle -= self.speed_turn
        if p.btn(p.KEY_RIGHT) or p.btn(p.KEY_D):
            self.angle += self.speed_turn
        
        if not any([p.btn(p.KEY_LEFT), p.btn(p.KEY_RIGHT), p.btn(p.KEY_Q), p.btn(p.KEY_D)]):
            self.correct_angle()

    def update(self, hors_piste):
        self.move(hors_piste)
        self.keyboard_input()

    def draw_car(self):
        self.draw_line()
        self.drawer.draw_car(self.color, self.x, self.y, self.angle)
