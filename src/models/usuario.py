<<<<<<< HEAD
class Usuario:
    def __init__(self, id_usuario: int, nome: str, email: str, senha: str, tipo_perfil: str, endereco: str,
                 telefone: int):

        self._id_usuario = id_usuario
        self._nome = nome
        self._email = email
        self._senha = senha
        self._tipo_perfil = tipo_perfil
        self._endereco = endereco
        self._telefone = telefone

    # --- ID DO USUÁRIO ---
    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, valor: int):
        self._id_usuario = valor

    # --- NOME ---
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if len(valor) > 0:
            self._nome = valor
        else:
            print("ERRO: Tentativa de inserir nome vazio bloqueada!")

    # --- EMAIL ---
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor: str):
        self._email = valor

    # --- SENHA ---
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor: str):
        self._senha = valor

    # --- TIPO DE PERFIL ---
    @property
    def tipo_perfil(self):
        return self._tipo_perfil

    @tipo_perfil.setter
    def tipo_perfil(self, valor: str):
        self._tipo_perfil = valor

    # --- ENDEREÇO ---
    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, valor: str):
        self._endereco = valor

    # --- TELEFONE ---
    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor: int):
        self._telefone = valor

    # metodos
    def verificar_login(self, email_tentativa: str, senha_tentativa: str) -> bool:
        if email_tentativa == self._email and senha_tentativa == self._senha:
            return True
        return False

    def atualizar_contato(self, novo_endereco: str, novo_telefone: int):
        self.endereco = novo_endereco
        self.telefone = novo_telefone
=======
class Usuario:
    def __init__(self, id_usuario: int, nome: str, email: str, senha: str, tipo_perfil: str, endereco: str,
                 telefone: int):

        self._id_usuario = id_usuario
        self._nome = nome
        self._email = email
        self._senha = senha
        self._tipo_perfil = tipo_perfil
        self._endereco = endereco
        self._telefone = telefone

    # --- ID DO USUÁRIO ---
    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, valor: int):
        self._id_usuario = valor

    # --- NOME ---
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if len(valor) > 0:
            self._nome = valor
        else:
            print("ERRO: Tentativa de inserir nome vazio bloqueada!")

    # --- EMAIL ---
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor: str):
        self._email = valor

    # --- SENHA ---
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor: str):
        self._senha = valor

    # --- TIPO DE PERFIL ---
    @property
    def tipo_perfil(self):
        return self._tipo_perfil

    @tipo_perfil.setter
    def tipo_perfil(self, valor: str):
        self._tipo_perfil = valor

    # --- ENDEREÇO ---
    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, valor: str):
        self._endereco = valor

    # --- TELEFONE ---
    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor: int):
        self._telefone = valor

    # metodos
    def verificar_login(self, email_tentativa: str, senha_tentativa: str) -> bool:
        if email_tentativa == self._email and senha_tentativa == self._senha:
            return True
        return False

    def atualizar_contato(self, novo_endereco: str, novo_telefone: int):
        self._endereco = novo_endereco
        self._telefone = novo_telefone
>>>>>>> vinicius-dev
        return "Dados de contato atualizados com sucesso."