from src.models.usuario import Usuario

class Doador(Usuario):
    def __init__(self, id_usuario: int, nome: str, email: str, senha: str, endereco: str, telefone: int, id_doador: int):
        super().__init__(id_usuario, nome, email, senha, "Doador", endereco, telefone)
        self._id_doador = id_doador
        self._historico_doacoes = []

    @property
    def id_doador(self):
        return self._id_doador

    @id_doador.setter
    def id_doador(self, valor: int):
        self._id_doador = valor

    def pesquisar_locais_doacao(self, localizacao_busca: str):
        return f"Buscando locais de doação próximos a: {localizacao_busca}..."

    def realizar_doacao(self, id_pedido: int, data_doacao: str):
        registro = f"Doação realizada para o pedido {id_pedido} em {data_doacao}"
        self._historico_doacoes.append(registro)
        return "Doação registrada com sucesso! Obrigado por ajudar."