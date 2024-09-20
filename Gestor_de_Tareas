import tkinter as tk                    # Librerias para interfaz grafica
from tkinter import ttk, messagebox     # Para cuadros emergentes
from datetime import datetime           # Para el manejo de fechas
import re                               # Modulo para trabajar expresiones regulares (validación de fechas)

"""  Clase Tarea
Esta clase define una tarea con: 
- Título 
- Descripción 
- Fecha límite 
- Estado (pendiente por defecto) 
- Prioridad (0 por defecto).

====FUNCIONES UTILIZADAS EN LA CLASE====

self: Se refiere a la propia instancia de la clase que está siendo creada o manipulada.
    Ejemplo:
    Linea 24 "self.titulo = titulo"
    Esta línea guarda el valor que se pasa como titulo en el parámetro al atributo self.titulo de la instancia.

datetime: 
    Ejemplo:
    Linea # "self.fecha_limite = datetime.strptime(fecha_limite, "%Y-%m-%d")"
    fecha_limite: Convierte la fecha de cadena a un objeto datetime.

Funcion __str__(self)
    Se utiliza para definir cómo se representa una instancia de una clase cuando se convierte en una cadena de texto.
"""

class Tarea:
    def __init__(self, titulo, descripcion, fecha_limite):      # Constructor de la clase
        self.titulo = titulo                                    # Variable de tipo string "Capitulo 3"
        self.descripcion = descripcion
        self.fecha_limite = datetime.strptime(fecha_limite, "%Y-%m-%d")    
        self.estado = 'pendiente'
        self.prioridad = 0                                      # Variable de tipo entero "Capitulo 2"
    
    def marcar_completada(self):
        self.estado = 'completada'
    
    def __str__(self):
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}\nFecha Límite: {self.fecha_limite.strftime('%Y-%m-%d')}\nEstado: {self.estado}\nPrioridad: {self.prioridad}\n"

