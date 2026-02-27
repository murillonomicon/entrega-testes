def raiz_quadrada(a):
    if a<0:
        raise ValueError("Operação inválida: não é possível calcular raiz quadrada com números negativos.")
    else:
        raiz= a**0.5
        return raiz
    
def calcular_media(a:list):
    if len(a) == 0:
        raise ValueError("Operação inválida: não é possível calcular a média de uma lista vazia.")
    else:
        media = sum(a)/len(a)
        return media
    
def subtrair(a,b):
    subtracao = a-b
    if subtracao > 0:
        return True
    return False
