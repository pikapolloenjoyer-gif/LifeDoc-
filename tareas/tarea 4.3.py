#Tarea4.3:Realizar un programa que cuente las letras, vocales, espacios y palabras de una oración.

#pido la oración
oracion = input("Ingrese una oración: ")

#cuentos las letras, vocales, espacios y palabras
                                #Condición para contar las letras 
letras = sum(1 for c in oracion  if c.isalpha())
                                         #Condición para contar las vocales
vocales = sum(1 for c in oracion.lower() if c in "aeiouáéíóúü")
espacios = oracion.count(" ")
palabras = len(oracion.split())

#Muestro el resultado
print("Número de letras:", letras)
print("Número de vocales:", vocales)
print("Número de espacios:", espacios)
print("Número de palabras:", palabras)  
