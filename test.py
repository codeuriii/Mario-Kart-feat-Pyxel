import pyxel

# Définir les propriétés du personnage et des projectiles
player_x = 80
player_y = 60
bullets_g = []
bullets_d = []
player_a = 80
player_b = 60

def update():
    global player_x, player_y
    global player_a, player_b
    global bullets_d, bullets_g
    # Déplacement du personnage avec les touches de direction
    if pyxel.btn(pyxel.KEY_LEFT):
        player_x -= 2
    if pyxel.btn(pyxel.KEY_RIGHT):
        player_x += 2
    if pyxel.btn(pyxel.KEY_UP):
        player_y -= 2
    if pyxel.btn(pyxel.KEY_DOWN):
        player_y += 2

    # Tirer une balle avec la touche M
    if pyxel.btnp(pyxel.KEY_M):
        bullets_d.append([player_x - 4, player_y + 8])  # Ajuster la position initiale de la balle
        # Tirer une balle avec la touche W
    if pyxel.btnp(pyxel.KEY_X):
        bullets_d.append([player_a - 4, player_b + 8])  # Ajuster la position initiale de la balle

    for bullet in bullets_d:
        bullet[0] += +10 # la balle se déplace vers la droite
    for bullet in bullets_g:
        bullet[0] += -10
      # Tirer une balle avec la touche L
    if pyxel.btnp(pyxel.KEY_L):
        bullets_g.append([player_x + 4, player_y + 8])  # Ajuster la position initiale de la balle
        # Tirer une balle avec la touche X
    if pyxel.btnp(pyxel.KEY_W):
        bullets_g.append([player_a + 4, player_b + 8])  # Ajuster la position initiale de la balle

    
    bullets_g[:] = [bullet for bullet in bullets_g if bullet[0] < pyxel.width]
    bullets_d[:] = [bullet for bullet in bullets_d if bullet[0] < pyxel.width]

def draw():
    pyxel.cls(11)  # Efface l'écran avec la couleur 0 (noir)
    # Dessiner le personnage x,y
    print(player_x, player_y, player_a, player_b)
    pyxel.rect(player_x, player_y, 16, 16, 11)
     # Dessiner le personnage a,b
    pyxel.rect(player_a, player_b, 16, 16, 8)
    # Dessiner les projectiles
    all_bullets = []
    all_bullets.extend(bullet_g) # Ajoute les bullets g dans all bullets
    all_bullets.extend(bullet_d)
    for bullet in all_bullets:
        pyxel.rect(bullet[0], bullet[1], 5, 2, 2)

pyxel.init(260, 180)  # Initialise une fenêtre de 260x180 pixels
pyxel.run(update, draw)  # Lance le jeu avec les fonctions de mise à jour et de dessin
