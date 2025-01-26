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
        self.fireball_arr = []
        self.item_timer = 100 # temporary number for testing: TODO: adjust

    def update(self, player_angle):
        match self.id:
            case Items.fleur_de_feu:
                self.use_fireball(player_angle)

        self.x += self.x_vel
        self.y += self.y_vel

        if self.x < 0 or self.x > p.width or self.y < 0 or self.y > p.height:
            return False
        return True

    def draw(self):
        match self.id:
            case Items.fleur_de_feu:
                if not self.x == 10 and not self.y == 10:
                    self.drawer.draw_item(self.x, self.y, Items.boule_de_feu)
                else:
                    self.draw_item(self.x, self.y)

    def draw_item(self, x, y, id=None):
        if not id:
            id = self.id
        
        if id == Items.fleur_de_feu:
            self.drawer.draw_item(x, y, Items.boule_de_feu)
        else:
            self.drawer.draw_item(x, y, id)

    def use_fireball(self, player_angle):
        self.x_vel = self.speed * p.cos(player_angle)
        self.y_vel = self.speed * p.sin(player_angle)

    def launch_green_shell(self):
        pass

    def launch_red_shell(self):
        pass

        

