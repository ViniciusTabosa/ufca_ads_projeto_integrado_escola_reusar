import pytest

from src.utils.seguranca import gerar_hash_senha, verificar_senha

SENHA = "minha-senha-123"


@pytest.fixture
def hash_salvo():
    return gerar_hash_senha(SENHA)


def test_verificar_senha_correta_retorna_true(hash_salvo):
    assert verificar_senha(SENHA, hash_salvo) is True


def test_verificar_senha_errada_retorna_false(hash_salvo):
    assert verificar_senha("outra-senha", hash_salvo) is False


def test_verificar_senha_com_hash_invalido_retorna_false():
    resultado = verificar_senha("qualquer", "senha-em-texto-puro")

    assert resultado is False