import tkinter as tk
from tkinter import messagebox

def calcular_temps():
    try:
        # Si hay valor en Celsius
        if var_celcius.get() != "":
            ce = float(var_celcius.get())
            fa = (ce * 9/5) + 32
            ke = ce + 273.15
            var_fahrenheit.set(round(fa, 2))
            var_kelvin.set(round(ke, 2))

        # Si hay valor en Fahrenheit
        elif var_fahrenheit.get() != "":
            fa = float(var_fahrenheit.get())
            ce = (fa - 32) * 5/9
            ke = ce + 273.15
            var_celcius.set(round(ce, 2))
            var_kelvin.set(round(ke, 2))

        # Si hay valor en Kelvin
        elif var_kelvin.get() != "":
            ke = float(var_kelvin.get())
            ce = ke - 273.15
            fa = (ce * 9/5) + 32
            var_celcius.set(round(ce, 2))
            var_fahrenheit.set(round(fa, 2))

        else:
            messagebox.showwarning("Advertencia", "Debes ingresar un valor en al menos un campo.")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese solo numeros validos.")

def limpiar():
    var_celcius.set("")
    var_fahrenheit.set("")
    var_kelvin.set("")
    messagebox.showinfo("Limpiando", "Se han borrado los valores.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("350x250")
ventana.config(bg="#f0f0f0")

# Variables de texto
var_celcius = tk.StringVar()
var_fahrenheit = tk.StringVar()
var_kelvin = tk.StringVar()

# Etiquetas
tk.Label(ventana, text="Celsius:", bg="#f0f0f0", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Label(ventana, text="Fahrenheit:", bg="#f0f0f0", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Label(ventana, text="Kelvin:", bg="#f0f0f0", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=10, sticky="e")

# Entradas
tk.Entry(ventana, textvariable=var_celcius).grid(row=0, column=1, padx=10, pady=10)
tk.Entry(ventana, textvariable=var_fahrenheit).grid(row=1, column=1, padx=10, pady=10)
tk.Entry(ventana, textvariable=var_kelvin).grid(row=2, column=1, padx=10, pady=10)

# Botones
tk.Button(ventana, text="Calcular", width=12, bg="#4caf50", fg="white", command=calcular_temps).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(ventana, text="Limpiar", width=12, bg="#f44336", fg="white", command=limpiar).grid(row=4, column=0, padx=10, pady=10)
tk.Button(ventana, text="Salir", width=12, bg="#2196f3", fg="white", command=ventana.quit).grid(row=4, column=1, padx=10, pady=10)

ventana.mainloop()  