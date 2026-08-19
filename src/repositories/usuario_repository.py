from src.config.database import conectar
from src.utils.seguranca import gerar_hash_senha


def salvar_usuario(nome: str, email: str, senha: str, tipo_perfil: str) -> int:
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
    conexao = conectar()
    try:
        linhas = conexao.execute(
            "SELECT id_usuario, nome, email, tipo_perfil FROM usuario ORDER BY id_usuario"
        ).fetchall()
        return [dict(linha) for linha in linhas]
    finally:
        conexao.close()
