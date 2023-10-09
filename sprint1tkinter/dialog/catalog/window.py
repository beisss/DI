from tkinter import Tk, ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox

class MainWindow:
    def onButtonClicked(cell):
        message = "Has hecho click en la celda "+cell.title
        messagebox.showinfo("Información",message)

    def __init__(self, root):
        root.title("MainWindow")

        self.cells = [
            Cell("Charizard","/Users/beis/Documentos/di/sprint1tkinter/dialog/catalog/data/edited/charizard.jpeg"),
            Cell("Gengar","/Users/beis/Documentos/di/sprint1tkinter/dialog/catalog/data/edited/gengar.png"),
            Cell("Pikachu","/Users/beis/Documentos/di/sprint1tkinter/dialog/catalog/data/edited/pikachu.png"),
            Cell("Snorlax","/Users/beis/Documentos/di/sprint1tkinter/dialog/catalog/data/edited/snorlax.jpeg"),
            Cell("Turtwig","/Users/beis/Documentos/di/sprint1tkinter/dialog/catalog/data/edited/turtwig.png"),
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(
                root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM
            )
            label.grid(row=i, column=0)
            label.bind(
                "<Button-1>",lambda event, cell=cell: self.onButtonClicked(cell)
            )