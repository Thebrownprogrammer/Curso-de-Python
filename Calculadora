import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Funciones básicas que ya habíamos definido
def operaciones_basicas(a, b):
    try:
        a, b = float(a), float(b)
        suma = a + b
        resta = a - b
        multiplicacion = a * b
        division = a / b if b != 0 else "Indefinido"
        return f"Suma: {suma}\nResta: {resta}\nMultiplicación: {multiplicacion}\nDivisión: {division}"
    except ValueError:
        return "Por favor, ingrese números válidos."

def exponentes(base, exponente):
    try:
        base, exponente = float(base), float(exponente)
        return base ** exponente
    except ValueError:
        return "Ingrese valores válidos para base y exponente."

def redondeo(numero, decimales):
    try:
        numero, decimales = float(numero), int(decimales)
        return round(numero, decimales)
    except ValueError:
        return "Por favor, ingrese un número válido y decimales como enteros."

# Función para interactuar con el usuario
def mostrar_resultado(funcion, *args):
    resultado = funcion(*args)
    messagebox.showinfo("Resultado", resultado)

# Configuración de la interfaz
def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Calculadora Interactiva Mejorada")
    ventana.geometry("400x500")

    # Cargar imagen de fondo o usar color de fondo
    try:
        imagen_fondo = Image.open("fondo.jpg")  # Cambia a la ruta de tu imagen
        imagen_fondo = imagen_fondo.resize((400, 500), Image.ANTIALIAS)
        imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
        fondo = tk.Label(ventana, image=imagen_fondo)
        fondo.place(relwidth=1, relheight=1)
    except:
        ventana.configure(bg='#ADD8E6')  # Color de fondo si no hay imagen

    # Configuración de estilo de los elementos
    estilo_boton = {'bg': '#FF7F50', 'fg': 'white', 'font': ('Arial', 12), 'relief': 'raised', 'width': 20}
    estilo_entrada = {'bg': 'white', 'font': ('Arial', 12)}
    estilo_titulo = {'bg': '#ADD8E6', 'font': ('Arial', 14, 'bold'), 'fg': '#333333'}

    # Título y espaciado
    tk.Label(ventana, text="Operaciones Básicas", **estilo_titulo).place(x=120, y=20)
    
    tk.Label(ventana, text="Número 1:", **estilo_titulo).place(x=30, y=60)
    tk.Label(ventana, text="Número 2:", **estilo_titulo).place(x=210, y=60)
    
    entrada1 = tk.Entry(ventana, **estilo_entrada)
    entrada2 = tk.Entry(ventana, **estilo_entrada)
    entrada1.place(x=30, y=90, width=150)
    entrada2.place(x=210, y=90, width=150)

    # Botón para operaciones básicas
    tk.Button(ventana, text="Calcular", command=lambda: mostrar_resultado(operaciones_basicas, entrada1.get(), entrada2.get()), **estilo_boton).place(x=90, y=130)

    # Exponentes
    tk.Label(ventana, text="Exponentes", **estilo_titulo).place(x=150, y=180)
    
    tk.Label(ventana, text="Base:", **estilo_titulo).place(x=30, y=210)
    tk.Label(ventana, text="Exponente:", **estilo_titulo).place(x=210, y=210)
    
    base = tk.Entry(ventana, **estilo_entrada)
    exponente = tk.Entry(ventana, **estilo_entrada)
    base.place(x=30, y=240, width=150)
    exponente.place(x=210, y=240, width=150)

    # Botón para exponentes
    tk.Button(ventana, text="Calcular Exponente", command=lambda: mostrar_resultado(exponentes, base.get(), exponente.get()), **estilo_boton).place(x=90, y=280)

    # Redondeo
    tk.Label(ventana, text="Redondeo", **estilo_titulo).place(x=160, y=330)
    
    tk.Label(ventana, text="Número:", **estilo_titulo).place(x=30, y=360)
    tk.Label(ventana, text="Decimales:", **estilo_titulo).place(x=210, y=360)
    
    numero = tk.Entry(ventana, **estilo_entrada)
    decimales = tk.Entry(ventana, **estilo_entrada)
    numero.place(x=30, y=390, width=150)
    decimales.place(x=210, y=390, width=150)

    # Botón para redondeo
    tk.Button(ventana, text="Redondear", command=lambda: mostrar_resultado(redondeo, numero.get(), decimales.get()), **estilo_boton).place(x=90, y=430)

    # Ejecución de la ventana
    ventana.mainloop()

# Ejecutar la interfaz
crear_interfaz()
