import tkinter as tk
from tkinter import Label, Entry, Button, Radiobutton, IntVar, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def calcular_poblacion_final(poblacion_inicial, tasa_crecimiento, anios):
    poblacion_final = poblacion_inicial * (tasa_crecimiento ** anios)
    return poblacion_final

def simular_migracion(poblacion_inicial, tasa_crecimiento, anios, prob_comida, prob_depredadores, factor_entorno):
    poblacion = [poblacion_inicial]
    for i in range(1, anios + 1):
        probabilidad_supervivencia = max(0, min(1, prob_comida - prob_depredadores + factor_entorno))
        poblacion_i = poblacion[i - 1] * tasa_crecimiento * probabilidad_supervivencia
        poblacion.append(poblacion_i)
    return poblacion

def graficar_migracion():
    poblacion_inicial = float(entry_poblacion.get())
    tasa_crecimiento = 1 + float(entry_tasa.get()) / 100

    # Verificar si se ha ingresado un valor en entry_anios
    anios_str = entry_anios.get()
    if not anios_str:
        messagebox.showerror("Error", "Ingresa el número de años.")
        return

    # Convertir la cadena a un número entero
    anios = int(anios_str)

    prob_comida = float(entry_prob_comida.get())
    prob_depredadores = float(entry_prob_depredadores.get())

    poblacion = simular_migracion(poblacion_inicial, tasa_crecimiento, anios, prob_comida, prob_depredadores, 0)

    fig, ax = plt.subplots()
    ax.plot(range(anios + 1), poblacion, marker='o', linestyle='-', color='b')
    ax.set_xlabel('Años')
    ax.set_ylabel('Población de Patos')
    ax.set_title('Patrones de Migración de Patos')

    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=7, column=0, columnspan=2, pady=10)

# Crear la interfaz gráfica
app = tk.Tk()
app.title("Calculadora y Gráfico de Migración de Patos")

Label(app, text="Población Inicial de Patos:").grid(row=0, column=0, padx=10, pady=5)
entry_poblacion = Entry(app)
entry_poblacion.grid(row=0, column=1, padx=10, pady=5)

Label(app, text="Tasa de Crecimiento (%):").grid(row=1, column=0, padx=10, pady=5)
entry_tasa = Entry(app)
entry_tasa.grid(row=1, column=1, padx=10, pady=5)

Label(app, text="Número de Años:").grid(row=2, column=0, padx=10, pady=5)
entry_anios = Entry(app)
entry_anios.grid(row=2, column=1, padx=10, pady=5)

Label(app, text="Probabilidad de Encontrar Comida:").grid(row=3, column=0, padx=10, pady=5)
entry_prob_comida = Entry(app)
entry_prob_comida.grid(row=3, column=1, padx=10, pady=5)
entry_prob_comida.insert(0, "0.8")

Label(app, text="Probabilidad de Depredadores:").grid(row=4, column=0, padx=10, pady=5)
entry_prob_depredadores = Entry(app)
entry_prob_depredadores.grid(row=4, column=1, padx=10, pady=5)
entry_prob_depredadores.insert(0, "0.1")

# Botones para interactuar con la aplicación
Button(app, text="Calcular y Graficar Migración", command=graficar_migracion).grid(row=8, column=0, columnspan=2, pady=10)

# Iniciar la aplicación
app.mainloop()
