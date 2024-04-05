#MENU PRINCIPAL   
while True:
    print("=================================")
    print("menu")
    print("=================================")
    print("\t[1]Insertar producto")
    print("\t[2]Lista de Productos")
    print("\t[3]Actializar Productos")
    print("\t[4]Eliminar producto")
    print("\t[5]Salir")
    print("=============================")
    opcion=int(input("seleccionar una opcion: "))
    print()
    if(opcion==1):
        agregar()
    elif(opcion==2):
         lista()
    elif (opcion==3):
          actualizar()
    elif (opcion==4):
          eliminar()
    elif (opcion==5):
              break
    else:
        print("opcion invalida")
===============
print ("hola")
print ("prueba")
