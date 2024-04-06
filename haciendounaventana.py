import tkinter as tkinter
from tkinter import ttk 

def saludar():
    print ("Hola a todxs")
root = tk.Tk ()
root.geometry("450x200")
root.title("practicando")
etiqueta = ttk.Label(root,text "Hoy practicamos tkinter", padding (50,30))
etiqueta.pack ()
boton_saludo = ttk.Button(root, text="saludo", command =saludar)
boton_escribir.pack()
boton_contestar = ttk.Button(root, text="contestar", command =contestar)
boton_contestar.pack()
boton_salir = ttk.Button(root, text="salir", command =root.destroy)
boton_salir.pack()

root.mainloop()

