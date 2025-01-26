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
    def __init__(self, id):
        self.id = id
        self.drawer = Drawer()
        self.x = 0
        self.y = 0
        self.x_vel = 0
        self.y_vel = 0
        self.speed = 5
        self.speed = 5
        self.is_single_use = False
        self.used = False

    def update(self, player_x, player_y, player_angle):
        print(f"used? {self.used}")
        print(f"single use? {self.is_single_use}")
        self.check_single_use()
        self.check_item_use(player_x, player_y, player_angle)

        self.x += self.x_vel
        self.y += self.y_vel

        if self.x < 0 or self.x > p.width or self.y < 0 or self.y > p.height:
            return False
        return True

    def check_single_use(self):
        match int(self.id):
            case Items.carapace_verte:
                self.is_single_use = True

    def check_item_use(self, player_x, player_y, player_angle):
        if self.used:
            return

        if p.btnp(p.KEY_E):
            if self.is_single_use:
                self.used = True
            match int(self.id):
                case Items.carapace_verte:
                    self.x = player_x
                    self.y = player_y
                    self.launch_green_shell(player_angle)

    def draw(self):
        self.draw_item(self.x, self.y, int(self.id))

    def draw_item(self, x, y, id):
        self.drawer.draw_item(x, y, id)

    def launch_green_shell(self, player_angle):
        self.x_vel = self.speed * p.cos(player_angle)
        self.y_vel = self.speed * p.sin(player_angle)

    def launch_red_shell(self):
        pass

        

