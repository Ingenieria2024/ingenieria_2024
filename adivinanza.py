import random

def adivinanza():
  adivinanza = "qué hace un limon en el agua?"
  respuesta_correcta = "limonada"

  print ("adivina esta adivinanza:")
  print (adivinanza)

  respuesta = input("responde:").lower()

  if respuesta == respuesta_correcta:
    print("¡Correcto! Adivinaste!")
  else:
    print("incorrecto. La respuesta correcta era:", respuesta_correcta)

if __name__== "__main__":
  adivinanza() 