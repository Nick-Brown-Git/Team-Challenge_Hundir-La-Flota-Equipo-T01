import constants as constants

from barco import Barco
from tablero import Tablero


barcos = constants.BARCOS

barcos_disponibles = []
print("CREANDO BARCOS...")
for barco in barcos:

	cantidad = barco["Cantidad"]
	for x in range(cantidad):
		ship = Barco(barco["Descripcion"], barco["Eslora"])
		barcos_disponibles.append(ship)

"""
print("\nBARCOS DISPONIBLES")
print("="*40)
for barco in barcos_disponibles:
	print("-"*40)
	print(f"BARCO: {barco.descripcion.upper()}")
	print("-"*40)
	##print(f"CANTIDAD: {barco.cantidad}")
	print(f"TAMAÑO: {barco.eslora}")
	print(f"¿Está posicionado en el tablero?:", barco.esta_posicionado())
	print("\n")
"""

tablero_jugador = Tablero("Jugador", constants.TABLERO_DIMENSION, barcos_disponibles)
tablero_jugador.posicionar_barcos()
fila, columna = tablero_jugador.dibujar_disparo_propio()



tablero_ia = Tablero("IA", constants.TABLERO_DIMENSION, barcos_disponibles)
tablero_ia.posicionar_barcos()
es_acierto = tablero_ia.dibujar_disparo_contrincante(fila, columna)


fila = int(input(f"Ingrese la fila (0-{self.tamaño-1}): "))
columna = int(input(f"Ingrese la columna (0-{self.tamaño-1}): "))
tablero_jugador.disparo_jugador((fila, columna), tablero_contrincante.board_main)


