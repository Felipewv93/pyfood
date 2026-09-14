from app.validador import validar_pedido

def test_validador():
    assert validar_pedido({}) == True