class TorreControl:
    def __init__(self):
        self.arribos = []
        self.partidas = []

    def nuevo_arribo(self, vuelo):
        self.arribos.append(vuelo)

    def nueva_partida(self, vuelo):
        self.partidas.append(vuelo)

    def asignar_pista(self):
        if self.arribos:
            vuelo = self.arribos.pop(0)
            return f'El vuelo {vuelo} aterrizó con éxito.'
        elif self.partidas:
            vuelo = self.partidas.pop(0)
            return f'El vuelo {vuelo} despegó con éxito.'
        else:
            return 'No hay vuelos en espera.'

    def ver_estado(self):
        print(f'Vuelos esperando aterrizar: {", ".join(self.arribos)}')
        print(f'Vuelos esperando despegar: {", ".join(self.partidas)}')
