class CalculadoraService:

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não permitida")
        return a / b

    def isPar(self, a):
        return a % 2 == 0

    def validarNumeroPositivo(self, a):
        return a > 0
