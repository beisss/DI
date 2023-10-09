from tkinter import Tk # Importamos Tkinter
from window import MainWindow

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()