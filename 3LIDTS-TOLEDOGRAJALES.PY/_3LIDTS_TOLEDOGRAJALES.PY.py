import tkinter as tk
from tkinter import messagebox
def calcular_temps():
    if(tbCelsius.get() or tbFahrenheit.get() or tbKelvin.get()):
        try:
            print("Calculando temperatura")
            if(tbCelsius.get()):
                print("Calculando desde Celsius")
                ce = float(tbCelsius.get())
                fa = (ce * 9/5) + 32
                tbFahrenheit.delete(0,tk.END)
                tbFahrenheit.insert(0, str(round(fa,2)))
                ke = ce + 273.15
                tbKelvin.delete(0,tk.END)
                tbKelvin.insert(0, str(round(ke,2)))
            elif(tbFahrenheit.get()):
                print("Calculando desde Fahrenheit")
                fa = float(tbFahrenheit.get())
                ce = (fa - 32) * 5/9
                tbCelsius.delete(0,tk.END)
                tbCelsius.insert(0, str(round(ce,2)))
                ke = ce + 273.15
                tbKelvin.delete(0,tk.END)
                tbKelvin.insert(0, str(round(ke,2)))
            elif(tbKelvin.get()):
                print("Calculando desde Kelvin")
                ke = float(tbKelvin.get())
                ce = ke - 273.15
                tbCelsius.delete(0,tk.END)
                tbCelsius.insert(0, str(round(ce,2)))
                fa = (ce * 9/5) + 32
                tbFahrenheit.delete(0,tk.END)
                tbFahrenheit.insert(0, str(round(fa,2)))
        except ValueError:
            messagebox.showerror(title="Error", message="Tipo de dato ingresado incompatible")
    else:
        messagebox.showwarning(title="advertencia", message="Los contenedores estan vacios")
def limpiar():
    #print("Limpiando")
    tbCelsius.delete(0,tk.END)
    tbFahrenheit.delete(0,tk.END)
    tbKelvin.delete(0,tk.END)
    messagebox.showinfo(title="Limpiando", message="Se estan borrando los valores")
#Crear ventana principal
ventana = tk.Tk()
ventana.title("Conversor basico de Temperaturas")
#Etiquetas
#tk.Label(ventana, text ="Celsius:").grid(row=0, column=0, padx=10, pady=10)
lbCelsius = tk.Label(ventana, text ="Celsius:")
lbCelsius.grid(row=0, column=0, padx=10, pady=10)
#tk.Lable(ventana, text="Fahrenheit:").grid(row=1, column=0, padx=10, pady=10))
lbFahrenheit = tk.Label(ventana, text="Fahrenheit:")
lbFahrenheit.grid(row=1, column=0, padx=10, pady=10)
#tk.Label(ventana, text="Kelvin:").grid(row=2, column=0, padx=10, pady=10)
lbKelvin = tk.Label(ventana, text="Kelvin:")
lbKelvin.grid(row=2, column=0, padx=10, pady=10)
#Entradas
tbCelsius = tk.Entry(ventana)
tbFahrenheit = tk.Entry(ventana)
tbKelvin = tk.Entry(ventana)
tbCelsius.grid(row=0, column=1, padx=10, pady=10)
tbFahrenheit.grid(row=1, column=1, padx=10, pady=10)
tbKelvin.grid(row=2, column=1, padx=10, pady=10)
#Botones
btnCalcular = tk.Button(ventana, text="Calcular",command=calcular_temps)
btnLimpiar = tk.Button(ventana, text="Limpiar",command=limpiar)
btnCalcular.grid(row=3, column=0, columnspan=2, pady=10)
btnLimpiar.grid(row=4, column=0, padx=10, pady=10)
btnSalir = tk.Button(ventana, text="Salir", command=ventana.quit)
btnSalir.grid(row=4, column=1, padx=10, pady=10)
#Ejecucion de la ventana
ventana.mainloop()