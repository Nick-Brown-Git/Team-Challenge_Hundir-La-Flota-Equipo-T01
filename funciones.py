def disparo_jugador(self, tablero_oponente):
        """El jugador dispara hasta fallar."""

        print("\n--- Turno del id_jugador ---")
        while True:
            try:
                fila = int(input(f"Ingrese la fila (0-{self.tamaño-1}): "))
                columna = int(input(f"Ingrese la columna (0-{self.tamaño-1}): "))

                if not (0 <= fila < self.tamaño and 0 <= columna < self.tamaño):
                    print("¡Disparo fuera del tablero! Intenta otra vez.")
                    continue

                celda = tablero_oponente.matriz[fila][columna]
                if celda in ('X', '-'):
                    print("¡Ya disparaste ahí! Intenta otra vez.")
                    continue

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