# Camada de acesso ao banco de dados (SQLite).

import sqlite3
from pathlib import Path

# src/config/
PASTA_CONFIG = Path(__file__).resolve().parent

# Raiz do projeto
RAIZ_PROJETO = PASTA_CONFIG.parent.parent

# O banco é um único arquivo na raiz do projeto.
CAMINHO_BANCO = RAIZ_PROJETO / "escola_reusar.db"

# Cria as tabelas.
CAMINHO_SCHEMA = PASTA_CONFIG / "schema.sql"


def conectar() -> sqlite3.Connection:
    #Abre uma conexão com o banco
    conexao = sqlite3.connect(CAMINHO_BANCO)

    # devolve as linhas como dicionários
    conexao.row_factory = sqlite3.Row

    return conexao


def criar_banco() -> None:
    # Cria o arquivo do banco e as tabelas descritas em schema.sql.
    sql = CAMINHO_SCHEMA.read_text(encoding="utf-8")

    conexao = conectar()
    try:
        conexao.executescript(sql)
        conexao.commit()
    finally:
        conexao.close()

    print(f"Banco pronto em: {CAMINHO_BANCO}")

if __name__ == "__main__":
    criar_banco()
