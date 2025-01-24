import pyxel as p

class Drawer:
    def __init__(self):
        self.cars = {
            "blue": (0, 0, 16, 16),
            "red": (16, 0, 16, 16),
            "green": (32, 0, 16, 16),
            "yellow": (48, 0, 16, 16)
        }

        self.roads = {
            "vertical": 0,
            "horizontal": 1,
            "vert_left": 2,
            "right_vert": 3,
            "desc_right": 4,
            "right_desc": 5
        }

        self.roads_data = {
            0: (0, 0, 32, 32),   # Vertical road │
            1: (32, 0, 32, 32),  # Horizontal road ─
            2: (32, 32, 32, 32),  # le bas vers la droite
            3: (32, 32, -32, 32),  # le bas vers la gauche
            4: (32, 32, -32, -32),  # Le haut vers la droite
            5: (32, 32, 32, -32),  # Le bas vers la gauche
        }
    
    def draw_car(self, color, x, y):
        p.blt(x, y, 0, *self.cars[color], 0)

    def draw_road_tile(self, x, y, index):
        if type(index) == int:
            p.blt(x, y, 1, *self.roads_data[index], 0)
        elif type(index) == str:
            p.blt(x, y, 1, *self.roads_data[self.roads[index]], 0)
