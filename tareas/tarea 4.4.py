#tarea4.4:Realizar un programa que diga si adivinaste la palabra secreta.


#Palabra secreta
palabra_secreta = "targaryen"


#Bucle para permitir al usuario adivinar la palabra secreta
while True:
 #Pista
 print("Pista: Es una familia de la serie Game of Thrones")
 #Solicito al usuario que adivine la palabra
 adivinanza = input("Adivina la palabra secreta: ")

 #Condición para verificar si la adivinanza es correcta
 if adivinanza == palabra_secreta:
    print("¡Felicidades! Has adivinado la palabra secreta.")
    break
 else:
    print("Lo siento, esa no es la palabra secreta.")