def calcular_imc(peso, altura):
    return peso/altura**2

class Cachorro:
    def __init__(self, cor='preto'):
        self.cor=cor

    def latir(self):
        print('AU AU')

