from io import BytesIO
import tkinter as tk
from PIL import Image, ImageTk
import requests

class Cell:

    # Método constructor al que importamos los datos para usar luego
    def __init__(self, title, image_url, desc):
        # Asigna el título, la URL de la imagen
        self.title = title
        self.image_url = image_url

        # Realiza una solicitud HTTP GET para obtener la URL
        response = requests.get(image_url)
        # Abre la imagen a partir de los datos binarios de la respuesta HTTP
        img_data = Image.open(BytesIO(response.content))
        # Convierte la imagen en un objeto de tipo PhotoImage para su uso en interfaz gráfica
        self.Image_tk = ImageTk.PhotoImage(img_data)
        self.desc = desc