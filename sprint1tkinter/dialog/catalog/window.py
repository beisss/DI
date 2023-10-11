from tkinter import Tk, ttk
import tkinter as tk
from PIL import ImageTk, Image
from cell import Cell
from tkinter import messagebox
from detail_window import detailWindow

class MainWindow:
    def onButtonClicked(self, cell):
        detailWindow(cell)

    def __init__(self, root):
        root.title("MainWindow")    # Título de la ventana  

        # Lista de objetos
        self.cells = [
            Cell("Charizard","/Users/beis/Documentos/di/sprint1tkinter/dialog/catalog/data/unedited/charizard.jpeg","Charizard es un poderoso Pokémon de tipo Fuego/Volador conocido por su imponente apariencia y su aliento de fuego. Es un símbolo de valentía y determinación."),
            Cell("Gengar","/Users/beis/Documentos/di/sprint1tkinter/dialog/catalog/data/unedited/gengar.png","Gengar es un astuto Pokémon de tipo Fantasma/Veneno. Siempre acecha en las sombras y disfruta asustando a los incautos. Es un maestro de las artes furtivas."),
            Cell("Pikachu","/Users/beis/Documentos/di/sprint1tkinter/dialog/catalog/data/unedited/pikachu.png","Pikachu es la mascota más icónica de Pokémon, conocida por su ternura y su ataque característico, el Rayo. Es un compañero leal y entrañable en las aventuras de entrenadores."),
            Cell("Snorlax","/Users/beis/Documentos/di/sprint1tkinter/dialog/catalog/data/unedited/snorlax.jpeg","Snorlax es un masivo Pokémon de tipo Normal que suele dormir y bloquear caminos. Su apetito insaciable y su naturaleza tranquila lo hacen un personaje único."),
            Cell("Turtwig","/Users/beis/Documentos/di/sprint1tkinter/dialog/catalog/data/unedited/turtwig.png","Turtwig es un Pokémon de tipo Planta. Es conocido por llevar una pequeña planta en su espalda y representa la fuerza de la naturaleza en su crecimiento lento pero constante."),
        ]

        for i, cell in enumerate(self.cells):
            img = Image.open(cell.path) # Abre una sobre la ruta cell.path
            imgResized = img.resize((100,100),Image.Resampling.LANCZOS)

            cell.image_tk = ImageTk.PhotoImage(imgResized)

            label = ttk.Label(
                root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM
            )
            label.grid(row=i, column=0)
            label.bind(
                "<Button-1>",lambda event, cell=cell: self.onButtonClicked(cell)
            )