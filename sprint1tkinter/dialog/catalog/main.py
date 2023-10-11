from tkinter import Tk # Importamos Tkinter
from window import MainWindow

# Cuestiona si el script es un programa independiente
# o se está importando como módulo desde otro script
if __name__ == "__main__":
    # Crea una ventana
    root = Tk()
    # Ejecuta MainWindow
    app = MainWindow(root)
    root.mainloop()