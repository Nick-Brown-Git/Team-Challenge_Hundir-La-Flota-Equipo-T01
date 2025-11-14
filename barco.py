class Barco:
	# eslora
	# descripcion
	# posicion
	# esta_tocado
	# esta_hundido
	# cant_aciertos
	def __init__(self, descripcion, eslora, cantidad):
		self.descripcion = descripcion
		self.eslora = eslora
		self.cantidad = cantidad

		# Lista de aciertos recibidos
		self.aciertos = {}
		# Ubicación
		self.ubicacion = {}

		self.cant_aciertos = 0
		self.esta_hundido = False
		self.esta_tocado = False


	def posicionar(self, punto_inicial, punto_final):
		"""
		punto_inicial (xi,yi) y punto_final (xf,yf)
		verificar que la posicion no supere el tamaño del barco

		esta_posicionado = True
		"""
		pass

	def esta_posicionado(self):
		"""
		Está posicionado el barco? Si nuestro listado de ubicaciónes no tiene \
				datos entonces el barco no está posicionado
		"""
		return len(self.ubicacion) != 0

	def danar(self, posicion):
		"""
		Funcion para dañar el barco
		"""
		
		self.cant_aciertos += 1

	def esta_tocado(self):
		"""
		Función para saber si el barco esta tocado
		"""
		return self.cant_aciertos > 0

	def esta_hundido(self):
		"""
		Función para saber si el barco esta hundido
		"""
		return self.cant_aciertos == self.eslora
