def calcular_preco_final(preco_base, cupom=None, frete_gratis=False):
    if preco_base <= 0:
        raise ValueError("O preço base deve ser maior que zero.")

    desconto = 0

    if cupom == "PROMO10":
        desconto = 0.10
    elif cupom == "PROMO20":
        desconto = 0.20
    elif cupom is not None:
        desconto = 0

    preco_com_desconto = preco_base * (1 - desconto)

    if frete_gratis or preco_com_desconto > 500:
        frete = 0
    else:
        frete = 20

    return preco_com_desconto + frete