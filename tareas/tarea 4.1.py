
#Tarea4.1:Realizar un programa que calcule la tabla de multiplicación del numero que deseas.

#Pido el número
numero = int(input("Ingrese el número para mostrar su tabla de multiplicar: "))

#Aplico condición 
if numero == 0:
   print("Inicie el programa otra vez e ingrese un número valido!")

resultado = 0
#Pongo un for que aunque los ciclos no sea el tema ahora, de otra forma con los if no se podra mostrar el numero que yo desee (o bueno sí pero seria muy dificil y largo xd)
for i in range(1,13):
    resultado = numero * i
     
    #Muestro el resultado
    print(f"{numero} x {i} = {resultado}")
    #Reinicio el resultado porque si no CACA
    resultado = 0
