import tkinter as tk
from tkinter import ttk

def detailWindow(cell):

    # Crea una nueva ventana independiente de la principal
    root = tk.Toplevel()

    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry(f"+{int(x)}+{int(y)}")

    # Crea una etiqueta con la imagen, una con el título y otra con la descripción
    label1 = ttk.Label(root, image=cell.Image_tk)
    label2 = ttk.Label(root, text=cell.title)
    label3 = ttk.Label(root, text=cell.desc)

    # Empaqueta las etiquetas
    label1.pack()
    label2.pack()
    label3.pack()

    root.mainloop()