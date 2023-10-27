from tkinter import Tk, ttk
import tkinter as tk
from PIL import ImageTk, Image
from cell import Cell
from tkinter import messagebox
from detail_window import detailWindow
import cell

class MainWindow:

    def __init__(self, root, json_data):
        root.title("MainWindow")    # Título de la ventana  

        cells = [] # Inicializa una lista de celdas vacías

        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.geometry(f"+{int(x)}+{int(y)}")

        # Procesa json_data para crear las celdas
        for item in json_data:
            # Obtiene el valor asociado a la clave y lo almacena
            name = item.get("name") 
            descripcion = item.get("description")
            image_url = item.get("image_url")

            # Crea una instancia de la clase Cell utilizando los datos obtenidos
            cell = Cell(name, image_url, descripcion)
            cells.append(cell)  # Agrega la instancia recién creada a una lista llamada cells

        # Bucle for que ejecuta su contenido por cada una de las celdas
        for i, cell in enumerate(cells):

            # Crea una etiqueta que muestra la imagen, el texto y la posiciona
            label = ttk.Label(
                root, image=cell.Image_tk, text=cell.title, compound=tk.BOTTOM
            )

            # Ajusta la posición de manera horizontal
            label.grid(row=i, column=0)

            # Establece una acción al momento de clicar la etiqueta, ejecuta onButtonClicked
            label.bind(
                "<Button-1>",lambda event, cell=cell: self.onButtonClicked(cell)
            )
    
    # Función que ejecuta detailWindow
    def onButtonClicked(self, cell):
        detailWindow(cell)