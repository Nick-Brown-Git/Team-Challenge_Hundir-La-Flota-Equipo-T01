class Barco:
	# eslora
	# descripcion
	# posicion
	# esta_tocado
	# esta_hundido
	# cant_aciertos
class Barco:
    def __init__(self, descripcion, eslora, cantidad=1):
        self.descripcion = descripcion
        self.eslora = int(eslora)
        self.cantidad = int(cantidad)

        # aciertos recibidos: dict coordenada -> True/False (True = tocado)
        self.aciertos = {}
        # ubicacion: dict coordenada -> False (no tocado) | True (tocado)
        self.ubicacion = {}

        self.cant_aciertos = 0
        self.esta_hundido = False
        self.esta_tocado = False

    # ---- posicionar ----
    def posicionar(self, punto_inicial, punto_final, ocupadas=None):
        if ocupadas is None:
            ocupadas = set()

        coords = self._rango_lineal(punto_inicial, punto_final)
        if coords is None:
            return (False, "La posición debe ser horizontal o vertical (no diagonal).")

        if len(coords) != self.eslora:
            return (False, f"La longitud entre puntos debe ser {self.eslora} (eslora del barco).")

        # comprobar solapamiento con ocupadas
        for c in coords:
            if c in ocupadas:
                return (False, f"Solapamiento con otro barco en {c}.")

        # todos los chequeos OK -> guardar ubicación
        # usamos diccionario con valor False (no tocado)
        self.ubicacion = {c: False for c in coords}
        # reset aciertos por si lo reusamos
        self.aciertos = {}
        self.cant_aciertos = 0
        self.esta_hundido = False
        self.esta_tocado = False
        return (True, None)

    # ---- danar ----
    def danar(self, posicion):
        if not self.esta_posicionado():
            return ('no_en_barco', None)

        # no pertenece al barco
        if posicion not in self.ubicacion:
            return ('no_en_barco', None)

        # ya tocada
        if self.ubicacion[posicion] is True:
            return ('repetido', None)

        # marcar acierto
        self.ubicacion[posicion] = True
        self.cant_aciertos += 1
        self.aciertos[posicion] = True
        self.esta_tocado = True

        # comprobar si hundido
        if self.cant_aciertos >= self.eslora:
            self.esta_hundido = True
            return ('hundido', posicion)
        else:
            return ('impacto', posicion)

    # ---- ayuda: saber si está posicionado ----
    def esta_posicionado(self):
        return len(self.ubicacion) != 0




	'''def __init__(self, descripcion, eslora, cantidad):
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
'''