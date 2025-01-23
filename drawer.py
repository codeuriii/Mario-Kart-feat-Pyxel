import pyxel as p

class Drawer:
    def __init__(self):
        self.cars = {
            "blue": (0, 0, 16, 16),
            "red": (16, 0, 16, 16),
            "green": (32, 0, 16, 16),
            "yellow": (48, 0, 16, 16)
        }
    
    def draw_car(self, color, x, y):
        p.blt(x, y, 0, *self.cars[color], 0)