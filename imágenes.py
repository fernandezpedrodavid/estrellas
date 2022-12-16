import base64

with open("C:/Users/IBARRA/Pictures/Saved Pictures/posiciones.png", "rb")as image_file:
    cancha_64= base64.b64encode(image_file.read())
print (cancha_64)