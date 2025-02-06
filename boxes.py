
from drawer import Drawer

class Box:
    def __init__(self, x: int, y: int, inline: bool):
        self.drawer = Drawer()
        self.x = x
        self.y = y
        x *= 32
        y *= 32
        if inline:
            self.x1 = x
            self.x2 = x + 16
            self.y1 = y + 8
            self.y2 = y + 8
        else:
            self.x1 = x + 8
            self.x2 = x + 8
            self.y1 = y
            self.y2 = y + 16
    
    def draw(self):
        self.drawer.draw_item_box(self.x1, self.y1)
        self.drawer.draw_item_box(self.x2, self.y2)