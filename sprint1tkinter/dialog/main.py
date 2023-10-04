from tkinter import Tk 
from window import MainWindow   # Importación clase MainWindow (window.py)
if __name__ == "__main__":      # Verifica si está siendo ejecutado como programa principal
    root = Tk()                 # Instancia ventana principal
    app = MainWindow(root)      # Interfaz gráfica
    root.mainloop()             # Mantiene la ventana abierta, esperando eventos del usuario