class ListaDeTareas:
    def __init__(self):
        self.tareas = []        # Lista vacía que almacenará objetos Tarea
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)       # Añade una tarea a la lista
    
    def eliminar_tarea(self, titulo):
        self.tareas = [tarea for tarea in self.tareas if tarea.titulo != titulo]
        """eliminar_tarea(self,titulo)

        Recibe como argumento un titulo 
        self.tareas = [tarea for tarea in self.tareas if tarea.titulo != titulo] es una lista 
        por comprension.
        Crea una nueva lista que contiene solo las tareas cuyo título no coincide con el título 
        que se pasa como argumento.

        """
    
    def marcar_completada(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.marcar_completada()
                break
    
    def mostrar_tareas(self):
        return "\n".join(str(tarea) for tarea in self.tareas) if self.tareas else "No hay tareas en la lista."
    
    def contar_tareas_completadas(self):
        completadas = sum(1 for tarea in self.tareas if tarea.estado == 'completada')
        return completadas

    def ordenar_tareas_por_fecha(self):
        self.tareas.sort(key=lambda tarea: tarea.fecha_limite)
        """Funcion sort()
        La función sort() es un método que ordena una lista en su lugar, es decir, 
        modifica la lista existente en lugar de devolver una nueva lista ordenada.
        """

class InterfazTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("500x450")
        self.lista_de_tareas = ListaDeTareas()

        # Configurar tema
        self.estilo = ttk.Style()
        self.estilo.theme_use('clam')  # Puedes cambiar el tema a 'alt', 'default', 'classic'
        self.estilo.configure("TButton", foreground="white", background="#4CAF50", padding=6)
        self.estilo.configure("TLabel", foreground="#333", background="#f0f0f0")
        
        # Crear widgets
        self.titulo_label = ttk.Label(root, text="Título de la Tarea:")
        self.titulo_entry = ttk.Entry(root, width=40)
        self.descripcion_label = ttk.Label(root, text="Descripción:")
        self.descripcion_entry = ttk.Entry(root, width=40)
        self.fecha_label = ttk.Label(root, text="Fecha Límite (YYYY-MM-DD):")
        self.fecha_entry = ttk.Entry(root, width=20)
        self.prioridad_label = ttk.Label(root, text="Prioridad (0-7):".upper())
        self.prioridad_entry = ttk.Entry(root, width=5)
        self.agregar_button = ttk.Button(root, text="Agregar Tarea", command=self.agregar_tarea)
        self.tareas_text = tk.Text(root, width=50, height=10, state="disabled", bg="#e0f7fa", fg="#333")
        self.completar_button = ttk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.eliminar_button = ttk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.ordenar_button = ttk.Button(root, text="Ordenar por Fecha", command=self.ordenar_tareas)

        # Barra de menú
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Opciones", menu=self.file_menu)
        self.file_menu.add_command(label="Ayuda", command=self.mostrar_ayuda)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=root.quit)

        # Ubicar widgets en la ventana
        self.titulo_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.titulo_entry.grid(row=0, column=1, padx=5, pady=5)
        self.descripcion_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.descripcion_entry.grid(row=1, column=1, padx=5, pady=5)
        self.fecha_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.fecha_entry.grid(row=2, column=1, padx=5, pady=5)
        self.prioridad_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.prioridad_entry.grid(row=3, column=1, padx=5, pady=5)
        self.agregar_button.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        self.tareas_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        self.completar_button.grid(row=6, column=0, padx=5, pady=5)
        self.eliminar_button.grid(row=6, column=1, padx=5, pady=5, sticky='w')
        self.ordenar_button.grid(row=7, column=1, padx=5, pady=5, sticky='e')

        # Mostrar las tareas iniciales (si las hay)
        self.mostrar_tareas()

    def agregar_tarea(self):
        titulo = self.titulo_entry.get()
        descripcion = self.descripcion_entry.get()
        fecha = self.fecha_entry.get()
        prioridad = self.prioridad_entry.get()

        try:
            if titulo and descripcion and fecha:
                self.validar_fecha(fecha)
                tarea = Tarea(titulo, descripcion, fecha)
                self.lista_de_tareas.agregar_tarea(tarea)
                if prioridad.isdigit() and 0 <= int(prioridad) <= 7:
                    tarea.prioridad = int(prioridad)
                self.mostrar_tareas()
                self.limpiar_campos()
            else:
                messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
        except ValueError as e:
            messagebox.showerror("Error de formato", str(e))

    def marcar_completada(self):
        titulo = self.titulo_entry.get()
        if titulo:
            self.lista_de_tareas.marcar_completada(titulo)
            self.mostrar_tareas()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Título faltante", "Por favor, ingrese el título de la tarea a completar.")

    def eliminar_tarea(self):
        titulo = self.titulo_entry.get()
        if titulo:
            self.lista_de_tareas.eliminar_tarea(titulo)
            self.mostrar_tareas()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Título faltante", "Por favor, ingrese el título de la tarea a eliminar.")

    def mostrar_tareas(self):
        self.tareas_text.config(state="normal")
        self.tareas_text.delete(1.0, tk.END)
        self.tareas_text.insert(tk.END, self.lista_de_tareas.mostrar_tareas())
        self.tareas_text.config(state="disabled")

    def limpiar_campos(self):
        self.titulo_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)
        self.fecha_entry.delete(0, tk.END)
        self.prioridad_entry.delete(0, tk.END)

    def ordenar_tareas(self):
        self.lista_de_tareas.ordenar_tareas_por_fecha()
        self.mostrar_tareas()

    def validar_fecha(self, fecha):
        patron = r"\d{4}-\d{2}-\d{2}"
        if not re.fullmatch(patron, fecha):
            raise ValueError("La fecha debe estar en formato YYYY-MM-DD")

    def mostrar_ayuda(self):
        messagebox.showinfo("Ayuda", "Este es un gestor de tareas. Ingrese el título, descripción y fecha límite de la tarea, y use los botones para agregar, completar o eliminar tareas.")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazTareas(root)
    root.mainloop()
