from app.pagamento import finalizar_compra
from unittest.mock import call

def test_deve_verificar_fraude_antes_de_cobrar(mocker, pedido_simples):
    mock_gateway = mocker.Mock()
    finalizar_compra(pedido_simples, mock_gateway)

    roteiro_esperado = [
        call.verificar_fraude(pedido_simples),
        call.cobrar(pedido_simples)
    ]

    mock_gateway.assert_has_calls(roteiro_esperado, any_order=False)
