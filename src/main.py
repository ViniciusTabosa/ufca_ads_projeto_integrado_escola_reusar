from src.models.recebedor import Recebedor
from src.models.doador import Doador


def main():
    print("=== TESTE DE INTEGRAÇÃO\n")

    # 1. Criando um Recebedor
    print("1. Criando Recebedor...")
    recebedor = Recebedor(10, "Ana Aluna", "ana@escola.com", "123", "Rua Escola, 1", 9999, 500)
    print(f"   -> Recebedor criado: {recebedor.nome} (ID: {recebedor.id_recebedor})")

    # 2. Testando Login
    print("\n2. Testando Login...")
    if recebedor.verificar_login("ana@escola.com", "123"):
        print("   -> Login OK!")
    else:
        print("   -> Falha no Login!")

    # 3. Criando Pedido (Integração com código do colega)
    print("\n3. Criando Pedido de Doação...")
    materiais_necessarios = ["Mochila", "Caderno 10 matérias", "Estojo"]

    sucesso, mensagem = recebedor.criar_pedido_doacao(
        titulo="Preciso de material para o 5º ano",
        descricao="Minha filha começou as aulas e falta material.",
        lista_materiais=materiais_necessarios
    )

    print(f"   -> {mensagem}")

    # 4. Verificando se o pedido foi salvo corretamente
    print("\n4. Consultando detalhes do Pedido (Acessando classes do Vinicius)...")
    pedidos = recebedor.listar_meus_pedidos()

    for p in pedidos:
        # Aqui estamos acessando as propriedades da classe PedidoDoacao
        print(f"   [Título]: {p.titulo}")
        print(f"   [Data]: {p.data}")
        print(f"   [Status Aberto?]: {p.pedidoAberto}")
        print(f"   [Materiais Solicitados]: {p.materiais.retornarItens()}")

        # Testando o relacionamento inverso (Pedido sabe quem é o dono?)
        print(f"   [Dono do Pedido]: {p.recebedor.nome}")

    # 5. Testando Validação do Colega (Tratamento de Erro)
    print("\n5. Testando Erro (Título Vazio)...")
    sucesso_erro, msg_erro = recebedor.criar_pedido_doacao("", "Descrição", ["Lápis"])
    print(f"   -> Resultado: {msg_erro}")

    # 6. Simulando um Doador vendo o pedido
    print("\n6. Doador visualizando...")
    doador = Doador(20, "Carlos Doador", "carlos@doar.com", "abc", "Av. Paz", 8888, 100)
    # Supondo que o doador encontrou o pedido 'p'
    print(f"   -> O doador {doador.nome} viu o pedido de {p.recebedor.nome} e vai ajudar!")
    print(f"   -> {doador.realizar_doacao(1, '14/12/2025')}")


if __name__ == "__main__":
    main()