#Tarea3.2: Realizar un programa que diga si un número es primo  .

#Pido el número al usuario
numero_primo = int(input("Ingrese un número: "))
es_primo = True


if numero_primo < 2:
    es_primo = False
else:
    for i in range(2, int(numero_primo ** 0.5) + 1):
        if numero_primo % i == 0:
            es_primo = False
            break

if es_primo:
    print("El número es primo.")
else:
    print("El número no es primo.")