import constants as constants

from barco import Barco
from tablero import Tablero


barcos = constants.BARCOS

barcos_disponibles = []
print("CREANDO BARCOS...")
for barco in barcos:
    ship = Barco(barco["Descripcion"], barco["Eslora"], barco["Cantidad"])
    barcos_disponibles.append(ship)

print("\nBARCOS DISPONIBLES")
print("="*40)
for barco in barcos_disponibles:
    print("-"*40)
    print(f"BARCO: {barco.descripcion.upper()}")
    print("-"*40)
    print(f"CANTIDAD: {barco.cantidad}")
    print(f"TAMAÑO: {barco.eslora}")
    print(f"¿Está posicionado en el tablero?:", barco.esta_posicionado())
    print("\n")


tablero_jugador = Tablero("Jugador", constants.TABLERO_DIMENSION, barcos_disponibles)

tablero_ia = Tablero("IA", constants.TABLERO_DIMENSION, barcos_disponibles)

print("Queres que dibujemos los barcos?")
tablero.dibujar_barcos()

print("1. Mostrar tableros")
print("2. Disparar")
opcion = input("opcion:")
