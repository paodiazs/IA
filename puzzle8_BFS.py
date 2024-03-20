from queue import Queue

class Puzzle:
    def __init__(self, estado_inicial, estado_meta):
        self.estado_inicial = estado_inicial
        self.estado_meta = estado_meta
        self.visitados= []
        self.cola = Queue()

    
    def obtener_movimientos(self, estado):
        # Devuelve lista de todos los posibles estados
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

    def BFS(self):
        self.cola.put((self.estado_inicial, [self.estado_inicial]))
        while not self.cola.empty():
            estado, path = self.cola.get()
            self.visitados.append(estado)
            if estado == self.estado_meta:
                return path
            
            for movimiento in self.obtener_movimientos(estado):
                if movimiento not in self.visitados:
                    self.cola.put((movimiento, path + [movimiento]))
        return []  # Si ya recorrimos todo el árbol, retorna el path o nada
    
    @staticmethod
    def imprimir_puzzle(estado):
        linea = "+---+---+---+"
        for i in range(3):
            print(linea)
            for j in range(3):
                print("| {} ".format(estado[i * 3 + j]), end="")
            print("|")
        print(linea)

estado_inicial = [1, 2, 3, 4, 5, 6, 0, 7, 8]  # array de números
estado_meta = [1, 2, 3, 4, 5, 6, 7, 8, 0]

puzzle = Puzzle(estado_inicial, estado_meta)
camino_solucion = puzzle.BFS()

for movimiento in camino_solucion:
    Puzzle.imprimir_puzzle(movimiento)
