from tkinter import Tk, ttk
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from cell import Cell
from tkinter import messagebox
from detail_window import detailWindow
import cell

class MainWindow:

    def __init__(self, root, json_data):
        self.root = root
        self.root.title("MainWindow")    # Título de la ventana  

        cells = [] # Inicializa una lista de celdas vacías

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")

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
                "<Button-1>",lambda event, cell=cell: detailWindow(cell)
            )
            
        #creamos la barra de menus 
        barra_menus = tk.Menu()
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(
            #indicamos la etiqueta que sale en la ventana principal
                label="Acerca de ",
                #inddicamos que accion realiza al clicar en ayuda
                command=self.onButtonClicked
                )
        #añadimos a la barra menus
        barra_menus.add_cascade(menu=menu_archivo, label="Ayuda")
        root.config(menu=barra_menus)
        #cerramos el bucle
        root.mainloop()


    # Función que ejecuta detailWindow
    def onButtonClicked(self):
        messagebox.showinfo("Acerca del desarrollador","ama Pokemon")

    