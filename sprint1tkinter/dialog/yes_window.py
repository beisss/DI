from tkinter import ttk
import tkinter as tk    # Define tk como alias de tkinter

def show_yes_window():
    yes_root=tk.Tk()
    yes_root.geometry("250x30")     # Establece el tamaño de la ventana

    frame = ttk.Frame(yes_root)     # Crea un marco dentro de la ventana, para organizar los elementos
    frame.pack()                    # Empaqueta el marco, lo hace visible en la ventana

    etiqueta = ttk.Label(frame, text="A mi también :)") # Crea una etiqueta de texto
    etiqueta.pack()                                     # Empaqueta la etiqueta, la hace visible

    yes_root.mainloop()         # Inicia el bucle para que la ventana sea interactiva y se mantenga abierta