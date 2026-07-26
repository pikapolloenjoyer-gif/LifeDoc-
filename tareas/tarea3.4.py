#Tarea3.4:  Realizar un programa que realice una entrevista a una persona y de acuerdo a sus pregunta se puedas dar nacionalidad dominicana.

#Hago las preguntas al usuario
nombre = input("¿Cuál es tu nombre? ")
pais = input("¿De qué país eres? ")
if pais.lower() == "república dominicana" or pais.lower() == "dominicana":
    print("¡Eres dominicano!")
    exit()  
años = int(input("¿Cuántos años llevas viviendo en República Dominicana? "))
pagas = input("¿Pagas impuestos en República Dominicana? (sí/no) ")

#Valido las respuestas para determinar si la persona es dominicana o no
if años >= 5 and pagas.lower() == "sí":
    print("Toma tu nacionalidad dominicana xd.")
else:
    print("No cumples con los requisitos para obtener la nacionalidad dominicana.")