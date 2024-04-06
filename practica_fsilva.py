#antes que nada importo tkinter para que ande la ventana
import tkinter as tk
from tkinter import ttk 
#aca agrego unos saludos para mas adelante
def saludines():
    print ("Alo alo amigos")
def dijeno():
    etiqueta2.pack()    
#aca creo la ventana
root = tk.Tk()
#aplico propiedades
root.geometry("600x400")
root.title("Recien hoy me puse a practicar")
#Aqui agrego etiquetas
etiqueta = ttk.Label (root, text="Hola querido como andas", padding=(50, 50))
etiqueta.pack()
#otra etiqueta
etiqueta2 =ttk.Label(root,text=" Te dije que no toques!! ", padding=(50, 50))
#aca agrego algunos botones
boton_escribir = ttk.Button(root, text=" Si haces click te saludo ", command=saludines)
boton_escribir.pack()

boton_prohibido= ttk.Button(root, text=" No hagas click xfa ", command=dijeno)
boton_prohibido.pack()

boton_salir= ttk.Button(root, text=" Botón de autodestrucción", command=root.destroy)
boton_salir.pack()

#aplico loop
root.mainloop()
