# Tkinter
import tkinter as tk
from tkinter import ttk

# Funciones
def biblioteca ():
    print ("Usted ha ingresado a la biblioteca digital de la UNPAZ.")
    
def geolocalizacion ():
    print ("Usted ha ingresado a la geolocalización de las distintas sedes de la UNPAZ.")

def plan_de_estudio ():
    print ("Usted ha ingresado al plan de estudio de la carrera de TUIAS.")

# Root/Ventana
root = tk.Tk ()
root.geometry ("400x250")
root.title ("Universidad Nacional de José Clemente Paz - APP")

# Etiqueta
etiqueta = ttk.Label (root, text = "Bienvenidos/as al portal de la Universidad Nacional de José C. Paz", padding = (27, 27), background = "light blue")
etiqueta.pack ()

# Botones
boton_biblioteca = ttk.Button (root, text = "Biblioteca", padding = (29, 10), command = biblioteca)
boton_biblioteca.pack ()

boton_geolocalizacion = ttk.Button (root, text = "Geolocalización", padding = (20, 10), command = geolocalizacion)
boton_geolocalizacion.pack ()

boton_plan_de_estudio = ttk.Button (root,text = "Plan de estudio", padding = (20, 10), command = plan_de_estudio)
boton_plan_de_estudio.pack ()

# Loop eterno
root.mainloop ()