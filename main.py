import constants as constants
import funciones as utils

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

player = Tablero("Jugador", constants.TABLERO_DIMENSION, barcos_disponibles)
opponent = Tablero("IA", constants.TABLERO_DIMENSION, barcos_disponibles)

player.posicionar_barcos()
opponent.posicionar_barcos()

turno_finalizado = utils.establecer_turno(player, opponent, False)
print(turno_finalizado)

turno_finalizado = utils.establecer_turno(opponent, player, True)
print(turno_finalizado)
