import pyxel as p

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1
        self.angle = 0

    def move(self):
        self.x += self.speed * p.cos(self.angle)
        self.y += self.speed * p.sin(self.angle)

    def keyboard_input(self):
        if p.btn(p.KEY_UP):
            self.speed += 1 
        elif p.btn(p.KEY_DOWN):
            self.speed -= 1
        elif p.btn(p.KEY_LEFT):
            self.angle -= 1
        elif p.btn(p.KEY_RIGHT):
            self.angle += 1

    def update_car(self):
        self.keyboard_input()
        self.move()

    def draw_car(self):
        p.rect(self.x, self.y, 10, 5, 7)
