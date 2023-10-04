from tkinter import ttk
import tkinter as tk    # Define tk como alias de tkinter

def show_no_window():
    no_root=tk.Tk()
    no_root.geometry("250x30")          # Establece el tamaño de la ventana

    frame = ttk.Frame(no_root)          # Crea un marco dentro de la ventana, para organizar los elementos
    frame.pack()                        # Empaqueta el marco, lo hace visible en la ventana

    label = ttk.Label(frame, text="No sabes lo que te pierdes :(")  # Crea una etiqueta de texto
    label.pack()                                                    # Empaqueta la etiqueta, la hace visible

    no_root.mainloop()              # Inicia el bucle para que la ventana sea interactiva y se mantenga abierta