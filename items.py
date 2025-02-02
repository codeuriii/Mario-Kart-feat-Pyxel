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
        self.id = int(id)
        self.drawer = Drawer()
        self.x = float(x)
        self.y = float(y)
        self.svgd_x = self.x
        self.svgd_y = self.y
        self.x_vel = 0
        self.y_vel = 3
        self.angle = float(angle)
        self.speed = 3
        self.roads = Roads()
        self.deplacement = ""
        if self.id in Items.is_line:
            self.deplacement = "line"
        elif self.id in Items.dont_move:
            self.deplacement = "dont move"
        elif self.id in Items.follow_road:
            self.deplacement = "follow road"
        self.item_offset_timer = []
        self.item_offset_callbacks = []
        self.is_waiting_for_offset = False
        self.n_iterations = 4

    def set_callbacks_for_offset(self, callbacks, n=4):
        self.is_waiting_for_offset = True
        self.item_offset_callbacks = callbacks
        self.n_iterations = n

    def wait_for_changing(self):
        if self.is_waiting_for_offset:
            self.item_offset_timer.append("hehe")
        if len(self.item_offset_timer) > self.n_iterations:
            for callback in self.item_offset_callbacks:
                callback()
            self.is_waiting_for_offset = False
            self.item_offset_callbacks.clear()
            self.item_offset_timer.clear()

    def update(self, tuile, old_tuile):
        tile_x, tile_y = int(self.x // 32) * 32, int(self.y // 32) * 32
        match self.deplacement:
            case "line":
                self.x_vel = self.speed * p.cos(self.angle)
                self.y_vel = self.speed * p.sin(self.angle)
                
            case "dont move":
                pass

            case "follow road":
                def go_up():
                    self.y_vel = -self.speed
                def go_down():
                    self.y_vel = self.speed
                def reset_up_down():
                    self.y_vel = 0
                
                def go_right():
                    self.x_vel = self.speed
                def go_left():
                    self.x_vel = -self.speed
                def reset_right_left():
                    self.x_vel = 0

                if tuile != old_tuile:
                    match old_tuile:
                        case self.roads.horizontal:
                            # Si on arrive d'un horizontal
                            # On a horizontal, donc on arrive d'un coté, donc on monte
                            if tuile in [self.roads.haut_droite, self.roads.haut_gauche]:
                                # print(f"self.x {self.x}, svgd_x {self.svgd_x}, tile_x {tile_x}")
                                self.set_callbacks_for_offset([reset_right_left, go_up])

                            # On arrive d'un coté et le virage contient une connection en bas et sur un coté, donc on descend
                            elif tuile in [self.roads.bas_droite, self.roads.bas_gauche]:
                                self.set_callbacks_for_offset([reset_right_left, go_down], 6 if tuile == self.roads.bas_droite else 5)
                            # On s'en fiche du carrefour car on va tout droit donc on change rien (on vient d'horizontal)
                        
                        case self.roads.vertical:
                            # Si on arrive d'une route verticale
                            # On a verticale, donc on arrive soit d'en haut, soit d'en bas
                            if tuile in [self.roads.haut_droite, self.roads.bas_droite]:
                                self.set_callbacks_for_offset([reset_up_down, go_right])
                            elif tuile in [self.roads.haut_gauche, self.roads.bas_gauche]:
                                self.set_callbacks_for_offset([reset_up_down, go_left], 6 if tuile == self.roads.bas_gauche else 4)
                            # Pareil pour le carrefour, on ne change rien
                        
                # a partir de la tuile correspondante, regarder d'ou tu viens, et donc eliminer d'ou tu viens et donc savoir dans quelle direction aller (il n'y a que deux entrée dans une road)
                # SI c'est un carrefour, savoir d'ou tu vient et aller tout droit.

        self.wait_for_changing()

        self.svgd_x = self.x
        self.svgd_y = self.y
        self.x += self.x_vel
        self.y += self.y_vel

        if self.x < 0 or self.x > p.width or self.y < 0 or self.y > p.height:
            return False
        return True

    def draw(self):
        if self.id != Items.none: 
            self.draw_item(self.x, self.y, int(self.id))

    def draw_item_case(self):
        self.drawer.draw_item_case()

    def draw_item(self, x, y, id):
        self.drawer.draw_item(x, y, id)
       
