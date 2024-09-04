class RaizCuadrada:
    def __init__(self, numero):
        self.numero = numero
        self.x = 1.0

    def calcular_raiz(self, iteraciones):
        for k in range(1, iteraciones + 1):
            self.x = (self.x + self.numero / self.x) / 2
            self.mostrar_resultado(k)

    def mostrar_resultado(self, iteracion):
        print(f"La raíz después de {iteracion} iteraciones es {self.x}")