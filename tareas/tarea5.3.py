#Tarea5.3:Crear un programa que te permita agrega numero a lista y al final que diga la suma de todos los números.

#Creo la lista para guardar los números
numeros = []

#Pido los números al usuario, el programa se detiene cuando el usuario ingresa "fin"
while True:
    numero = input("Ingrese un número ('fin' para terminar): ")
     
     #Calculo la suma de los números en la lista
    suma = sum(numeros)
    if numero == "fin":
        break

    try:
        numero = float(numero)  # Intento convertir el input a un número
        numeros.append(numero)
    except ValueError:
        print("Entrada no válida, por favor ingrese un número o 'fin' para terminar.")

#Muestro resultado
print(f"La suma de los números ingresados es: {suma}")