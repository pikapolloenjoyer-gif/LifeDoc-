from datetime import datetime

dia = input("Ingresa la fecha: ")
fecha = "15/8/2026"

dias1 = datetime.strptime(dia, "%d/%m/%Y")


print(dias1.strftime("%A,%d"))