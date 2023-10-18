import threading
import tkinter as tk
import requests
from window import MainWindow

class LoadingWindow:
    def __init__(self,root):
        self.root = root                    # Hace referencia a la ventana principal de la aplicación
        self.finished = False
        self.json_data = []
        self.root.title("Cargando...")      # Configura el título de la ventana principal
        self.root.geometry("170x120")       # Establece el tamaño de la ventana principal
        self.root.resizable(False,False)    # Desactiva la capacidad de cambiar el tamaño de la ventana

        # Crea una etiqueta con los datos señalados
        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg")  # Obtiene el bgcolor de la etiqueta 'label'

        # Crea un elemento Canvas en la ventana principal 'root'
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0   # Instancia el progreso en 0
        self.draw_progress_circle(self.progress)    # Dibuja el progreso con el valor de progress
        self.update_progress_circle()   # Actualiza el progreso

        # Crea un hilo y lo ejecuta
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()

    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")      # Borra todos los elementos con la etiqueta 'progress'
        angle = int(360 * (progress/100))   # Calcula un ángulo en grados

        # Crea un arco gráfico que representa el progreso
        self.canvas.create_arc(10, 10, 35, 35,
                               start=0, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC)

    # Función que se encarga de actualizar el progreso del círculo
    def update_progress_circle(self):
        if self.progress < 100:
            self.progress += 10
        else:
            self.progress = 0
        
        self.draw_progress_circle(self.progress)            # Llama a la función draw_progress_circle y le pasa el parámetro de progress
        self.root.after(100, self.update_progress_circle)   # Establece un temporizador que ejecutará la función update_progress_circle después de 100 milisegundos

    def fetch_json_data(self):
        # Realiza una solicitud HTTP y guarda el JSON en response
        response = requests.get("https://github.com/beisss/DI/blob/main/resources/catalog.json")
        # Verifica que la solicitud fue exitosa
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished=True
    
    # Verifica si el hilo en segundo plano ha terminado
    def check_thread(self):
        if self.finished:       
            self.root.destroy()
            launch_main_window(self.json_data)
        else:                   
            self.root.after(100, self.check_thread)

# Procede a ejecutar MainWindow
def launch_main_window(json_data):
    root = tk.Tk()
    app = MainWindow(root,json_data)
    root.mainloop()