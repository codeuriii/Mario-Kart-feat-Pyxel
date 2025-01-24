from drawer import Drawer

class Roads:
    empty = -1
    vertical = 0
    horizontal = 1
    haut_gauche = 5
    haut_droite = 4
    bas_droite = 3
    bas_gauche = 2

class Road:
    def __init__(self):
        self.drawer = Drawer()
        roads = Roads()
        self.track_1 = [
            [roads.empty, roads.bas_droite,  roads.horizontal, roads.horizontal,  roads.horizontal,  roads.horizontal, roads.horizontal, roads.bas_gauche, roads.empty],
            [roads.empty, roads.vertical,    roads.empty,      roads.empty,       roads.empty,       roads.empty,      roads.empty,      roads.vertical,   roads.empty],
            [roads.empty, roads.haut_droite, roads.horizontal, roads.horizontal,  roads.bas_gauche,  roads.empty,      roads.empty,      roads.vertical,   roads.empty],
            [roads.empty, roads.empty,       roads.empty,      roads.empty,       roads.vertical,    roads.empty,      roads.empty,      roads.vertical,   roads.empty],
            [roads.empty, roads.bas_droite,  roads.horizontal, roads.horizontal,  roads.haut_gauche, roads.empty,      roads.empty,      roads.vertical,   roads.empty],
            [roads.empty, roads.vertical,    roads.empty,      roads.empty,       roads.empty,       roads.empty,      roads.empty,      roads.vertical,   roads.empty],
            [roads.empty, roads.haut_droite, roads.horizontal, roads.horizontal,  roads.horizontal,  roads.horizontal, roads.horizontal, roads.haut_gauche, roads.empty]
        ]

    def draw_road(self):
        for y in range(7):
            for x in range(9):
                tile = self.track_1[y][x]
                if tile >= 0:
                    self.drawer.draw_road_tile(x * 32, y * 32, tile)
