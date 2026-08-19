"""
Ponto de entrada da aplicação web Escola Reusar.

Este arquivo cria o servidor. É ele que fica "escutando" o navegador,
recebendo requisições e devolvendo respostas.
"""

import sqlite3
from pathlib import Path

from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from src.config.database import criar_banco
from src.repositories.usuario_repository import (
    buscar_por_email,
    listar_usuarios,
    salvar_usuario,
)
from src.utils.seguranca import verificar_senha

# local src
PASTA_SRC = Path(__file__).resolve().parent

# objeto da aplicação
app = FastAPI(title="Escola Reusar")

# Garante que o banco e as tabelas existem
criar_banco()


# Arquivos estáticos: CSS, imagens e as páginas HTML.
app.mount("/css", StaticFiles(directory=PASTA_SRC / "css"), name="css")
app.mount("/imgs", StaticFiles(directory=PASTA_SRC / "imgs"), name="imgs")
app.mount("/paginas", StaticFiles(directory=PASTA_SRC / "paginas"), name="paginas")


# Rotas
@app.get("/")
def pagina_inicial():
    """Entrega a landing page do projeto."""
    return FileResponse(PASTA_SRC / "index.html")


@app.post("/cadastro")
def cadastrar_usuario(
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    tipo_perfil: str = Form(...),
):
    """Recebe o formulário de cadastro e grava o usuário no banco.

    Form(...) diz ao FastAPI: "este valor vem de um campo de formulário
    HTML, e é obrigatório". O nome do parâmetro tem que ser igual ao
    atributo name= do <input> na página.
    """
    try:
        salvar_usuario(nome, email, senha, tipo_perfil)
    except sqlite3.IntegrityError:
        # A coluna email é UNIQUE: o próprio banco barrou a duplicata.
        raise HTTPException(status_code=400, detail="Este e-mail já está cadastrado.")

    # 303 faz o navegador buscar a próxima página com GET. Se fosse um
    # redirecionamento comum, atualizar a página reenviaria o formulário.
    return RedirectResponse(url="/paginas/perfil.html", status_code=303)


@app.post("/login")
def fazer_login(email: str = Form(...), senha: str = Form(...)):
    """Confere e-mail e senha e libera o acesso.

    A senha digitada nunca é comparada diretamente com o banco: calcula-se
    o hash dela e compara-se com o hash guardado.
    """
    usuario = buscar_por_email(email)

    # Mesma mensagem para e-mail inexistente e senha errada, de propósito:
    # respostas diferentes revelariam quais e-mails estão cadastrados.
    if usuario is None or not verificar_senha(senha, usuario["senha"]):
        raise HTTPException(status_code=401, detail="E-mail ou senha incorretos.")

    return RedirectResponse(url="/paginas/lista-pedidos.html", status_code=303)


@app.get("/usuarios")
def usuarios():
    """Lista os usuários gravados no banco. Serve para conferir o cadastro."""
    return listar_usuarios()


@app.get("/status")
def status():
    """Rota simples para conferir se o servidor está de pé."""
    return {"status": "no ar", "aplicacao": "Escola Reusar"}
