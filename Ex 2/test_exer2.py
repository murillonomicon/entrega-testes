import pytest
import operacoes as o

def test_raiz():
    assert o.raiz_quadrada(16)==4


def test_raiz_negativa():
    with pytest.raises(ValueError):
        o.raiz_quadrada(-2)


def test_calcular_media():
    assert o.calcular_media([0.1,0.2,0.3,0.4,0.5])== pytest.approx(0.3)


def test_calcular_media_vazia():
    with pytest.raises(ValueError):
        o.calcular_media([])


def test_false():
    assert o.subtrair(2,3) is False


def test_true():
    assert o.subtrair(3,2) is True

