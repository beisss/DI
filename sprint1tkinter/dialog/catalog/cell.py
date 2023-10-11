import tkinter as tk
from PIL import Image, ImageTk

class Cell:

    # Método constructor al que importamos los datos para usar luego
    def __init__(self, title, path, desc):
        self.title = title
        self.path = path
        self.image_tk = ImageTk.PhotoImage(file=self.path)
        self.desc = desc
