import constants as const

import numpy as np


def crear_coordenadas_automaticas(): # {{{
	"""
	Función para generar coordenadas automáticas
	"""
	print("Generando coordenadas automáticas...")

	return (
		random.randint(0, const.TABLERO_DIMENSION),
		random.randint(0, const.TABLERO_DIMENSION)
	)
# }}}

def preparar_disparo(disparo_automatico=False): # {{{
	print("Preparando disparo")
	print("="*50)

	if disparo_automatico:
		return crear_coordenadas_automaticas()
	else:
		x = int(input("Ingresar la coordenada x a la que desea disparar:"))
		y = int(input("Ingresar la coordenada y a la que desea disparar:"))

		return (x, y)
# }}}

def mostrar_menu(): # {{{
	opcion = 0
	while (opcion < 1) or (opcion > 3):
		print("Seleccionar una opción del menú")
		print("1) Realizar disparo")
		print("2) Ver posicionamiento de barcos propios")
		print("3) Ver disparos realizados")
		print("-"*50)
		opcion = int(input("OPCIÓN:"))
		if (opcion < 1) or (opcion > 3):
			print("-"*50)
			print("Opción incorrecta. Intente nuevamente\n")
	return opcion
# }}}

def establecer_turno(player, tablero_contrincante, disparo_automatico=False): # {{{
	"""
	Función para crear turno de usuario

	Args:
		- player: tablero del jugador al que le corresponde el turno
		- disparo_automatico: permite la generación automática de coordenadas
	"""

	print("Turno de ", player.descripcion)
	print("="*50)

	turno_finalizado = True
	while turno_finalizado:
		seleccion = mostrar_menu()
		if seleccion == 1:
			disparo_valido = False
			while not disparo_valido:
				disparo = preparar_disparo(disparo_automatico)
				disparo_valido = player.efectuar_disparo(disparo)

				es_acierto = tablero_contrincante.dibujar_disparo_enemigo(disparo)
				player.dibujar_disparo_propio(disparo, es_acierto)

		if seleccion == 2:
			print("\nFORMACION EN LINEA DE BATALLA")
			print("="*50)
			player.mostrar_tablero_barcos()

		if seleccion == 3:
			print("\nREGISTRO DE DISPAROS")
			print("="*50)
			player.mostrar_tablero_referencia()

	return turno_finalizado
# }}}

def disparo_jugador(self, posicion, tablero_oponente): # {{{
	"""El jugador dispara hasta fallar.

	disparo_automatico = True/False
	"""
	print("\n--- Turno del id_jugador ---")
	disparo_valido = False
	while not disparo_valido:
		try:
			fila = int(input(f"Ingrese la fila (0-{self.tamaño-1}): "))
			columna = int(input(f"Ingrese la columna (0-{self.tamaño-1}): "))

			es_posicion_valida = self.__posicion_valida__((fila, columna))
			if not es_posicion_valida:
				print("¡Disparo fuera del tablero! Intenta otra vez.")

			celda = tablero_oponente.matriz[fila][columna]
			if celda in ('X', '-'):
				print("¡Ya disparaste ahí! Intenta otra vez.")


			if celda == 'O':
				tablero_oponente.matriz[fila][columna] = 'X'
				print(f"¡Impacto en ({fila}, {columna})! ¡Vuelves a disparar!")
				tablero_oponente.mostrar(ocultar_barcos=True)

				continue  # puede seguir disparando
			else:
				tablero_oponente.matriz[fila][columna] = '-'
				print(f"Fallo en ({fila}, {columna}). Fin de tu turno.")
				tablero_oponente.mostrar(ocultar_barcos=True)
				break

		except ValueError:
			print("Por favor, ingresa solo números válidos.")
# }}}


def disparo_oponente(self, tablero_jugador):
	"""La computadora dispara hasta fallar."""
	print("\n--- Turno del oponente ---")

	while True:
		# Elegir coordenadas aleatorias válidas
		fila = random.randint(0, self.tamaño - 1)
		columna = random.randint(0, self.tamaño - 1)

		celda = tablero_jugador.matriz[fila][columna]

		# Evita disparar donde ya disparó
		if celda in ('X', '-'):
			print("¡Ya disparaste ahí! Intenta otra vez.")
			continue  # buscar otro disparo válido
		
		# Si acierta
		if celda == 'O':
			tablero_jugador.matriz[fila][columna] = 'X'
			print(f"El oponente impactó en ({fila}, {columna}) ¡dispara de nuevo!")
			tablero_jugador.mostrar(ocultar_barcos=False)  # Puedes ajustar si quieres ocultar
			continue  # sigue disparando
		
		# Si falla
		else:
			tablero_jugador.matriz[fila][columna] = '-'
			print(f"El oponente falló en ({fila}, {columna}). Fin del turno enemigo.")
			tablero_jugador.mostrar(ocultar_barcos=False)
			break
