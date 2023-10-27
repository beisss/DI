from tkinter import Tk # Importamos Tkinter
from window import MainWindow
from loading_window import LoadingWindow

# Cuestiona si el script es un programa independiente
# o se está importando como módulo desde otro script
if __name__ == "__main__":
    # Crea una ventana
    root = Tk()
    # Ejecuta LoadingWindow
    app = LoadingWindow(root)
    root.mainloop()