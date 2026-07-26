#Pido la info
prestamo = int(input("De cuánto fue su prestamo? "))
interes = float(input("Cual fué su tasa de interés? "))
tiempo = int(input("Cual es el tiempo de su préstamo? "))

#Calculo todo xd
r = prestamo * interes * tiempo 

total = prestamo + r

#Muestro el resultado
print("Su total a pagar es: ", total)