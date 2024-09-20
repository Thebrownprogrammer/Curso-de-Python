import re
import tkinter as tk
from tkinter import messagebox

# Funciones que implementan las expresiones regulares
def buscar_numero():
    texto = entrada_texto.get()
    resultado = re.search(r'\d+', texto)
    if resultado:
        messagebox.showinfo("Resultado", f"Primer número encontrado: {resultado.group()}")
    else:
        messagebox.showinfo("Resultado", "No se encontraron números")

def buscar_palabras_mayusculas():
    texto = entrada_texto.get()
    resultado = re.findall(r'\b[A-Z][a-z]*\b', texto)
    if resultado:
        messagebox.showinfo("Resultado", f"Palabras que empiezan con mayúscula: {resultado}")
    else:
        messagebox.showinfo("Resultado", "No se encontraron palabras que empiecen con mayúscula")

def dividir_por_numeros():
    texto = entrada_texto.get()
    resultado = re.split(r'\d+', texto)
    messagebox.showinfo("Resultado", f"Texto dividido por números: {resultado}")

def reemplazar_anios():
    texto = entrada_texto.get()
    resultado = re.sub(r'\b\d{4}\b', '****', texto)
    messagebox.showinfo("Resultado", f"Texto con los años reemplazados: {resultado}")

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Expresiones Regulares con Interfaz")
ventana.geometry("400x300")

# Etiqueta y entrada de texto
etiqueta_texto = tk.Label(ventana, text="Ingresa el texto:")
etiqueta_texto.pack(pady=10)

entrada_texto = tk.Entry(ventana, width=50)
entrada_texto.pack(pady=10)

# Botón para buscar el primer número en el texto
boton_buscar_numero = tk.Button(ventana, text="Buscar número", command=buscar_numero)
boton_buscar_numero.pack(pady=5)

# Botón para buscar palabras que empiecen con mayúscula
boton_palabras_mayusculas = tk.Button(ventana, text="Buscar palabras con mayúscula", command=buscar_palabras_mayusculas)
boton_palabras_mayusculas.pack(pady=5)

# Botón para dividir el texto por números
boton_dividir_numeros = tk.Button(ventana, text="Dividir por números", command=dividir_por_numeros)
boton_dividir_numeros.pack(pady=5)

# Botón para reemplazar años por ****
boton_reemplazar_anios = tk.Button(ventana, text="Reemplazar años", command=reemplazar_anios)
boton_reemplazar_anios.pack(pady=5)

# Iniciar la interfaz gráfica
ventana.mainloop()
