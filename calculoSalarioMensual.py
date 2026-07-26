#Examen calcular todo lo relacionado al salario mensual, incluyendo impuestos, pensión y seguro.
#Agrego rich para color y más organización
from rich.console import Console
from rich.table import Table

#<>
console = Console()

#Pido el salario al usuario
salario = int(input("Ingrese su salario mensual: "))

table = Table(title = "ISR, Pensión y seguro")
table.add_column("[red]ISR[/]",justify= "center")
table.add_column("[blue]Pensión[/]",justify= "center")
table.add_column("[green]Seguro[/]",justify= "center")

#Variables de pensión y seguro la pensión y seguro en RD cuestan un 0.287% y 0.304% 
pension = 0.0287
seguro = 0.0304

#Calculo pensión y seguro
pension *= salario
seguro *= salario    

#Uso varios if para condicionar las tablas de impuestos y calcularlos(sistema dominicano ISR)
salario *= 12

if salario <= 416220:
    print("No debes pagar impuestos")
elif salario > 416220 and salario <= 624329:
    
    #se le resta el límite inferior del tramo
    salario -= 416220
    #Aquí es 15%
    salario *= 0.15
    salario /= 12
    salario2 = int([salario])
    #Agrego filas
    table.add_row(f"{salario2} Pesos mensuales", f"{pension} Pesos mensuales",f"{seguro} Pesos mensuales"  )
elif salario  >  624329 and  salario <= 867123:
     salario -= 624329
     #Aquí es 20%
     salario *= 0.20
     #Se suma el impuesto fijo del tramo anterios(31,216)
     salario += 31216
     salario /= 12
     table.add_row(f"{salario} Pesos mensuales", f"{pension} Pesos mensuales",f"{seguro} Pesos mensuales"  )
elif salario  > 867123:
     salario -= 867123
     #Aquí es 25%
     salario *= 0.25
     #Se suma el fijo de los tramos anteriores(79,776)
     salario += 79776
     salario /= 12
     table.add_row(f"{salario} Pesos mensuales", f"{pension} Pesos mensuales",f"{seguro} Pesos mensuales"  )


#Muestro el resultado
console.print(table)


