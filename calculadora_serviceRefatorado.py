class CalculadoraService:

    def somar(self, parcela1, parcela2):
        return parcela1 + parcela2

    def subtrair(self, minuendo, subtraendo):
        return minuendo - subtraendo

    def multiplicar(self, multiplicando, multiplicador):
        return multiplicando * multiplicador

    def dividir(self, dividendo, divisor):
        if divisor == 0:
            raise ValueError("Divisão por zero não permitida")
        return dividendo / divisor

    def isPar(self, numero):
        return numero % 2 == 0

    def validarNumeroPositivo(self, numero):
        return numero > 0