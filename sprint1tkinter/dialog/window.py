from tkinter import ttk
from yes_window import show_yes_window  # Importan los métodos desde sus clases
from no_window import show_no_window

class MainWindow:
    def buttonYes(self):    # Cuando es llamado ejecuta su contenido
        show_yes_window()

    def buttonNo(self):     # Cuando es llamado ejecuta su contenido
        show_no_window()
    
    def __init__(self, root):
        self.root = root        # Almacena la ventana principal para que se pueda usar en esta clase

        # Marco
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        # Etiqueta
        self.label = ttk.Label(self.frame, text="¿Te gustan los nachos?")
        self.label.pack()

        # Botón SI
        self.button1 = ttk.Button(
            self.frame, text="SI", command=self.buttonYes
        )
        self.button1.pack(side="left")

       # Botón NO 
        self.button2 = ttk.Button(
            self.frame, text="NO", command=self.buttonNo
        )
        self.button2.pack(side="right")