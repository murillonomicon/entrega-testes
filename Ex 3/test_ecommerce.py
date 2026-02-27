import pytest
from ecommerce import calcular_preco_final

def test_preco_zero():
    with pytest.raises(ValueError):
        calcular_preco_final(0)

def test_preco_negativo():
    with pytest.raises(ValueError):
        calcular_preco_final(-100)

def test_sem_cupom_com_frete():
    resultado = calcular_preco_final(100)
    assert resultado == 120


def test_sem_cupom_frete_gratis_parametro():
    resultado = calcular_preco_final(100, frete_gratis=True)
    assert resultado == 100


def test_sem_cupom_frete_gratis_por_valor():
    resultado = calcular_preco_final(600)
    assert resultado == 600

def test_cupom_10_porcento():
    resultado = calcular_preco_final(200, cupom="PROMO10")
    assert resultado == pytest.approx(200 * 0.9 + 20)

def test_cupom_20_porcento():
    resultado = calcular_preco_final(200, cupom="PROMO20")
    assert resultado == pytest.approx(200 * 0.8 + 20)

def test_cupom_invalido():
    resultado = calcular_preco_final(200, cupom="INVALIDO")
    assert resultado == 220

def test_desconto_que_ativa_frete_gratis():
    resultado = calcular_preco_final(600, cupom="PROMO20")
    assert resultado == pytest.approx(480 + 20)


def test_desconto_que_ultrapassa_500():
    resultado = calcular_preco_final(600, cupom="PROMO10")
    assert resultado == pytest.approx(540)