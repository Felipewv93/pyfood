from app.validador import validar_pedido

def test_validador_pedido_vazio(pedido_vazio):
    assert validar_pedido(pedido_vazio) == False

def test_validador_pedido_comum(pedido_simples):
    assert validar_pedido(pedido_simples) == True