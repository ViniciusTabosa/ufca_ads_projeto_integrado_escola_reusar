# Postagem na plataforma informando que o usuário está precisando de materiais escolares
from datetime import date

class PedidoDoacao:
    def __init__(self, titulo, descricao):
        data = date.today()
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data = f'{data.day}/{data.month}/{data.year}'
        self.__pedidoAberto = True

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        if (not isinstance(novo_titulo, str)) or (not novo_titulo.strip()):
            raise ValueError('Texto inválido')
        self.__titulo = novo_titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        if (not isinstance(nova_descricao, str)) or (not nova_descricao.strip()):
            raise ValueError('Texto inválido')
        self.__descricao = nova_descricao

    @property
    def data(self):
        return self.__data

    # @data.setter
    # def data(self, nova_data):
    #     if (not isinstance(nova_data, str)) or (not nova_data.strip()):
    #         raise ValueError('Data inválido')
    #     self.__data = nova_data

    @property
    def pedidoAberto(self):
        return self.__pedidoAberto

    def fecharPedido(self):
        self.__pedidoAberto = False