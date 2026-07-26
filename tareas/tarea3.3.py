#tarea3.3:Realizar un programa donde se valide si que cosas contiene un texto(tiene texto, numeros o signos).

#Pido el texto al usuario
texto = input("Ingrese un texto: ")

#Uso condicionales para determinar si el texto tiene letras, números o signos
tiene_letras = any(c.isalpha() for c in texto)
tiene_numeros = any(c.isdigit() for c in texto)
tiene_signos = any(not c.isalnum() for c in texto)

if tiene_letras:
    print("El texto contiene letras.")
if tiene_numeros:
    print("El texto contiene números.")
if tiene_signos:
    print("El texto contiene signos.")