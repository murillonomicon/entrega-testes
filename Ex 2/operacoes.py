import math
import pytest

def raiz_quadrada(numero):
    if numero < 0:
        raise ValueError("Número negativo")
    else:
        return math.sqrt(numero)

def calcular_media(lista_numeros):
    count = len(lista_numeros)

    if count <= 0:
        raise ValueError("Lista vazia")
    else:
        return sum(lista_numeros) / count


