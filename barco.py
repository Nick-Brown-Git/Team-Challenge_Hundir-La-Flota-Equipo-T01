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
 		# Diccionario de posiciones del barco: False = intacto, True = impactado		self.ubicacion = {}
		self.ubicacion = {}

	def posicionar(self, punto_inicial, punto_final):
		"""
		punto_inicial (xi,yi) y punto_final (xf,yf)
		verificar que la posicion no supere el tamaño del barco y 
		que el barco se quiere posicionar correctamente
		"""
		xi, yi = punto_inicial
        xf, yf = punto_final

        if xi == xf:  # vertical
            if abs(yf - yi) + 1 != self.eslora: 
                raise ValueError("La posición no coincide con la eslora")
            for y in range(min(yi, yf), max(yi, yf)+1):
                self.ubicacion[(xi, y)] = False # la posición se instancia como falsa, no tocada

        elif yi == yf:  # horizontal
            if abs(xf - xi) + 1 != self.eslora:
                raise ValueError("La posición no coincide con la eslora")
            for x in range(min(xi, xf), max(xi, xf)+1):
                self.ubicacion[(x, yi)] = False 

        else: # no se coloca un barco en diagonal o puntos separados del tablero
            raise ValueError("El barco debe estar alineado horizontal o vertical")

		pass

	def esta_posicionado(self):
		"""
		Está posicionado el barco? Si nuestro listado de ubicaciónes no tiene \
				datos entonces el barco no está posicionado
		"""
		return bool(self.ubicacion)

	def danar(self, posicion):
 		"""
		Marca un impacto en la posición indicada
		"""
        if posicion in self.ubicacion:
            self.ubicacion[posicion] = True
		
		self.cant_aciertos += 1

	def esta_tocado(self):
		"""
		Función para saber si el barco esta tocado
		"""
		return any(self.ubicacion.values())

	def esta_hundido(self):
		"""
		Función para saber si el barco esta hundido
		"""
		return all(self.ubicacion.values())
