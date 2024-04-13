import tkinter as tk
from tkinter import ttk

# Ventana
root = tk.Tk()
root.geometry ("500x300")
root.title ("¡Bienvenidos al portal de la UNPAZ!")
root.config (background="light blue")

# 1° frame
frame1 = tk.Frame()
etiqueta_nombre = ttk.Label (frame1, text = "Ingresar su nombre y apellido", padding = (5, 5), font = "arial", background = "light green")
etiqueta_nombre.pack (side = "left", ipadx = 1, ipady = 1)

entrada_nombre = tk.Entry (frame1, bg = "white")
entrada_nombre.pack (side = "left")

frame1.pack()

# 2° frame
frame2 = tk.Frame()
etiqueta_dni = ttk.Label (frame2, text = "Ingresar su DNI", padding = (5, 5), font = "arial", background = "light green")
etiqueta_dni.pack (side = "left")

entrada_dni = tk.Entry (frame2, bg = "white")
entrada_dni.pack (side = "left")

frame2.pack()

# 3° frame
frame3 = tk.Frame()
etiqueta_contraseña = ttk.Label (frame3, text = "Ingresar contraseña", padding = (5, 5), font = "arial", background = "light green")
etiqueta_contraseña.pack()

entrada_contraseña = tk.Entry (frame3, bg = "white")
entrada_contraseña.pack()

frame3.pack()

# Botones
boton_cancelar = ttk.Button (root, text = "Cancelar", padding = (5, 5), command = root.destroy)
boton_cancelar.pack()


# Loop
root.mainloop()