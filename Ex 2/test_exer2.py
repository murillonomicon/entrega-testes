import pytest
from operacoes import raiz_quadrada, calcular_media

class TesteOperacoes():
    def test_raiz_quadrada_numero_negativo(self):
        with pytest.raises(ValueError):
            raiz_quadrada(-4)
    
    def test_raiz_quadrada_valores_inteiros(self):
        assert raiz_quadrada(4) == 2


    def test_raiz_quadrada_valores_float(self):
        resultado = raiz_quadrada(7.5)
        assert resultado == pytest.approx(2.7386127875258306)


    def test_calcular_media_inteiros(self):
        assert calcular_media([2, 4, 6]) == 4

    def test_calcular_media_floats(self):
        resultado = calcular_media([0.1, 0.2, 0.3])
        assert resultado == pytest.approx(0.2)
    
    def test_calcular_media_lista_vazia(self):
        with pytest.raises(ValueError):
            calcular_media([])