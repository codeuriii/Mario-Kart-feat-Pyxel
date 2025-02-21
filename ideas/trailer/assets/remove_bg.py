import sys
from PIL import Image

def remove_black_pixels(image_path):
    # Ouvrir l'image
    img = Image.open(image_path).convert("RGBA")  # Convertir en mode RGBA (avec alpha)
    pixels = img.load()

    # Parcourir tous les pixels
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if (r, g, b) == (0, 0, 0):  # Si le pixel est noir
                pixels[x, y] = (0, 0, 0, 0)  # Le rendre transparent

    # Remplacer l'image d'origine
    img.save(image_path, "PNG")
    print(f"Image mise à jour : {image_path}")

# Vérifier si un argument est fourni
if len(sys.argv) < 2:
    print("Usage: python script.py image.png")
else:
    remove_black_pixels(sys.argv[1])
