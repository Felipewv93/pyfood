import pytest


@pytest.fixture
def pedido_vazio():
    pedido = {
"endereco_entrega": "Rua das Flores, 123",
"itens": []
}
    return pedido


@pytest.fixture
def pedido_simples():
    pedido = {
"endereco_entrega": "Rua das Flores, 123",
"itens": [
{"nome": "Hamburguer", "preco": 35.00},
{"nome": "Refrigerante", "preco": 10.00}
]
}
    return pedido


@pytest.fixture
def pedido_premium():
    pedido = {
"endereco_entrega": "Rua das Flores, 123",
"itens": [
{"nome": "Hamburguer", "preco": 35.00},
{"nome": "Refrigerante", "preco": 10.00},
{"nome": "Batata frita", "preco": 25.00 },
{"nome": "Combo X-tudo", "preco": 50.00},
]
}
    return pedido