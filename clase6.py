import os
from rich import print


turno = False # False = jugador 1, True = jugador 2
tablon = [
    0,0,0,
    0,0,0, #Tablón
    0,0,0
]

reglas = [
    (0,1,2),#Tabla entera
    (3,4,5),#
    (6,7,8),#
    (0,3,6),#Columnas        
    (1,4,7),#
    (2,5,8),#
    (0,4,8),#Diagonales
    (2,4,6)#
]

# 1 x
# 2 o

                   #Jugadas
def definir_jugada(jugada):#Convierte los 1 y los 2 en X y O respectivamente, esto hace que el tablero se vea más amigable 
    #para el usuario, ya que en lugar de ver números verá las jugadas de cada jugador.También hace que el tablero se muestre vacío.
    if jugada == 0:
        return " "
    elif jugada == 1:
        return "[bold red]X[/]"
    elif jugada == 2:
        return "[bold yellow]O[/]"


def mostrar_tabla(tablon):
    print(f"{definir_jugada(tablon[0])}|{definir_jugada(tablon[1])}|{definir_jugada(tablon[2])}")
    print(f"{definir_jugada(tablon[3])}|{definir_jugada(tablon[4])}|{definir_jugada(tablon[5])}")
    print(f"{definir_jugada(tablon[6])}|{definir_jugada(tablon[7])}|{definir_jugada(tablon[8])}")

                    #tablón  #Reglas
def validar_ganador(tablon, validaciones):
               #Reglas
    for val in validaciones:
        a, b, c = val
        if tablon[a] == tablon[b] == tablon[c] != 0: #Si las casillas a, b y c son iguales y no son 0 (es decir, no están vacías), entonces hay un ganador.
            return True
    return False#?

def tablero_lleno(tablon): #si el tablero está lleno, es decir, no hay casillas vacías (0), entonces se considera un empate.
    for casilla in tablon:
        if casilla == 0:
            return False
    return True

while True:
    os.system("cls")
    turno = not turno #hace que el turno cambie cada vez que se ejecute el ciclo, es decir, si el turno es falso se vuelve verdadero y viceversa, esto hace que el juego sea para dos jugadores.
    
    if turno == True:
      print("[bold yellow]Turno del jugador 2 (O)[/]")
    else:
      print("[bold red]Turno del jugador 1 (X)[/]")

    mostrar_tabla(tablon)
    
    jugada = int(input("Ingrese su jugada: ")) -1
    if jugada < 0 or jugada > 8:
        input("Jugada no valida")
        continue
    if tablon[jugada] != 0:
        input("Esa casilla ya esta ocupada")
        continue


    tablon[jugada] = 1 if not turno else 2 #A "jugada" se le asigna un uno o un dos dependiendo a que jugador le toque, esto hace que cuando el usuario juegue en la casilla 9 al asiganarle un 1 o 2 se ponga 
                                            #la X o la O, que es como está diseñado en el método de "definir jugada"
    
    if validar_ganador(tablon, reglas):
        os.system("cls")
        mostrar_tabla(tablon)
        print("Felicidades has ganado!")                     
        for i in range(0,9):  #Con un ciclo for podria eliminar la tabla para que cuando el usario presione enter se le presente un nuevo juego? sí 
            tablon[i] = 0   #Done   
        final = input("Presiona Enter para continuar o escriba end para salir: ")
        if final == "end":
         break
    elif tablero_lleno(tablon):
        os.system("cls")
        mostrar_tabla(tablon)
        print("Empate!")
        for i in range(0,9):
            tablon[i] = 0
        final = input("Presiona Enter para continuar. Esto no se puede quedar así! ")
