from MVC.Model.usuario import Usuario

class Aluno(Usuario):
    def __init__(self, nome, telefone, email, data_nascimento, ano_atual):
        super().__init__(nome, telefone, email, data_nascimento, ano_atual)

    @property
    def nome(self):
        return self.__codigo

    @nome.setter
    def nome(self, nome):
        self.__nome = nome