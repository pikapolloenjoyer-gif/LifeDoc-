#Importo rich para mejorar la visualización de los mensajes en la consola.
from rich import print
from rich.console import Console
from rich.table import Table
import os
import json
#Proyecto final: Cree un programa de su interes que abarque buena parte de todo lo mencionado en las clases anteriores.

#Programa que simula una cuenta bancaria.

class CuentaBancaria:
    def __init__(self, nombre,apellido, saldo):
        """Constructor de la clase CuentaBancaria"""
        self.__titular = f"{nombre} {apellido}"
        self.__saldo = saldo
        
    def get_titular(self): #Método para obtener el nombre del titular de la cuenta
            """Metodo para obtener el nombre del titular de la cuenta"""
            return self.__titular
        
    def get_saldo(self): #Método para mostrar el saldo actual de la cuenta
          """Metodo para mostrar el saldo actual de la cuenta"""  
          return self.__saldo
        
    def depositar(self, monto): #Método para depositar dinero en la cuenta
            """Metodo para depositar dinero en la cuenta"""
            self.__saldo += monto
            print(f"Has depositado {monto} pesos. Tu nuevo saldo es: {self.__saldo} pesos.")
        
    def retirar(self, monto): #Método para retirar dinero de la cuenta
            """Metodo para retirar dinero de la cuenta"""
            if monto > self.__saldo:
                print("No tienes suficiente saldo para realizar esta operación.")
            else:
                self.__saldo -= monto
                print(f"Has retirado {monto} pesos. Tu nuevo saldo es: {self.__saldo} pesos.")

#Funciones para manejar los datos de los usuarios en un archivo JSON. No es necesario para el funcionamiento del programa, 
# pero lo agregué para practicar lo que vimos en clase.
def cargar_usuarios(ruta):
    if not os.path.exists(ruta):
        return {}
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def guardar_usuarios(ruta, data):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
   table = Table(title="Cuenta de Banco") #Creo una tabla para mostrar la cuenta. Y que se vea más organizadito
   table .add_column("Titular", justify="center", style="cyan", no_wrap=True)
   table .add_column("Saldo", justify="center", style="magenta")
   
   ruta_usuarios = "usuarios.json" #Archivo JSON para guardar los datos de los usuarios.

   usuarios = cargar_usuarios(ruta_usuarios) #Cargo los datos de los usuarios desde el archivo JSON. Si el archivo no existe, se crea un diccionario vacío.

   usuario_actual = None
   cuenta = None

   #Bucle para mostrar el menú de inicio de sesión y registro y tal.          
   while True:
      os.system("cls")
      os.system("clear")
      print("\n[bold cyan]Bienvenido[/bold cyan]")
      print("[bold green]1.[/bold green] Registrarse")
      print("[bold green]2.[/bold green] Iniciar sesión")
      print("[bold green]3.[/bold green] Salir")
      opcion_login = input("Selecciona una opcion: ")

      if opcion_login == "1":
        usuario = input("Crea un nombre de usuario: ").strip()
        if usuario in usuarios:
            print("Ese usuario ya existe.")
            input("Presiona enter para continuar")
            continue
        password = input("Crea una contraseña: ").strip()
        nombreb = input("Ingresa tu nombre: ")
        apellidob = input("Ingresa tu apellido: ")
        saldob = float(input("Ingresa el saldo inicial de tu cuenta: "))
        usuarios[usuario] = {
            "password": password,
            "nombre": nombreb,
            "apellido": apellidob,
            "saldo": saldob
        }
        guardar_usuarios(ruta_usuarios, usuarios)
        print("Registro exitoso. Ahora puedes iniciar sesión.")
        input("Presiona enter para continuar")
      elif opcion_login == "2":
        usuario = input("Usuario: ").strip()
        password = input("Contraseña: ").strip()
        if usuario not in usuarios or usuarios[usuario]["password"] != password:
            print("Usuario o contraseña incorrectos.")
            input("Presiona enter para continuar")
            continue
        input("Has iniciado sesión correctamente, presiona enter para continuar")
        usuario_actual = usuario
        datos = usuarios[usuario_actual]
        cuenta = CuentaBancaria(datos["nombre"], datos["apellido"], datos["saldo"])
        break
      elif opcion_login == "3":
        print("Hasta luego!")
        exit()

   while True: #Bucle para mostrar el menú de opciones al usuario, porque si no se cerraria el programa de una
      os.system("cls") # En windows. 
      os.system("clear") # En mac. por qué es diferente? no lo sé. pongo los dos por si acaso
      print("\n[bold cyan]Bienvenido al sistema bancario[/bold cyan]")
      print("[bold green]1.[/bold green] Mostrar información de la cuenta")
      print("[bold green]2.[/bold green] Depositar dinero")
      print("[bold green]3.[/bold green] Retirar dinero")
      print("[bold green]4_.[/bold green] Salir")
      opcion = input("Selecciona una opción: ")
    
      if opcion == "1":
        table.add_row(cuenta.get_titular(), str(cuenta.get_saldo()))
        print(table)
        input("Presiona enter para continuar")
      elif opcion == "2":
        monto_deposito = float(input("Ingresa el monto a depositar: "))
        cuenta.depositar(monto_deposito)
        input("Presiona enter para continuar")
      elif opcion == "3":
        monto_retiro = float(input("Ingresa el monto a retirar: "))
        cuenta.retirar(monto_retiro)
        input("Presiona enter para continuar")
      elif opcion == "4":
        print("Gracias por usar el sistema bancario. Hasta luego!")
        break


    
