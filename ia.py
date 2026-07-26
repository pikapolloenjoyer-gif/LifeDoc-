# Crear tablero
tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def mostrar_tablero():
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def verificar_ganador(jugador):
    # Filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] == jugador:
            return True
    
    # Columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] == jugador:
            return True
    
    # Diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    
    return False

def tablero_lleno():
    for fila in tablero:
        if " " in fila:
            return False
    return True


# Juego principal
jugador_actual = "X"

while True:
    mostrar_tablero()
    
    fila = int(input(f"Jugador {jugador_actual} - Fila (0-2): "))
    col = int(input(f"Jugador {jugador_actual} - Columna (0-2): "))
    
    if tablero[fila][col] == " ":
        tablero[fila][col] = jugador_actual
        
        if verificar_ganador(jugador_actual):
            mostrar_tablero()
            print(f"🎉 ¡Jugador {jugador_actual} gana!")
            break
        
        if tablero_lleno():
            mostrar_tablero()
            print("🤝 ¡Empate!")
            break
        
        # Cambiar jugador
        jugador_actual = "O" if jugador_actual == "X" else "X"
    else:
        print("⚠ Esa posición ya está ocupada.")
