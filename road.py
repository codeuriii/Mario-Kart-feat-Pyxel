from drawer import Drawer

class Roads:
    empty = -1
    vertical = 0
    horizontal = 1
    haut_gauche = 5
    haut_droite = 4
    bas_droite = 3
    bas_gauche = 2
    carrefour = 6

class Road:
    def __init__(self):
        self.drawer = Drawer()

    def draw_road(self, track):
        for y in range(7):
            for x in range(9):
                tile = track[y][x]
                if tile >= 0:
                    self.drawer.draw_road_tile(x * 32, y * 32, tile)
