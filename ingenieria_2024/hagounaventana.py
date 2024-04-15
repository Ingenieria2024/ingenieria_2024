import tkinter as tk
from tkinter import ttk

def boton_uno(): 
    accion.configure(text="Conocenos")

def boton_dos():
    accion.configure(text="Colaborá")

def boton_tres():
    accion.configure(text="Contacto")

# Inicializar ventana, título y tamaño
ventana = tk.Tk()
ventana.title("CONSTRUYENDO_SONRISAS_ONG")

# Parte 1
frame1 = ttk.Frame(ventana)
frame1.pack(fill='both', expand=True)

etiqueta = ttk.Label(frame1, text="CONSTRUYENDO SONRISAS")
etiqueta.pack(side='left', padx=5, pady=5)

botones_frame1 = ttk.Frame(frame1)
botones_frame1.pack(side='right', fill='both', expand=True)

ttk.Button(botones_frame1, text="Conocenos", command=boton_uno).pack(side='left', padx=5, pady=5)
ttk.Button(botones_frame1, text="Colaborá", command=boton_dos).pack(side='left', padx=5, pady=5)
ttk.Button(botones_frame1, text="Contacto", command=boton_tres).pack(side='left', padx=5, pady=5)

# Parte 2
frame2 = ttk.Frame(ventana)
frame2.pack(fill='both', expand=True)

ttk.Label(frame2, text="Sé parte de nuestra misión").pack(padx=10, pady=10)
ttk.Label(frame2, text="Esta es tu oportunidad, colaborá con alguna de nuestras campañas y/o la difusión de nuestra fundación.").pack(padx=10, pady=10)

# Parte 3
frame3 = ttk.Frame(ventana)
frame3.pack(fill='both', expand=True)

ttk.Label(frame3, text="Colaborá con Construyendo Sonrisas").pack(padx=10, pady=10)
ttk.Button(frame3, text="SUMATE").pack(padx=10, pady=10)

# Parte 4
frame4 = ttk.Frame(ventana)
frame4.pack(fill='both', expand=True)

ttk.Label(frame4, text="Construyendosonrisas@gmail.com").grid(row=0, column=0, padx=5, pady=5, sticky="w")
ttk.Label(frame4, text="Suscribite").grid(row=0, column=1, padx=5, pady=5, sticky="w")
texto = tk.Text(frame4, height=5, width=30)
texto.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
ttk.Label(frame4, text="Números de emergencia").grid(row=0, column=2, padx=5, pady=5, sticky="w")
opciones = ttk.Combobox(frame4, values=["102", "911"])
opciones.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

# Activar ventana
ventana.mainloop()