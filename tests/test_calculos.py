import pytest
from app.calculos import calcular_total_com_desconto, dividir_conta

def test_calcular_valor_sem_desconto(pedido_simples):

    assert calcular_total_com_desconto(pedido_simples) == 45.00

def test_calcular_valor_com_desconto(pedido_premium):

    assert calcular_total_com_desconto(pedido_premium) == 108.00

def test_teste_deve_falhar_ao_dividir_por_zero(pedido_simples):
    with pytest.raises(ZeroDivisionError):
        dividir_conta(pedido_simples, 0)

def test_dividir_conta_valido(pedido_simples):
    assert dividir_conta(pedido_simples, 2) == True
