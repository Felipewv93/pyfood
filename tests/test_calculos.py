from app.calculos import calcular_total_com_desconto

def test_calcular_valor_sem_desconto(pedido_simples):

    assert calcular_total_com_desconto(pedido_simples) == 45.00

def calcular_valor_com_desconto(pedido_premium):

    assert calcular_total_com_desconto(pedido_premium) == 108.00