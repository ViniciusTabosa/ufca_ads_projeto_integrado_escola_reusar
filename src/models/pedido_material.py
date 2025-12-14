class MateriaisPedido:
    def __init__(self, *args):
        self.__materiais = []
        for i in args:
            if (not isinstance(i, str)) or (not i.strip()):
                raise ValueError('Item inválido')
            else:
                self.__materiais.append(i)

    def adicionarItem(self, item):
        if (not isinstance(item, str)) or (not item.strip()):
            raise ValueError('Item inválido')
        else:
            self.__materiais.append(item)

    def removerItem(self, item):
        if (not isinstance(item, str)) or (not item.strip()):
            raise ValueError('Item não encontrado')
        else:
            self.__materiais.remove(item)

    def retornarItens(self):
        return self.__materiais