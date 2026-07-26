from rich.console import Console
from rich.table import Table     
from rich import  print
import json
import os
from datetime import datetime

to_do_list = {} # dia : highlight, madrugar, limpieza, coding, pushups, jugar , leer

if not os.path.exists("To do list.json"):
   with open("To do list.json", "w") as f:
      json.dump(to_do_list, f)

else:
 with open("To do list.json", "r") as f:
    to_do_list = json.load(f)

dias = [
   "Lu",
   "Ma",
   "Mi",
   "Ju",
   "Vi",
   "Sa",
   "Do"
]

hoy = datetime.now()
ayer = hoy.replace(day=hoy.day - 1)

tabla = Table("Dias", style="black", title= hoy.strftime("%B %Y"))

highlight = input("Highlight del día: ")
madrugar = input("¿Madrugaste? (Sí/No): ")
limpieza = input("¿Hiciste limpieza? (Sí/No): ")
coding = input("Coding? (Sí/No): ")
pushups = input("¿Hiciste push-ups? (Sí/No): ")
jugar = input("¿Jugaste? (Sí/No): ")
leer = input("¿Leíste? (Sí/No): ")


to_do_list[ayer.strftime("%d")] = {
   "highlight": highlight,
   "madrugar": madrugar,
   "limpieza": limpieza,
   "coding": coding,
   "pushups": pushups,
   "jugar": jugar,
   "leer": leer
}

tabla.add_column("Highlight", justify="center")
tabla.add_column("Madrugar", justify="center")
tabla.add_column("Limpieza", justify="center")
tabla.add_column("Coding", justify="center")
tabla.add_column("Push-ups", justify="center")
tabla.add_column("Jugar", justify="center")
tabla.add_column("Leer", justify="center")



os.system("cls") 
for key, value in to_do_list.items():
    
 tabla.add_row(f"{key}", value["highlight"], value["madrugar"], value["limpieza"], value["coding"], value["pushups"], value["jugar"], value["leer"])
  
    


console = Console()
console.print(tabla)

with open("To do list.json", "w") as f:
    json.dump(to_do_list, f)
