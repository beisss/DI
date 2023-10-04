from tkinter import Tk, ttk
import tkinter as tk

class MainWindow:
    def onButtonClicked(self, cell):
        pass
    
    def __init__(self, root):
        self.root = root

        # Marco
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        # Etiqueta
        self.label = ttk.Label(self.frame, text="Este mensaje es poco importante")
        self.label.pack()

        # Botón
        self.button = ttk.Button(
            self.frame, text="Realizar la acción", command=self.onButtonClicked
        )
        self.button.pack()