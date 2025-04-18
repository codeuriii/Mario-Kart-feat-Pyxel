from drawer import Drawer
import pyxel as p

class Items:
    none = -1
    carapace_verte = 1
    carapace_rouge = 2
    carapace_bleue = 3
    peau_de_banane = 4
    bombe = 6
    horn = 7
    bullet_bill = 8

class Item:
    def __init__(self, id, owner):
        self.id = id
        self.drawer = Drawer()
        self.x = 0
        self.y = 0
        self.x_vel = 0
        self.y_vel = 0
        self.speed = 5
        self.owner = owner
        self.speed = 5

    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel

        if self.x < 0 or self.x > p.width or self.y < 0 or self.y > p.height:
            return False
        return True

    def draw(self):
        pass 

    def draw_item_case(self):
        self.drawer.draw_item_case()

    def draw_item(self, x, y, id=None):
        if not id:
            id = self.id
        self.drawer.draw_item(x, y, id)

    def launch_green_shell(self):
        pass

    def launch_red_shell(self):
        pass

        

