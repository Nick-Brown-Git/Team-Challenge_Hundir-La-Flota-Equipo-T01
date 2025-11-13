def disparo_jugador(self, tablero_oponente):
        """El jugador dispara hasta fallar."""
        while True:
            try:
                fila = int(input(f"Ingrese la fila (0-{self.tamaño-1}): "))
                columna = int(input(f"Ingrese la columna (0-{self.tamaño-1}): "))

                if not (0 <= fila < self.tamaño and 0 <= columna < self.tamaño):
                    print("¡Disparo fuera del tablero! Intenta otra vez.")
                    continue

                celda = tablero_oponente.matriz[fila][columna]
                if celda in ('X', 'O'):
                    print("¡Ya disparaste ahí! Intenta otra vez.")
                    continue

                if celda == 'B':
                    tablero_oponente.matriz[fila][columna] = 'X'
                    print(f"¡Impacto en ({fila}, {columna})! ¡Vuelves a disparar!")
                    tablero_oponente.mostrar(ocultar_barcos=True)
                    continue  # puede seguir disparando
                else:
                    tablero_oponente.matriz[fila][columna] = 'O'
                    print(f"Fallo en ({fila}, {columna}). Fin de tu turno.")
                    tablero_oponente.mostrar(ocultar_barcos=True)
                    break

            except ValueError:
                print("Por favor, ingresa solo números válidos.")