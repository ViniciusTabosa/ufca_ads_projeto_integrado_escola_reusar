from src.models.doador import Doador
from src.models.recebedor import Recebedor
from src.models.pedido_doacao import PedidoDoacao
from src.models.pedido_material import MateriaisPedido
from src.models.doacao import Doacao

def main():
    materiais = MateriaisPedido("Caderno", "Lápis")

    recebedor = Recebedor(
        id_usuario=1,
        nome="EEEP",
        email="eeep@gmail.com",
        senha="123",
        endereco="Rua B",
        telefone=36318552,
        id_recebedor=1
    )

    pedido = PedidoDoacao(
        usuario=recebedor,
        titulo="Pedido de materiais",
        descricao="Precisamos de materiais escolares",
        materiais=materiais
    )

    doador = Doador(
        id_usuario=2,
        nome="Sarah Lucas",
        email="sarah@gmail.com",
        senha="123",
        endereco="Rua A",
        telefone=88998585698,
        id_doador=1
    )

    doacao = Doacao(
        id_doacao=1,
        doador=doador,
        pedido=pedido
    )

    print("=== DOAÇÃO CRIADA ===")
    print(doacao)

    print("\n=== CONFIRMANDO DOAÇÃO ===")
    print(doacao.confirmar())
    print(doacao)

    print("\n=== TENTANDO CANCELAR ===")
    print(doacao.cancelar())


if __name__ == "__main__":
    main()