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
tablero_ia = Tablero("IA", constants.TABLERO_DIMENSION, barcos_disponibles)

tablero_jugador.posicionar_barcos()
tablero_ia.posicionar_barcos()

disparo = (5,5) # disparo de jugador
tablero_jugador.efectuar_disparo(disparo) # verificamos que sea valido
es_acierto = tablero_ia.dibujar_disparo_enemigo(disparo) # dibujamos en tablero del contrincante el disparo y comprobamos si es acierto o no
tablero_jugador.dibujar_disparo_propio(disparo, es_acierto) # dibujamos en nuestro tablero el resultado


disparo = (3,7) # disparo de ia
tablero_ia.efectuar_disparo(disparo) # verificamos qque sea un disparo válido
es_acierto = tablero_jugador.dibujar_disparo_enemigo(disparo) # dibujamos en tablero enemigo el disparo y comprobamos si es acierto o no
tablero_jugador.dibujar_disparo_propio(disparo, es_acierto) # dibujamos en tablero de ia el resultado