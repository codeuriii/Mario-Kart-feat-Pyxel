from drawer import Drawer
import pyxel as p
from road import Roads

class Items:
    none = -1
    carapace_verte = 1
    carapace_rouge = 2
    carapace_bleue = 3
    peau_de_banane = 4
    bombe = 6
    horn = 7
    bullet_bill = 8
    is_line = [1]
    dont_move = [4, 6, 7]
    follow_road = [2, 3, 8]

class Item:
    def __init__(self, id, x, y, angle):
        self.id = id
        self.drawer = Drawer()
        self.x = float(x)
        self.y = float(y)
        self.angle = float(angle)
        self.speed = 5
        self.roads = Roads()
        self.deplacement = ""
        if self.id in Items.is_line:
            self.deplacement = "line"
        elif self.id in Items.dont_move:
            self.deplacement = "dont move"
        elif self.id in Items.follow_road:
            self.deplacement = "follow road"

    def update(self, tuile, old_tuile       ):
        match self.deplacement:
            case "line":
                self.x_vel = self.speed * p.cos(self.angle)
                self.y_vel = self.speed * p.sin(self.angle)
            case "dont move":
                pass
            case "follow road":
                # Ca va etre chiant mdr
                # Récupérer les coos de l'item
                self.x, self.y  # Ct facil
                # Récupérer la tuile correspondante
                tuile  # ct pa tro facil
                # a partir de la tuile correspondante, regarder d'ou tu viens, et donc eliminer d'ou tu viens et donc savoir dans quelle direction aller (il n'y a que deux entrée dans une road)
                # SI c'est un carrefour, savoir d'ou tu vient et aller tout droit.
                print("hell naw")
                pass

        self.x += self.x_vel
        self.y += self.y_vel

        if self.x < 0 or self.x > p.width or self.y < 0 or self.y > p.height:
            return False
        return True

    def draw(self):
        if int(self.id) != Items.none: 
            self.draw_item(self.x, self.y, int(self.id))

    def draw_item(self, x, y, id):
        self.drawer.draw_item(x, y, id)

    def launch_red_shell(self):
        pass

        

