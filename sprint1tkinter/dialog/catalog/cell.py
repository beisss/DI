import tkinter as tk
from PIL import Image, ImageTk


class Cell:
    def __init__(self, title, path, desc):
        self.title = title
        self.path = path
        self.image_tk = ImageTk.PhotoImage(file=self.path)
        self.desc = desc
