def calcular_total_com_desconto(pedido: dict) -> float:
    total = 0
    for item in pedido["itens"]:
        total += item["preco"]
    valor_final = total
    if valor_final > 100:
        valor_final = valor_final * 0.9

    return valor_final


def dividir_conta(pedido: dict, numero_pessoas: int) -> bool:
    if numero_pessoas == 0:
        raise ZeroDivisionError
    return True
