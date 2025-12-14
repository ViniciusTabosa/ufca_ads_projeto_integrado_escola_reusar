# ufca_ads_projeto_integrado_escola_reusar
# ============================================================================================
# Universidade: Universidade Federal do Cariri (UFCA)
# Polo: Itapipoca-Ce
# Semestre: 2025.2
# Disciplina: Projeto Integrado II
# Equipe 9: SARAH OLIVEIRA LUCAS DIÓGENES (2025013808)
#           SAULO VICTO SOARES (2025013853)
#           PABLO HENRIQUE LIMA DE ARAUJO (2025013700)
#           VINICIUS TABOSA DOS SANTOS (2025013890)
# Entregavel 1
# ============================================================================================
# 

# Classe Doacao

class Doacao:
    def __init__(self, id_doacao, doador, pedido, data_doacao=None status_doacao="pendente"):
        self.id_doacao = id_doacao
        self.doador = doador
        self.pedido = pedido
        self.data_doacao = data_doacao if data_doacao else date.today()
        self.status_doacao = status_doacao
    
    def confirmar(self):
        self.status_doacao = "Realizada
        self.pedido.atualizar_status("Atendido")
        print(f"Doação {self.id_docao} realizada por {self.doador.nome} para o pedido {self.pedido.titulo}.")

    def cancelar(self):
        self.status_doacao = "Cancelada"
        self.pedido.atualizar("Pendente")
        print(f"Doação {slef.id_doacao} cancelada. Pedido {self.pedido.titulo} voltou ao status pendente.")
    
    def __str__(self):
        return (f"Doação {self.id_doacao}\n"
                f"Doador: {self.doador.nome} (ID {self.pedido.id_pedido})\n"
                f"Data: {self.data_doacao}\n"
                f"Status: {self.status_doacao}")