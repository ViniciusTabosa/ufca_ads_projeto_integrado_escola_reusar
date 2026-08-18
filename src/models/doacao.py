<<<<<<< HEAD
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
=======
from datetime import date

class Doacao:
    def __init__(self, id_doacao, doador, pedido, data_doacao=None, status_doacao="pendente"):
        if id_doacao <= 0:
            raise ValueError("ID da doação deve ser maior que zero.")

        if doador is None:
            raise ValueError("Doador inválido.")

        if pedido is None:
            raise ValueError("Pedido inválido.")
        
        self.id_doacao = id_doacao
        self.doador = doador
        self.pedido = pedido
        self.data_doacao = data_doacao if data_doacao else date.today()
        self.status_doacao = status_doacao

    @property
    def id_doacao(self):
        return self._id_doacao

    @property
    def doador(self):
        return self._doador

    @property
    def pedido(self):
        return self._pedido

    @property
    def data_doacao(self):
        return self._data_doacao

    @property
    def status_doacao(self):
        return self._status_doacao    
    
    def confirmar(self):
        if self._status_doacao == "Realizada":
            print("ERRO: A doação já foi realizada.")
            return
        
        if self._status_doacao == "Cancelada":
            print("ERRO: Não é possível confirmar uma doação cancelada.")
            return

        self._status_doacao = "Realizada"
        self._pedido.atualizar_status("Atendido")

        print(f"Doação {self._id_doacao} realizada por {self._doador.nome} "
              f"para o pedido {self._pedido.titulo}.")

    def cancelar(self):

        if self._status_doacao == "Realizada":
            print("ERRO: Não é possível cancelar uma doação já realizada.")
            return

        if self._status_doacao == "Cancelada":
            print("ERRO: A doação já está cancelada.")
            return

        self._status_doacao = "Cancelada"
        self._pedido.atualizar_status("Pendente")

        print(f"Doação {self._id_doacao} cancelada. "
              f"Pedido {self._pedido.titulo} voltou ao status pendente.")
    
    def __str__(self):
        return (
            f"Doação {self._id_doacao}\n"
            f"Doador: {self._doador.nome} (Pedido ID {self._pedido.id_pedido})\n"
            f"Data: {self._data_doacao}\n"
            f"Status: {self._status_doacao}"
>>>>>>> vinicius-dev
        )