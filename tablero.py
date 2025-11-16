import constants as constants
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

        self.barcos = barcos
        self.board_shoots = np.full((tamano, tamano), constants.SIMBOLO_AGUA)
        self.board_main = np.full((tamano, tamano), constants.SIMBOLO_AGUA)


    def __es_posicion_valida(self, posicion):
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


    def __dibujar(self, posicion, simbolo, tablero="principal"):
        """
        Función para dibujar en el tablero un símbolo
        """
        posicion_valida = self.__es_posicion_valida(posicion)
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
                        self.__dibujar(posicion,
                                       constants.SIMBOLO_BARCO,
                                       self.board_main)


    def dibujar_disparo_propio(self, disparo, es_acierto):
        """
        dibujar en tablero board_ref

        """
        """El jugador dispara hasta fallar."""

        print(f"\n--- Turno del {id_jugador} ---")
        while True:
            try:
                fila = int(input(f"Ingrese la fila (0-{self.tamaño-1}): "))
                columna = int(input(f"Ingrese la columna (0-{self.tamaño-1}): "))

                if not (0 <= fila < self.tamaño and 0 <= columna < self.tamaño):
                    print("¡Disparo fuera del tablero! Intenta otra vez.")
                    continue

                celda = self.board_main[columna]
                if celda in (SIMBOLO_ACIERTO, SIMBOLO_FALLO):
                    print("¡Ya disparaste ahí! Intenta otra vez.")
                    continue

                if celda == SIMBOLO_BARCO:
                    self.board_shoots[fila][columna] = SIMBOLO_ACIERTO
                    print(f"¡Impacto en ({fila}, {columna})! ¡Vuelves a disparar!")
                    continue  # puede seguir disparando
                else:
                    self.board_shoots[fila][columna] = SIMBOLO_FALLO
                    print(f"Fallo en ({fila}, {columna}). Fin de tu turno.")
                    break

            except ValueError:
                print("Por favor, ingresa solo números válidos.")
        


    def dibujar_disparo_contrincante(self, disparo):
        """
        dibujar en tablero board_boats

        Disparo (x, y)
        dibujar acierto o fallo

        devolver si es acierto o fallo
        """
        """La computadora dispara hasta fallar."""
        print(f"\n--- Turno del {oponente} ---")

        while True:
            # Elegir coordenadas aleatorias válidas
            fila = random.randint(0, self.tamaño - 1)
            columna = random.randint(0, self.tamaño - 1)

            celda = self.board_main[fila][columna]

            # Evita disparar donde ya disparó
            if celda in (SIMBOLO_ACIERTO, SIMBOLO_FALLO):
                print("¡Ya disparaste ahí! Intenta otra vez.")
                continue  # buscar otro disparo válido
            
            # Si acierta
            if celda == SIMBOLO_BARCO:
                self.board_shoots[fila][columna] = SIMBOLO_ACIERTO
                print(f"El oponente impactó en ({fila}, {columna}) ¡dispara de nuevo!")
                continue  # sigue disparando
            
            # Si falla
            else:
                self.board_shoots[fila][columna] = SIMBOLO_FALLO
                print(f"El oponente falló en ({fila}, {columna}). Fin del turno enemigo.")
                break
        

    def mostrar_tablero_referencia(self):
        self.board_shoots

    def mostrar_tablero_barcos(self):
        self.board_main

# vim: set shiftwidth=4 tabstop=4 noexpandtb textwidth=80 filetype=python foldmethod=marker
