#Tarea5.1:  Crear un programa que guarde nombres, pero si son muy cortos no se guarden.

#Creo la lista para guardar los nombres
nombres = []

#Pido los nombres al usuario, el programa se detiene cuando el usuario ingresa "fin"
while True:
    nombre = input("Ingrese un nombre ('fin' para terminar): ")

    if nombre.lower() == "fin":
        break

    if len(nombre) < 3:
        print("El nombre es demasiado corto, no se guardará.")
    else:
        nombres.append(nombre)

print("Nombres guardados: ", nombres)