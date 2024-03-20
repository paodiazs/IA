class Puzzle:
    def __init__(self, estado_inicial, estado_meta):
        self.estado_inicial = estado_inicial
        self.estado_meta = estado_meta
        self.visitados = set()

    def obtener_movimientos(self, estado):
        movimientos = []

        posicion_vacia = estado.index(0)
        
        # Arriba
        if posicion_vacia >= 3:
            movimiento = estado[:posicion_vacia - 3] + [0] + estado[posicion_vacia - 2:posicion_vacia] + [estado[posicion_vacia - 3]] + estado[posicion_vacia + 1:]
            movimientos.append(movimiento)
        
        # Abajo
        if posicion_vacia <= 5:
            movimiento = estado[:posicion_vacia] + [estado[posicion_vacia + 3]] + estado[posicion_vacia + 1:posicion_vacia + 3] + [0] + estado[posicion_vacia + 4:]
            movimientos.append(movimiento)
        
        # Izquierda
        if (posicion_vacia % 3) > 0:
            movimiento = estado[:posicion_vacia - 1] + [estado[posicion_vacia]] + [estado[posicion_vacia - 1]] + estado[posicion_vacia + 1:]
            movimientos.append(movimiento)
        
        # Derecha
        if (posicion_vacia % 3) < 2:
            movimiento = estado[:posicion_vacia] + [estado[posicion_vacia + 1]] + [estado[posicion_vacia]] + estado[posicion_vacia + 2:]
            movimientos.append(movimiento)
        
        return movimientos

    def DFS(self, estado, path):
        self.visitados.add(tuple(estado))
        if estado == self.estado_meta:
            return path
        
        for movimiento in self.obtener_movimientos(estado):
            if tuple(movimiento) not in self.visitados:
                solucion = self.DFS(movimiento, path + [movimiento])
                if solucion:
                    return solucion
        return []  # Si no se encuentra la solución, retornamos una lista vacía

    @staticmethod
    def imprimir_puzzle(estado):
        linea = "+---+---+---+"
        for i in range(3):
            print(linea)
            for j in range(3):
                print("| {} ".format(estado[i * 3 + j]), end="")
            print("|")
        print(linea)


estado_inicial = [1, 2, 3, 4, 5, 6, 0, 7, 8]
estado_meta = [1, 2, 3, 4, 5, 6, 7, 8, 0]

puzzle = Puzzle(estado_inicial, estado_meta)
camino_solucion = puzzle.DFS(estado_inicial, [estado_inicial])

for movimiento in camino_solucion:
    Puzzle.imprimir_puzzle(movimiento)
