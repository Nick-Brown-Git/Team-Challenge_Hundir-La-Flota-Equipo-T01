import constants as const
import numpy as np
import random

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
		self.board_shoots = np.full((tamano, tamano), const.SIMBOLO_AGUA)
		self.board_main = np.full((tamano, tamano), const.SIMBOLO_AGUA)

		self.descripcion = descripcion
		self.size = tamano

		# Cargamos los barcos para que se encuentren disponibles en el tablero
		self.__cargar_barcos__(barcos)

		print("="*50)
		print(f"Inicializando tableros de {self.size, self.size} para {self.descripcion}")
		print(f"Se han cargado {len(self.barcos)} barcos en el tablero.")
		print("="*50)



	def __cargar_barcos__(self, barcos): # {{{
		"""
		Función para cargar una lista de barcos en el tablero
		"""
		if barcos is None or len(barcos) < 1:
			raise ValueError("Lista de barcos vacía o inexistente.")

		self.barcos = barcos
	# }}}


	def __es_posicion_valida__(self, posicion): # {{{
		"""
		Función para verificar que la posición se encuentra dentro de los
		límites del tablero
		"""
		row, col = posicion
		posicion_valida = False

		print(f"\nValidando posición: ({row}, {col})")

		is_valid_row = row >= 0 and row < self.size
		is_valid_col = col >= 0 and col < self.size
		if (is_valid_row) and (is_valid_col):
			posicion_valida = True
		else:
			print(f"La posición ({row},{col}) se encuentra fuera de los límites del tablero.\n")

		return posicion_valida
	# }}}


	def __crear_posicion_aleatoria__(self): # {{{
		"""
		Función para generar una posición aleatoria
		"""
		print("Creando posición aleatoria...")

		return (random.randint(0,9), random.randint(0,9))
	# }}}


	def __generar_coordenadas__(self, barco): # {{{
		"""
		Función para generar coordenadas automáticamente

		Args:
			- barco: barco que se desea posicionar
		"""
		print("Generando posicionamiento inicial del barco...")
		row, col = self.__crear_posicion_aleatoria__()
		orientacion_idx = random.randint(1, 3)

		orientacion = const.ORIENTACION[orientacion_idx]
		print(f"\tCoordenada incial: ({row},{col})")
		print(f"\tOrientación: {orientacion}")
		print(f"\tEslora: {barco.eslora}")

		if orientacion == "N":
			x = row + barco.eslora - 1
			print(f"\tCoordenada final: ({x},{col})")

			posicion_valida = self.__es_posicion_valida__((x, col))
			if posicion_valida:
				print("¡Posicionamiento validado exitosamente!".upper())

				return row, col, orientacion
		
		if orientacion == "S":
			x = row - barco.eslora + 1
			print(f"\tCoordenada final: ({x},{col})")
			posicion_valida = self.__es_posicion_valida__((x, col))

			if posicion_valida:
				print("¡Posicionamiento validado exitosamente!".upper())

				return row, col, orientacion

		if orientacion == "E":
			y = col - barco.eslora + 1
			print(f"\tCoordenada final: ({row},{y})")
			posicion_valida = self.__es_posicion_valida__((row, y))

			if posicion_valida:
				print("¡Posicionamiento validado exitosamente!".upper())

				return row, col, orientacion

		if orientacion == "O":
			y = col + barco.eslora - 1
			print(f"\tCoordenada final: ({row},{y})")
			posicion_valida = self.__es_posicion_valida__((row, y))

			if posicion_valida:
				print("¡Posicionamiento validado exitosamente!".upper())

				return row, col, orientacion
		
		return -1, -1, "-"
	# }}}


	def __dibujar__(self, posicion, simbolo, tablero): # {{{
		"""
		Función para dibujar en el tablero un símbolo
		
		Args:
			- posicion: posición (x,y) en la que se va a dibujar el símbolo
			- simbolo: símbolo que se va a dibujar
		"""
		posicion_valida = self.__es_posicion_valida__(posicion)
		if posicion_valida:
				tablero[posicion[0], posicion[1]] = simbolo
	# }}}


	def posicionar_barco(self, barco): # {{{
		"""
		Función para posicionar un único barco

		Args:
			- barco: barco que se desea posicionar
		"""
		en_posicion = barco.esta_posicionado()
		while not en_posicion:
			coordenadas = []

			x, y, cardinal_point = self.__generar_coordenadas__(barco)
			if x != -1 and y != -1: # {{{
				print("\nEstableciendo ubicación final del barco...")
				print(f"Validando posición del barco desde ({x},{y})")

				# PUNTO CARDINAL NORTE # {{{
				if cardinal_point == "N":
					print("Orientación:", "Norte".upper())
					for i in range(x, x + barco.eslora + 1):
						if self.board_main[i][y] == const.SIMBOLO_BARCO:
							print(f"\nPosición inválida: Existe una colición con otro barco")

							# Llamada recursiva a la función posicionar barcos
							print(f"Reintanto posicionar {barco.descripcion}\n")
							return self.posicionar_barco(barco)
						else:
							coordenadas.append((i, y))
				# }}}

				# PUNTO CARDINAL SUR # {{{
				if cardinal_point == "S":
					print("Orientación:", "Sur".upper())
					for i in range(x, x - barco.eslora, -1):
						if self.board_main[i][y] == const.SIMBOLO_BARCO:
							print(f"\nPosición inválida: Existe una colición con otro barco")

							# Llamada recursiva a la función posicionar barcos
							print(f"Reintanto posicionar {barco.descripcion}\n")
							return self.posicionar_barco(barco)
						else:
							coordenadas.append((i, y))
				# }}}

				# PUNTO CARDINAL ESTE # {{{
				if cardinal_point == "E":
					print("Orientación:", "Este".upper())
					for i in range(y, y - barco.eslora, -1):
						if self.board_main[x][i] == const.SIMBOLO_BARCO:
							print(f"\nPosición inválida: Existe una colición con otro barco")

							# Llamada recursiva a la función posicionar barcos
							print(f"Reintanto posicionar {barco.descripcion}\n")
							return self.posicionar_barco(barco)
						else:
							coordenadas.append((x, i))
				# }}}

				# PUNTO CARDINAL OESTE  # {{{
				if cardinal_point == "O":
					print("Orientación:", "Oeste".upper())
					for i in range(y, y + barco.eslora):
						if self.board_main[x][i] == const.SIMBOLO_BARCO:
							print(f"\nPosición inválida: Existe una colición con otro barco")

							# Llamada recursiva a la función posicionar barcos
							print(f"Reintanto posicionar {barco.descripcion}\n")
							return self.posicionar_barco(barco)
						else:
							coordenadas.append((x, i))
				# }}}

				print("Coordenadas:", coordenadas)
				barco.establecer_ubicacion(coordenadas, cardinal_point)
				en_posicion = barco.esta_posicionado()
			# }}}
		return barco.esta_posicionado()
	# }}}


	def posicionar_barcos(self): # {{{
		"""
		Función recursiva para posicionar los barcos que no se encuentren
		posicionados en el tablero
		"""

		for index, barco in enumerate(self.barcos):
			print("="*50)
			print(f"Posicionando barco nº{index}: {barco.descripcion.upper()}")
			print("="*50)

			barco_posicionado = self.posicionar_barco(barco)
			if barco_posicionado:
				self.dibujar_barco(barco)
	# }}}


	def dibujar_barco(self, barco): # {{{
		"""
		Función para dibujar un barco en el tablero. El barco de estar
		posicionado correctamente 

		Args:
			- barco: barco que se desea dibujar
		"""
		if isinstance(barco, Barco):
			print("="*50) 
			print("Dibujando barco...") 
			print("-"*50) 
			if barco.esta_posicionado():
				barco.mostrar()
				coordenadas = barco.coordenadas

				for posicion in coordenadas:
					self.__dibujar__(
						posicion, const.SIMBOLO_BARCO, self.board_main
					)

				print(self.board_main)
			else:
				print("No se puede dibujar un barco que no esta posicionado en el tablero.\n")
			print("="*50)
	# }}}


	def dibujar_disparo_propio(self, disparo, es_acierto):
		"""
		dibujar en tablero board_ref

		- verificar que el disparo no sea en un sitio utilizado anteriormente
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
