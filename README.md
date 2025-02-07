
Vous vous trouvez actuellement sur la branche feat/items
Plusieurs branches sont disponibles  
feat/multi - La branche dédiée a l'affichage de multi joueur (breaking change oblige)  
feat/manette - La branche qui gère la manette (étonnant)  
fix/removetoken - La branche pour pouvoir se déconecter du serveur et actualiser les joueurs
feat/horspiste - La branche pour ralentir dans le hors piste
feat/correctdirection - La branche pour ajuster l'angle de la voiture pour l'aligner sur la route
feat/items - La branche pour gérer le comportement des objets

[ ] -> Pas fait  
[>] -> une branche dédiée, en cours  
[x] -> terminé  

# compte rendu:
**TO-DO:**
### ruben:
- [X] Dessiner pour chaque voiture de chaque couleur en diagonale 
- [x] faire le skin des items (voir liste des items)
- [>] Faire la mécanique des objets (classe, comportement etc) -> attendre le skin et le circuit (barrières) + oublie pas de pouvoir trail les carapaces verte, rouge et banane et bombe
    - [X] ajouter l'usage unique 
- [X] dessiner des tiles d'environement / un fond (herbe / terre ect ...)
- [X] dessiner les nombres
- [X] faire un player.hit() avec une rotation
- [ ] reglr le fait que les items ne partent pas 
- [ ] regler la desynchronisation des items quand lag
- [ ] Design les lignes d'item sur le terrain
- [ ] dessiner et implementer des particules de poussiere
- [ ] arreter le momentum du joueur si jamais il touche un bord + collision 

### nathan:
- [x] fix le this room is full error
- [x] faire un vrai circuit
- [x] dessiner les sprites de routes -> il manque le carrefour
- [x] faire le track 2
- [x] faire le track 3
- [x] Enlever le token si quelqu'un se déco
- [x] Correction de la direction
- [x] Faire le hors piste
- [>] Afficher les autres joueurs avec leur orientation + afficher les objets (attendre les objets)
- [>] Intégration a la manette
- [ ] Faire le comportement du bullet bill

Brainstorm

Liste des items
- Banane
- Carapace verte
- Carapace rouge
- Bleue ?
- Bombe
- Bullet bill ?
- Horn
