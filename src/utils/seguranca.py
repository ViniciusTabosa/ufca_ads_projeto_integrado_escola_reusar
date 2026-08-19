"""
Proteção de senhas.

Senha NUNCA deve ser guardada como o usuário digitou. Se o banco vazar,
todas as contas vazam junto - e como as pessoas repetem senha, o estrago
passa para outros sistemas.

A solução é guardar um "hash": um resultado matemático que se calcula a
partir da senha, mas do qual não se volta para a senha original. Na hora
do login, calcula-se o hash do que foi digitado e compara-se com o que
está no banco.

Usamos apenas a biblioteca padrão do Python (hashlib e secrets),
sem dependências externas.
"""

import hashlib
import hmac
import secrets

# Quantas vezes o cálculo é repetido. Número alto de propósito: deixa o
# processo lento para quem tenta descobrir senhas por força bruta.
ITERACOES = 200_000


def gerar_hash_senha(senha: str) -> str:
    """Transforma a senha em um hash seguro, pronto para gravar no banco.

    Devolve uma string no formato "salt:hash", ambos em hexadecimal.

    O "salt" é um valor aleatório diferente para cada usuário. Ele garante
    que duas pessoas com a mesma senha tenham hashes diferentes no banco.
    """
    salt = secrets.token_bytes(16)

    hash_bytes = hashlib.pbkdf2_hmac(
        "sha256",
        senha.encode("utf-8"),
        salt,
        ITERACOES,
    )

    return f"{salt.hex()}:{hash_bytes.hex()}"


def verificar_senha(senha_digitada: str, hash_salvo: str) -> bool:
    """Confere se a senha digitada corresponde ao hash guardado no banco."""
    try:
        salt_hex, hash_hex = hash_salvo.split(":")
        salt = bytes.fromhex(salt_hex)
    except ValueError:
        # Formato inesperado (por exemplo, senha antiga em texto puro).
        return False

    hash_calculado = hashlib.pbkdf2_hmac(
        "sha256",
        senha_digitada.encode("utf-8"),
        salt,
        ITERACOES,
    )

    # compare_digest evita que o tempo de resposta revele quantos
    # caracteres do hash estavam certos.
    return hmac.compare_digest(hash_calculado.hex(), hash_hex)
