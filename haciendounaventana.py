import tkinter as tkinter
from tkinter import ttk 

def saludar():
    print ("Hola a todxs")
root = tk.Tk ()
root.geometry("450x200")
root.title("practicando")
etiqueta = ttk.Label(root,text "Hoy practicamos tkinter", padding (50,30))
etiqueta.pack ()
