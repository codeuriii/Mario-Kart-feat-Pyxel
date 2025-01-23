import pyxel as p

class Drawer:
    def __init__(self):
        self.blue_car = (0, 0, 16, 16)
        self.red_car = (16, 0, 16, 16)
        self.green_car = (32, 0, 16, 16)
        self.yellow_car = (48, 0, 16, 16)
        self.cars = {
            "blue": self.blue_car,
            "red": self.red_car,
            "green": self.green_car,
            "yellow": self.yellow_car
        }
    
    def draw_car(self, color, x, y):
        p.blt(x, y, 0, *self.cars[color], 0)