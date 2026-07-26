from rich.console import Console
from rich.table import Table     
from rich import  print
import os
import json

console = Console()
#CRUD para crear personaje de videojuego

if __name__ == "__main__":
   personaje = {} # id : nombre, colordepelo, estatura, arma
   if not os.path.exists("personaje.json"):
      with open("personaje.json", "w") as f:
         json.dump(personaje, f)
   else:
      with open("personaje.json", "r") as f:
         personaje = json.load(f)  

   

   while True:
        os.system("cls") # En windows es cls
        
        
   
        #os.system("clear") #En mac

        opcion = input("\n1: Crear \n2: Leer \n3: Actualizar \n4: Eliminar \n5: Salir \nIngrese una opcion:")
       
        
        if opcion == "1":
           id = int(input("Ingrese el id: "))
           nombre = input("Ingrese el nombre: ")
           color_de_pelo = input("Ingrese el color de pelo(en inglés): ")
           estatura = (input("Ingrese la estatura: "))
           arma = input("Ingrese el arma: ")

           if not (id and nombre and color_de_pelo and estatura and arma):
              input("No se agregan los datos correctamente")
              continue

           personaje[id] = {
              "nombre":nombre,
              "colordepelo": color_de_pelo,
              "estatura":estatura,
              "arma":arma
            }
           input("personaje agregado correctamente")
        elif opcion == "2":
           if personaje:
              #Agrego rich
              tabla = Table(title= "Personajes")
              tabla.add_column("ID", justify="center")
              tabla.add_column("[bold yellow]Nombre[/]", justify="center")#yellow thing
              tabla.add_column("[red]C[/][blue]o[/][cyan]l[/][green]o[/][yellow]r[/] [magenta]d[/][green]e[/] [magenta]P[/][green]e[/][red]l[/]o", justify="center")#rainbow thing
              tabla.add_column("[bold blue]Estatura[/]", justify="center")#blue thing
              tabla.add_column("[bold red]Arma[/]", justify="center")#red thing

              for key, value, in personaje.items():         #este toque de color fué lo que más me costo, y era súper simple.xd
                 tabla.add_row(str(key), value['nombre'], f"[{value['colordepelo']}]{value['colordepelo']}[/]", value['estatura'],value['arma'])
                 continue
              console.print(tabla)  
              input ("Presione enter para continuar")
               
           else:
              print("No tienes personajes para mostrar")

        elif opcion == "3":
           if not personaje:
              print("No hay personaje para modificar")
              continue
           tabla = Table(title= "Personajes")
           tabla.add_column("ID", justify="center")
           tabla.add_column("[bold yellow]Nombre[/]", justify="center")
           tabla.add_column("Color de Pelo", justify="center")
           tabla.add_column("[bold blue]Estatura[/]", justify="center")
           tabla.add_column("[bold red]Arma[/]", justify="center")
           for key, value in personaje.items():
                 tabla.add_row(str(key), value['nombre'], f"[{value['colordepelo']}]{value['colordepelo']}[/]", value['estatura'],value['arma'])
                 continue
           console.print(tabla)  
           
           personaje[id] = input("Ingrese el id: ")
           if not id in personaje.keys():
              input("No existe el personaje con ese id")
              continue

           nombre = input("Ingrese el nombre: ")
           color_de_pelo = input("Ingrese el color de pelo(en inglés): ")
           estatura = (input("Ingrese la estatura: "))
           arma = input("Ingrese el arma: ")

           print("Personaje actualizado correctamente")
           if not (nombre and color_de_pelo and estatura and arma):
              input("No se agregan los datos correctamente")
              continue
           
           personaje[id] = {
              "nombre":nombre,
              "colordepelo": color_de_pelo,
              "estatura":estatura,
              "arma":arma
            }
           
        elif opcion == "4":

           if not personaje:
              print("No hay personaje para eliminar")
              continue   
           tabla = Table(title= "Personajes")
           tabla.add_column("ID", justify="center")
           tabla.add_column("[bold yellow]Nombre[/]", justify="center")
           tabla.add_column("Color de Pelo", justify="center")
           tabla.add_column("[bold blue]Estatura[/]", justify="center")
           tabla.add_column("[bold red]Arma[/]", justify="center")
           for key, value in personaje.items():
                 tabla.add_row(str(key), value['nombre'], f"[{value['colordepelo']}]{value['colordepelo']}[/]", value['estatura'],value['arma'])
                 continue
           console.print(tabla)  
           personaje[id] = input("Ingrese el id: ")
           if not id in personaje.keys():
              print("No existe el personaje con ese id")
              continue

           del personaje[id]
           input("personaje eliminado correctamente")
        elif opcion == "5":
           print("Gracias por usar el progama y tal")
           break
        else:
           input("Ingrese una opción valida \nPresione enter para continuar" )

        with open("personaje.json", "w") as f:
            json.dump(personaje, f)        