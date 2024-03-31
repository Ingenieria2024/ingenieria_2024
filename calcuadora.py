from tkinter import*
ventana= Tk()
ventana.title("calculadora unpaz")
#entrada
e_texto =Entry(ventana, font=("calibri 30"))
e_texto.grid(row = 0, column = 0, columnspan=6, padx=50, pady=5)



number1=int(input("ingresa un numero: "))
number2=int(input("ingresa tro numero: "))

eleccion=0

while eleccion != 6  :
    print(""""
    Indique la operacion a realizar:
    1-suma
    2-resta
    3-multiplicacion
    4-division
    5-cambio de valores
    6-salir
   """ )
    
    eleccion=int(input())
    if eleccion ==1:
        print(" ")
        print("Resultado: ", number1, "+", number2,"=",number1 + number2)



    if eleccion ==2:
        print(" ")
        print("Resultado: ", number1, "-", number2,"=",number1 - number2)


    if eleccion ==3:
        print(" ")
        print("Resultado: ", number1, "*", number2,"=",number1 * number2)


    if eleccion ==4:
        print(" ")
        print("Resultado: ", number1, "/", number2,"=",number1 / number2)   

    if eleccion ==5:
        number1=int(input("ingresa un numero: "))
        number2=int(input("ingresa tro numero: "))


    if eleccion ==6 :
        print("GRACIAS ")




ventana.mainloop()