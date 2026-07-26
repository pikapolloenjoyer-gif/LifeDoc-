#Tarea5.4:Crear un programa que guarde nombres, apellidos, y edad luego lo muestre enumerados.

#Creo la lista para guardar los datos
datos = []

#Pido los datos al usuario con un bucle. se detiene cuando el usuario ingresa "fin"

while True:
    nombre = input("Ingrese su nombre ('fin' para terminar): ")
    if nombre == "fin":
        break

    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")

    datos.append((nombre, apellido, edad)) 

# Muestro los datos enumerados, con un ciclo "for"
for i, (nombre, apellido, edad) in enumerate(datos, start=1):
    print(f"{i}. {nombre} {apellido}, Edad: {edad}")