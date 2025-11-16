def disparo_jugador(self, board_shoots):
        """El jugador dispara hasta fallar."""

        print("\n--- Turno del id_jugador ---")
        while True:
            try:
                fila = int(input(f"Ingrese la fila (0-{self.tamaño-1}): "))
                columna = int(input(f"Ingrese la columna (0-{self.tamaño-1}): "))

                if not (0 <= fila < self.tamaño and 0 <= columna < self.tamaño):
                    print("¡Disparo fuera del tablero! Intenta otra vez.")
                    continue

                celda = board_shoots[fila][columna]
                if celda in ('X', '-'):
                    print("¡Ya disparaste ahí! Intenta otra vez.")
                    continue

                if celda == 'O':
                    board_shoots[fila][columna] = 'X'
                    print(f"¡Impacto en ({fila}, {columna})! ¡Vuelves a disparar!")
                    board_shoots.mostrar(ocultar_barcos=True)
                    continue  # puede seguir disparando
                else:
                    board_shoots[fila][columna] = '-'
                    print(f"Fallo en ({fila}, {columna}). Fin de tu turno.")
                    board_shoots.mostrar(ocultar_barcos=True)
                    break

            except ValueError:
                print("Por favor, ingresa solo números válidos.")


def disparo_oponente(self, board_main):
    """La computadora dispara hasta fallar."""
    print("\n--- Turno del oponente ---")

    while True:
        # Elegir coordenadas aleatorias válidas
        fila = random.randint(0, self.tamaño - 1)
        columna = random.randint(0, self.tamaño - 1)

        celda = board_main[fila][columna]

        # Evita disparar donde ya disparó
        if celda in ('X', '-'):
            print("¡Ya disparaste ahí! Intenta otra vez.")
            continue  # buscar otro disparo válido
        
        # Si acierta
        if celda == 'O':
            board_main[fila][columna] = 'X'
            print(f"El oponente impactó en ({fila}, {columna}) ¡dispara de nuevo!")
            board_main.mostrar(ocultar_barcos=True)
            continue  # sigue disparando
        
        # Si falla
        else:
            board_main[fila][columna] = '-'
            print(f"El oponente falló en ({fila}, {columna}). Fin del turno enemigo.")
            board_main.mostrar(ocultar_barcos=True)
            break