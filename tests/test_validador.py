from app.validador import validar_pedido

def test_validador_pedido_vazio(pedido_vazio):
    assert validar_pedido(pedido_vazio) == False

def test_validador_pedido_comum(pedido_simples):
    assert validar_pedido(pedido_simples) == True


def test_validador_pedido_sem_endereco(pedido_sem_endereco):
    assert validar_pedido(pedido_sem_endereco) == False


def test_validar_pedido_endereco_vazio(pedido_endereco_vazio):
    assert validar_pedido(pedido_endereco_vazio) == False


def test_validar_pedido_valor_baixo(pedido_valor_baixo):
    assert validar_pedido(pedido_valor_baixo) == False
