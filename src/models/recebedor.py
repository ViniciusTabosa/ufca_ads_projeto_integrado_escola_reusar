<<<<<<< HEAD
from src.models.usuario import Usuario
from src.models.pedido_doacao import PedidoDoacao
from src.models.pedido_material import MateriaisPedido


class Recebedor(Usuario):
    def __init__(self, id_usuario: int, nome: str, email: str, senha: str, endereco: str, telefone: int,
                 id_recebedor: int):
        super().__init__(id_usuario, nome, email, senha, "Recebedor", endereco, telefone)
        self._id_recebedor = id_recebedor
        self._meus_pedidos = []  # Lista para guardar os objetos PedidoDoacao

    @property
    def id_recebedor(self):
        return self._id_recebedor

    @id_recebedor.setter
    def id_recebedor(self, valor: int):
        self._id_recebedor = valor


    def listar_meus_pedidos(self):
        return self._meus_pedidos

    def criar_pedido_doacao(self, titulo: str, descricao: str, lista_materiais: list):
        try:
            obj_materiais = MateriaisPedido(*lista_materiais)

            novo_pedido = PedidoDoacao(self, titulo, descricao, obj_materiais)

            self._meus_pedidos.append(novo_pedido)

            return True, f"Sucesso! Pedido '{novo_pedido.titulo}' criado."

        except ValueError as erro:
=======
from src.models.usuario import Usuario
from src.models.pedido_doacao import PedidoDoacao
from src.models.pedido_material import MateriaisPedido


class Recebedor(Usuario):
    def __init__(self, id_usuario: int, nome: str, email: str, senha: str, endereco: str, telefone: int,
                 id_recebedor: int):
        super().__init__(id_usuario, nome, email, senha, "Recebedor", endereco, telefone)
        self._id_recebedor = id_recebedor
        self._meus_pedidos = []  # Lista para guardar os objetos PedidoDoacao

    @property
    def id_recebedor(self):
        return self._id_recebedor

    def listar_meus_pedidos(self):
        return self._meus_pedidos

    def criar_pedido_doacao(self, titulo: str, descricao: str, lista_materiais: list):
        try:
            obj_materiais = MateriaisPedido(*lista_materiais)

            novo_pedido = PedidoDoacao(self, titulo, descricao, obj_materiais)

            self._meus_pedidos.append(novo_pedido)

            return True, f"Sucesso! Pedido '{novo_pedido.titulo}' criado."

        except ValueError as erro:
>>>>>>> vinicius-dev
            return False, f"Erro ao criar pedido: {erro}"