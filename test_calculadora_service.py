import pytest
#from calculadora_service import CalculadoraService
from calculadora_serviceRefatorado import CalculadoraService


class TestCalculadoraService:

    def setup_method(self):
        self.calc = CalculadoraService()

    # ---------------- SOMAR ----------------
    def test_somar_dois_numeros_positivos(self):
        assert self.calc.somar(2, 3) == 5

    def test_somar_positivo_e_negativo(self):
        assert self.calc.somar(5, -2) == 3

    def test_somar_dois_zeros(self):
        assert self.calc.somar(0, 0) == 0

    # ---------------- SUBTRAIR ----------------
    def test_subtrair_dois_numeros(self):
        assert self.calc.subtrair(5, 3) == 2

    def test_subtrair_com_resultado_negativo(self):
        assert self.calc.subtrair(3, 5) == -2

    def test_subtrair_valores_iguais(self):
        assert self.calc.subtrair(4, 4) == 0

    # ---------------- MULTIPLICAR ----------------
    def test_multiplicar_dois_positivos(self):
        assert self.calc.multiplicar(2, 3) == 6

    def test_multiplicar_por_zero(self):
        assert self.calc.multiplicar(5, 0) == 0

    def test_multiplicar_numeros_negativos(self):
        assert self.calc.multiplicar(-2, 3) == -6

    # ---------------- DIVIDIR ----------------
    def test_dividir_dois_numeros(self):
        assert self.calc.dividir(10, 2) == 5

    def test_dividir_por_zero_deve_lancar_excecao(self):
        with pytest.raises(ValueError):
            self.calc.dividir(10, 0)

    def test_dividir_numeros_decimais(self):
        assert self.calc.dividir(5, 2) == 2.5

    # ---------------- IS PAR ----------------
    def test_is_par_numero_par(self):
        assert self.calc.isPar(4) is True

    def test_is_par_numero_impar(self):
        assert self.calc.isPar(3) is False

    def test_is_par_zero(self):
        assert self.calc.isPar(0) is True

    # ---------------- VALIDAR NUMERO POSITIVO ----------------
    def test_validar_numero_positivo(self):
        assert self.calc.validarNumeroPositivo(5) is True

    def test_validar_numero_negativo(self):
        assert self.calc.validarNumeroPositivo(-3) is False

    def test_validar_zero(self):
        assert self.calc.validarNumeroPositivo(0) is False
