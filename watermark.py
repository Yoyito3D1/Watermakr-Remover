from skimage import io
from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import os

# ---------- FUNCIONS DE FILTRAT ----------
def select_pixel2(r, g, b):
    return 175 < r < 250 and 175 < g < 250 and 175 < b < 250

def handle(imgs):
    for i in range(imgs.shape[0]):
        for j in range(imgs.shape[1]):
            if select_pixel2(imgs[i][j][0], imgs[i][j][1], imgs[i][j][2]):
                imgs[i][j][0] = imgs[i][j][1] = imgs[i][j][2] = 255
    return imgs

# ---------- CONVERTIR PDF EN IMATGES ----------
images = convert_from_path('./marca_aigua.pdf')
output_dir = './Resultats'
os.makedirs(output_dir, exist_ok=True)

# Guardar imatges processades amb noms com img001.jpg, img002.jpg...
for index, img in enumerate(images, start=1):
    img_np = np.array(img)
    img_np = handle(img_np)
    filename = os.path.join(output_dir, f'img{index:03}.jpg')  # padding amb zeros
    io.imsave(filename, img_np)
    print(f"Pàgina {index} processada i guardada com: {filename}")

# ---------- ORDENAR IMATGES I GENERAR PDF ----------
def extract_number(filename):
    # extreu el número del nom com a enter per ordenar correctament
    import re
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else -1

image_files = sorted(
    [f for f in os.listdir(output_dir) if f.endswith('.jpg') or f.endswith('.png')],
    key=extract_number
)
image_paths = [os.path.join(output_dir, f) for f in image_files]

# Obrir les imatges amb PIL
pil_images = [Image.open(path).convert('RGB') for path in image_paths]

# Guardar el PDF final
if pil_images:
    output_pdf = './resultat_final.pdf'
    pil_images[0].save(output_pdf, save_all=True, append_images=pil_images[1:])
    print(f"PDF final guardat correctament a: {output_pdf}")
else:
    print("❌ No s'han trobat imatges per crear el PDF.")
