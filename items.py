
from drawer import Drawer

class Items:
    boule_de_feu = 0,
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

    def draw_item(self, x, y):
        self.drawer.draw_item(x, y, self.id)
