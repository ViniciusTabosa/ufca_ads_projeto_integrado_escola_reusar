from datetime import date
from src.models.doador import Doador
from src.models.pedido_doacao import PedidoDoacao

class Doacao:
    def __init__(self, id_doacao: int, doador: Doador, pedido: PedidoDoacao, data_doacao=None, status_doacao="Pendente"):
        if not isinstance(id_doacao, int) or id_doacao <= 0:
            raise ValueError('ID da doação deve ser maior que zero.')

        if not isinstance(doador, Doador):
            raise ValueError('Doador inválido.')

        if not isinstance (pedido, PedidoDoacao):
            raise ValueError('Pedido inválido.')
        
        if status_doacao not in ["Pendente", "Realizada", "Cancelada"]:
            raise ValueError("Status da doação inválido.")
        
        self.__id_doacao = id_doacao
        self.__doador = doador
        self.__pedido = pedido
        self.__data_doacao = data_doacao if data_doacao else date.today()
        self.__status_doacao = status_doacao

    @property
    def id_doacao(self):
        return self.__id_doacao

    @property
    def doador(self):
        return self.__doador

    @property
    def pedido(self):
        return self.__pedido

    @property
    def data_doacao(self):
        return self.__data_doacao

    @property
    def status_doacao(self):
        return self.__status_doacao    
    
    
    def confirmar(self):
        if self.__status_doacao == "Realizada":
            print("ERRO: A doação já foi realizada.")
            return
        
        if self.__status_doacao == "Cancelada":
            print("ERRO: Não é possível confirmar uma doação cancelada.")
            return

        self.__status_doacao = "Realizada"
        return "Doação confirmada com sucesso."
        

    def cancelar(self):

        if self.__status_doacao == "Realizada":
            print("ERRO: Não é possível cancelar uma doação já realizada.")
            return

        if self.__status_doacao == "Cancelada":
            print("ERRO: A doação já está cancelada.")
            return

        self.__status_doacao = "Cancelada"
        return "Doação cancelada com sucesso."

    
    def __str__(self):
        return (
            f"Doação {self.__id_doacao}\n"
            f"Doador: {self.__doador.nome}\n"
            f"Data: {self.__data_doacao}\n"
            f"Status: {self.__status_doacao}"
        )