# Postagem na plataforma informando que o usuário está precisando de materiais escolares
from datetime import date

class PedidoDoacao:
    def __init__(self, usuario, titulo, descricao):
        data = date.today()
        self.__recebedor = usuario
        if (not isinstance(titulo, str)) or (not titulo.strip()):
            self.__titulo = titulo
        else:
            raise ValueError('Título inválido')

        if (not isinstance(descricao, str)) or (not descricao.strip()):
            self.__descricao = descricao
        else:
            raise ValueError('Descrição inválido')

        self.__data = f'{data.day}/{data.month}/{data.year}'
        self.__pedidoAberto = True

    @property
    def recebedor(self):
        return self.__recebedor

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        if (not isinstance(novo_titulo, str)) or (not novo_titulo.strip()):
            raise ValueError('Título inválido')
        self.__titulo = novo_titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        if (not isinstance(nova_descricao, str)) or (not nova_descricao.strip()):
            raise ValueError('Descrição inválida')
        self.__descricao = nova_descricao

    @property
    def data(self):
        return self.__data

    @property
    def pedidoAberto(self):
        return self.__pedidoAberto

    def fecharPedido(self):
        self.__pedidoAberto = False