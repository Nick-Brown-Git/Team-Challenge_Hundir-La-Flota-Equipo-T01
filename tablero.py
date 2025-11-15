import constants as const
import numpy as np

from barco import Barco


class Tablero:
	# board_ref
	# board_boats
	# jugador/ia
	# tamano
	# barcos
	# dibujar_disparos()
	# es acierto o fallo?
	# acierto en otro tablero
	# mostrar tablero
	# dibujar_barco() 
	# barcos_disponibles
	def __init__(self, descripcion, tamano, barcos):
		"""
		Creamos dos tableros BOARD_REF y BOARD_BOATS.

		BOARD_SHOOTs van a estar nuestros disparos al enemigo
		BOARD_MAIN van a estar nuestros barcos posicionados
		"""
		self.descripcion = descripcion
		self.size = tamano

		self.barcos_posicionados = []
		self.board_shoots = np.full((tamano, tamano), const.SIMBOLO_AGUA)
		self.board_main = np.full((tamano, tamano), const.SIMBOLO_AGUA)

		self.__cargar_barcos__(barcos)


	def __cargar_barcos__(self, barcos):
		if barcos is None or len(barcos) < 1:
			raise ValueError("Lista de barcos vacía o inexistente.")
		
		self.barcos = barcos


	def __es_posicion_valida__(self, posicion):
		"""
		Función para verificar que la posición se encuentra dentro de los \
		límites del tablero
		"""
		row, col = posicion
		posicion_valida = True

		if row < 0 or row > self.size:
			print(f"La fila, {row}, no se encuentra dentro del tamaño del \
					tablero.")
			posicion_valida = False

		if col < 0 or col > self.size:
			print(f"La columna, {col}, no se encuentra dentro del tamaño del \
					tablero.")
			posicion_valida = False

		return posicion_valida


	def __dibujar__(self, posicion, simbolo, tablero="principal"):
		"""
		Función para dibujar en el tablero un símbolo
		"""
		posicion_valida = self.__es_posicion_valida__(posicion)
		if posicion_valida:
			if tablero.lower() == "principal":
				print("Dibujando en tablero principal.")
				self.board_main[posicion[0], posicion[1]] = simbolo

			if tablero.lower() == "disparos":
				print("Dibujando en tablero de disparos.")
				self.board_shoots[posicion[0], posicion[1]] = simbolo


	def dibujar_barcos(self, barcos):
		"""
		dibujar barcos en board_boats 

		[ portaviones, acorazado, etc ]
		for barco in barcos:
			if barco.esta_posicionado:
				xi, yi, xf, yf = barco.posicion
		"""
		for _, barco in enumerate(barcos):
			if isinstance(barco, Barco):
				print(f"Dibujando {barco.descripcion}...") 
				if barco.esta_posicionado():
					ubicacion = barco.ubicacion
					for posicion in ubicacion:
						self.__dibujar__(posicion,
									   const.SIMBOLO_BARCO,
									   self.board_main)


	def generar_coordenadas(self, barco, orientacion):
		"""
		Función para generar coordenadas automáticamente

		Args:
			- barco: barco que se desea posicionar
			- orientacion: punto cardinal para el que apunta la proa del barco
		"""
		rng = np.random.default_rng()
		row, col = rng.integers(low=0, high=10, size=(0, 2))
		orientacion_idx  = rng.integers(low=0, high=4)

		orientacion = const.ORIENTACION[orientacion_idx]

		if orientacion == "N":
			x = row + (barco.eslora - 1)
			posicion_valida = self.__es_posicion_valida__((x, col))

			if posicion_valida:
				return row, col, orientacion
		
		if orientacion == "S":
			x = row - (barco.eslora + 1)
			posicion_valida = self.__es_posicion_valida__((x, col))

			if posicion_valida:
				return row, col, orientacion

		if orientacion == "E":
			x = col - (barco.eslora + 1)
			posicion_valida = self.__es_posicion_valida__((row, x))

			if posicion_valida:
				return row, col, orientacion

		if orientacion == "O":
			x = col + (barco.eslora - 1)
			posicion_valida = self.__es_posicion_valida__((row, x))

			if posicion_valida:
				return row, col, orientacion
		
		return -1, -1, "-"


	def posicionar_barcos(self):
		for index, barco in enumerate(self.barcos):
			ubicacion = []

			print("Posicionando barco", index)

			x = -1
			y = -1
			while (x == -1 or y == -1):
				x, y, cp = self.generar_coordenadas(barco)

				if cp == "N":
					for x in range(x, x + barco.eslora):
						if self.board_main[x][y] == "O":



						ubicacion.append((x, y))

				if cp == "S":
					for x in range(x + barco.eslora - 1, x):
						self.__dibujar__((x, y), const.SIMBOLO_BARCO)

				if cp == "E":
					for x in range(x, x + barco.eslora):
						self.__dibujar__((x, y), const.SIMBOLO_BARCO)

				if cp == "O":
					for x in range(x, x + barco.eslora):
						self.__dibujar__((x, y), const.SIMBOLO_BARCO)

			barco.establecer_ubicacion(ubicacion)


	def dibujar_disparo_propio(self, disparo, es_acierto):
		"""
		dibujar en tablero board_ref

		"""

		pass


	def dibujar_disparo_contrincante(self, disparo):
		"""
		dibujar en tablero board_boats

		Disparo (x, y)
		dibujar acierto o fallo

		devolver si es acierto o fallo
		"""
		pass


	def mostrar_tablero_referencia(self):
		self.board_shoots

	def mostrar_tablero_barcos(self):
		self.board_main

# vim: set shiftwidth=4 tabstop=4 noexpandtb textwidth=80 filetype=python foldmethod=marker
