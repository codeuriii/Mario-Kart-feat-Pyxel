import pyxel as p

class Drawer:
    def __init__(self):
        self.cars = {
            "blue": {
                "haut": (0, 0, 16, 16),
                "bas": (0, 0, 16, -16),
                "gauche": (0, 16, 16, 16),
                "droite": (0, 16, -16, 16),
                "diagonale haut droite" : (0, 32, 16, 16),
                "diagonale haut gauche" : (0, 32, -16, 16),
                "diagonale bas droite" : (0, 32, 16, -16),
                "diagonale bas gauche" : (0, 32, -16, -16),
            },
            "red": {
                "haut": (16, 0, 16, 16),
                "bas": (16, 0, 16, -16),
                "gauche": (16, 16, 16, 16),
                "droite": (16, 16, -16, 16),
                "diagonale haut droite" : (16, 32, 16, 16),
                "diagonale haut gauche" : (16, 32, -16, 16),
                "diagonale bas droite" : (16, 32, 16, -16),
                "diagonale bas gauche" : (16, 32, -16, -16),
            },
            "green": {
                "haut": (32, 0, 16, 16),
                "bas": (32, 0, 16, -16),
                "gauche": (32, 16, 16, 16),
                "droite": (32, 16, -16, 16),
                "diagonale haut droite" : (32, 32, 16, 16),
                "diagonale haut gauche" : (32, 32, -16, 16),
                "diagonale bas droite" : (32, 32, 16, -16),
                "diagonale bas gauche" : (32, 32, -16, -16),
            },
            "yellow": {
                "haut": (48, 0, 16, 16),
                "bas": (48, 0, 16, -16),
                "gauche": (48, 16, 16, 16),
                "droite": (48, 16, -16, 16),
                "diagonale haut droite" : (48, 32, 16, 16),
                "diagonale haut gauche" : (48, 32, -16, 16),
                "diagonale bas droite" : (48, 32, 16, -16),
                "diagonale bas gauche" : (48, 32, -16, -16),
            }
        }

        self.roads = {
            "vertical": 0,
            "horizontal": 1,
            "haut_gauche": 2,
            "haut_droite": 3,
            "bas_droite": 4,
            "bas_gauche": 5,
            "carrefour": 6
        }

        self.roads_data = {
            0: (0, 0, 32, 32),   # Vertical road │
            1: (32, 0, 32, 32),  # Horizontal road ─
            2: (32, 32, 32, 32),  # le bas vers la droite
            3: (32, 32, -32, 32),  # le bas vers la gauche
            4: (32, 32, -32, -32),  # Le haut vers la droite
            5: (32, 32, 32, -32),  # Le bas vers la gauche
            6: (0, 64, 32, 32)  # Carrefour
        }
    
    def draw_car(self, color, x, y, angle):
        angle = round(angle / 45) * 45 % 360  # Ensure rounding to nearest 45°
        if angle == 0:
            p.blt(x, y, 0, *self.cars[color]["gauche"], 0) 
        elif angle == 180:
            p.blt(x, y, 0, *self.cars[color]["droite"], 0)
        elif angle == 270:
            p.blt(x, y, 0, *self.cars[color]["haut"], 0)
        elif angle == 90:
            p.blt(x, y, 0, *self.cars[color]["bas"], 0)
        elif angle == 315:
            p.blt(x, y, 0, *self.cars[color]["diagonale haut droite"], 0)
        elif angle == 225:
            p.blt(x, y, 0, *self.cars[color]["diagonale haut gauche"], 0)
        elif angle == 135:
            p.blt(x, y, 0, *self.cars[color]["diagonale bas gauche"], 0)
        elif angle == 45:
            p.blt(x, y, 0, *self.cars[color]["diagonale bas droite"], 0)
        # p.blt(x, y, 0, *self.cars[color], 0)

    def draw_road_tile(self, x, y, index):
        if type(index) == int:
            p.blt(x, y, 1, *self.roads_data[index], p.COLOR_BROWN)
        elif type(index) == str:
            p.blt(x, y, 1, *self.roads_data[self.roads[index]], p.COLOR_BROWN)
