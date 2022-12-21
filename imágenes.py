import base64


with open("C:/Users/IBARRA/Pictures/Saved Pictures/pesos.png", "rb")as image_file:
    puesto_64= base64.b64encode(image_file.read()).decode('utf-8')
print (puesto_64)
