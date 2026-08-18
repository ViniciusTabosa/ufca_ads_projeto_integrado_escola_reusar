class MaterialEscolar:
    def __init__(self, nome, descricao, estado_conservacao, quantidade_disponivel):
        if not nome.strip():
            raise ValueError('Campo nome vazio')
        else:
            self.nome = nome

        if not descricao.strip():
            raise ValueError('Campo descrição vazio')
        else:
            self.descricao = descricao
   
        if not estado_conservacao.strip():
            raise ValueError('Campo estado de conservação vazio')
        else:
            self.estado_conservacao = estado_conservacao
   
        if (not isinstance(quantidade_disponivel, int)) or quantidade_disponivel < 0:
            raise ValueError('Campo quantidade não pode ser negativo ou não inteiro')
        else:   
            self.quantidade_disponivel = quantidade_disponivel

