import pyxel as p
from drawer import Drawer

road_map = [
    [1, 2, 1, 1, 1, 3, 5, 1, 1, 1],  # Horizontal road with turns
    [4, -1, -1, -1, -1, -1, 2, 5, -1, 1],  # Left turns and open spaces
    [4, 1, 0, 1, 0, 3, 2, 1, 0, 1],  # Connecting the roads
    [4, 1, 5, 1, 0, 3, 2, 5, 1, 1],  # Additional roads connecting
    [4, 1, 1, 3, 5, 1, 1, 2, 1, 1],  # Making turns and joining paths
    [4, 1, 1, 0, 0, 2, 1, 1, 0, 1],  # Final turns
    [-1, 1, 3, 5, 1, 0, 1, 1, 1, -1],  # Ending the path (some open spaces)
]

class Road:
    def __init__(self):
        self.road_map = road_map
        self.drawer = Drawer()

    def draw_road(self):
        for y in range(5):
            for x in range(5):
                tile = self.road_map[y][x]
                if tile >= 0:
                    self.drawer.draw_road_tile(x * 32, y * 32, tile)
