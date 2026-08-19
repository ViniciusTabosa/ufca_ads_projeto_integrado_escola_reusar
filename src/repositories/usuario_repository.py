"""
Repositório de usuários.

Um "repositório" é a camada que concentra os comandos SQL de uma tabela.
Toda vez que a aplicação precisar gravar ou ler usuários, ela chama uma
função daqui - e não escreve SQL espalhado pelo resto do código.

Vantagem: se um dia o banco mudar de SQLite para PostgreSQL, só este
arquivo precisa ser revisado.
"""

from src.config.database import conectar
from src.utils.seguranca import gerar_hash_senha


def salvar_usuario(nome: str, email: str, senha: str, tipo_perfil: str) -> int:
    """Grava um novo usuário no banco e devolve o id gerado.

    A senha é convertida em hash aqui dentro, de propósito: assim é
    impossível alguém esquecer de proteger a senha em outro ponto do código.

    Levanta sqlite3.IntegrityError se o e-mail já estiver cadastrado
    (a coluna email é UNIQUE no schema).
    """
    conexao = conectar()
    try:
        cursor = conexao.execute(
            "INSERT INTO usuario (nome, email, senha, tipo_perfil) VALUES (?, ?, ?, ?)",
            (nome, email, gerar_hash_senha(senha), tipo_perfil),
        )
        conexao.commit()          # sem esta linha, o cadastro NÃO é gravado
        return cursor.lastrowid   # o id_usuario que o banco gerou sozinho
    finally:
        conexao.close()


def buscar_por_email(email: str) -> dict | None:
    """Procura um usuário pelo e-mail. Devolve None se não encontrar.

    Diferente de listar_usuarios(), esta função traz a coluna senha,
    porque é ela que o login precisa conferir.
    """
    conexao = conectar()
    try:
        linha = conexao.execute(
            "SELECT id_usuario, nome, email, senha, tipo_perfil FROM usuario WHERE email = ?",
            (email,),
        ).fetchone()
        return dict(linha) if linha is not None else None
    finally:
        conexao.close()


def listar_usuarios() -> list[dict]:
    """Devolve todos os usuários cadastrados.

    A coluna 'senha' é deliberadamente omitida: senha não deve sair do banco.
    """
    conexao = conectar()
    try:
        linhas = conexao.execute(
            "SELECT id_usuario, nome, email, tipo_perfil FROM usuario ORDER BY id_usuario"
        ).fetchall()
        return [dict(linha) for linha in linhas]
    finally:
        conexao.close()
