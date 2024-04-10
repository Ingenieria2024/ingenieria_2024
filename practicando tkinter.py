import tkinter as tk
from tkinter import ttk

def saludar():
    etiqueta.config(text="Hola!!!")

   #print("Hola a todos y todas")

root = tk.Tk()
root.geometry("450x150")
root.title("Practicando tkinter")
root.configure(bg="#ffa9ba")

etiqueta = ttk.Label(root, text="Hoy empezamos tkinter", padding=(20, 10))
etiqueta.pack()

boton_escribir = ttk.Button(root, text="Escribir", command=saludar)
boton_escribir.pack()

boton_cancelar = ttk.Button(root, text="Cancelar", command=root.destroy)
boton_cancelar.pack()
root.mainloop()
