#Tarea3.1: Realizar un programa que diga si un número es par o impar.

#Pido el número y tal
numero = int(input("Ingrese un número: "))

#Uso una condicional y un resto para determinar si el número es par o impar
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")