import constants as constants
import funciones as utils

from barco import Barco
from tablero import Tablero


barcos = constants.BARCOS

utils.bienvenido()

print("\n")
player = Tablero("Jugador", constants.TABLERO_DIMENSION, barcos)
print("\n")
player.posicionar_barcos()
print("\n")
print("\n")
opponent = Tablero("IA", constants.TABLERO_DIMENSION, barcos)
print("\n")
opponent.posicionar_barcos()
print("\n")

# player.mostrar_tablero_barcos()
# opponent.mostrar_tablero_barcos()

print("\n")
print("PARTIDA INICIADA")
print("="*50)

juego_finalizado = False
while not juego_finalizado:
	es_final = utils.establecer_turno(player, opponent, True)
	print(f"HA FINALIZADO EL TURNO DE {player.descripcion}")
	print(f"Reporte del turno:\n\tAciertos: {player.aciertos}\n")

	if es_final:
		juego_finalizado = True
		continue

	es_final = utils.establecer_turno(opponent, player, True)
	print(f"HA FINALIZADO EL TURNO DE {opponent.descripcion}\n")
	print(f"Reporte del turno:\n\tAciertos: {opponent.aciertos}\n")

	if es_final:
		juego_finalizado = True
		continue
