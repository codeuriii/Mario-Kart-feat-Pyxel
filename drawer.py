import random
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
            },
            "white": {
                "haut": (80, 0, 16, 16),
                "bas": (80, 0, 16, -16),
                "gauche": (80, 16, 16, 16),
                "droite": (80, 16, -16, 16),
                "diagonale haut droite" : (80, 32, 16, 16),
                "diagonale haut gauche" : (80, 32, -16, 16),
                "diagonale bas droite" : (80, 32, 16, -16),
                "diagonale bas gauche" : (80, 32, -16, -16),
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

        self.items = {
            "boule_de_feu": 0,
            "carapace_verte": 1,
            "carapace_rouge": 2,
            "carapace_bleue": 3,
            "banane": 4,
            "fleur_de_feu": 5,
            "bombe": 6,
            "horn": 7,
            "bullet_bill": 8,
        }

        self.items_data = {
            0: (0, 0, 8, 8),  # Boule de feu
            1: (8, 0, 8, 8),  # Carapace verte
            2: (16, 0, 8, 8),  # Carapace rouge
            3: (24, 0, 8, 8),  # Carapace bleue
            4: (32, 0, 8, 8),  # Peau de banane
            5: (40, 0, 8, 8),  # Fleur de feu
            6: (48, 0, 8, 8),  # Bombe
            7: (56, 0, 8, 8),  # Klaxon
            8: (64, 0, 8, 8)  # Bullet Bill
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

        self.backgrounds = {
            "flowers": [
                (0, 104, 16, 16),
                (0, 104, 16, -16),
                (0, 104, -16, 16),
                (0, 104, -16, -16),
                
                (8, 104, 16, 16),
                (8, 104, 16, -16),
                (8, 104, -16, 16),
                (8, 104, -16, -16),
                
                (16, 104, 16, 16),
                (16, 104, 16, -16),
                (16, 104, -16, 16),
                (16, 104, -16, -16),
                
                (24, 104, 16, 16),
                (24, 104, 16, -16),
                (24, 104, -16, 16),
                (24, 104, -16, -16),
                
                (32, 104, 16, 16),
                (32, 104, 16, -16),
                (32, 104, -16, 16),
                (32, 104, -16, -16)
            ],
            "grass": [
                (0, 120, 16, 16),
                (0, 120, 16, -16),
                (0, 120, -16, 16),
                (0, 120, -16, -16),

                (8, 120, 16, 16),
                (8, 120, 16, -16),
                (8, 120, -16, 16),
                (8, 120, -16, -16),

                (16, 120, 16, 16),
                (16, 120, 16, -16),
                (16, 120, -16, 16),
                (16, 120, -16, -16),

                (24, 120, 16, 16),
                (24, 120, 16, -16),
                (24, 120, -16, 16),
                (24, 120, -16, -16),

                (32, 120, 16, 16),
                (32, 120, 16, -16),
                (32, 120, -16, 16),
                (32, 120, -16, -16)
            ],
            "rocks": [
                (0, 136, 16, 16),
                (0, 136, 16, -16),
                (0, 136, -16, 16),
                (0, 136, -16, -16),

                (8, 136, 16, 16),
                (8, 136, 16, -16),
                (8, 136, -16, 16),
                (8, 136, -16, -16),

                (16, 136, 16, 16),
                (16, 136, 16, -16),
                (16, 136, -16, 16),
                (16, 136, -16, -16),

                (24, 136, 16, 16),
                (24, 136, 16, -16),
                (24, 136, -16, 16),
                (24, 136, -16, -16),

                (32, 136, 16, 16),
                (32, 136, 16, -16),
                (32, 136, -16, 16),
                (32, 136, -16, -16)
            ],
            "dirt": [
                (0, 152, 16, 16),
                (0, 152, 16, -16),
                (0, 152, -16, 16),
                (0, 152, -16, -16),

                (8, 152, 16, 16),
                (8, 152, 16, -16),
                (8, 152, -16, 16),
                (8, 152, -16, -16),

                (16, 152, 16, 16),
                (16, 152, 16, -16),
                (16, 152, -16, 16),
                (16, 152, -16, -16),

                (24, 152, 16, 16),
                (24, 152, 16, -16),
                (24, 152, -16, 16),
                (24, 152, -16, -16),

                (32, 152, 16, 16),
                (32, 152, 16, -16),
                (32, 152, -16, 16),
                (32, 152, -16, -16)
            ]
        }

        self.item_box = (0, 8, 16, 16)
        self.damier_vertical = (64, 0, 16, 32)
        self.damier_horizontal = (80, 0, 32, 16)
        self.item_case = (72, 0, 16, 16)
    
    def get_random_background(self, background):
        return random.choice(self.backgrounds[background])
    
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

    def draw_road_tile(self, x, y, index):
        if type(index) == int:
            p.blt(x, y, 1, *self.roads_data[index], p.COLOR_BROWN)
        elif type(index) == str:
            p.blt(x, y, 1, *self.roads_data[self.roads[index]], p.COLOR_BROWN)

    def draw_damier(self, x, y, inline):
        x *= 32
        y *= 32
        if inline:
            y += 8
            p.blt(x, y, 1, *self.damier_horizontal, p.COLOR_BROWN)
        else:
            x += 8
            p.blt(x, y, 1, *self.damier_vertical, p.COLOR_BROWN)

    def draw_item(self, x, y, item):
        if isinstance(item, int):
            if item >= 0:
                p.blt(x, y, 2, *self.items_data[item], 0)
        else:
            print(f"Expected an integer for id ({item}), but got {type(item)}")
    
    def draw_item_box(self, x, y):
        p.blt(x, y, 2, *self.item_box, p.COLOR_BLACK)

    def draw_background(self, x, y, tile):
        p.blt(x, y, 1, *tile)

    def draw_item_case(self):
        p.blt(p.width - 24, 6, 2, *self.item_case, p.COLOR_BLACK)
