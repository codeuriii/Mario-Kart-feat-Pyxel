from drawer import Drawer
import pyxel as p

class Items:
    none = -1
    boule_de_feu = 0
    carapace_verte = 1
    carapace_rouge = 2
    carapace_bleue = 3
    peau_de_banane = 4
    fleur_de_feu = 5
    bombe = 6
    horn = 7
    bullet_bill = 8

class Item:
    def __init__(self, id):
        self.id = id
        self.drawer = Drawer()
        self.x = 0
        self.y = 0
        self.x_vel = 0
        self.y_vel = 0 
        self.speed = 5

    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def draw(self):
        match self.id:
            case Items.fleur_de_feu:
                if not self.x == 10 and not self.y == 10:
                    self.drawer.draw_item(self.x, self.y, self.id)
                else:
                    self.draw_item(self.x, self.y)

    def draw_item(self, x, y):
        self.drawer.draw_item(x, y, self.id)

    def use_fireball(self, player_angle):
        self.x_vel = self.speed * p.cos(player_angle)
        self.y_vel = self.speed * p.sin(player_angle)

    def throw_fireball(self):
        pass

    def launch_green_shell(self):
        pass

    def launch_red_shell(self):
        pass

        

