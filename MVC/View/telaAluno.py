from MVC.View.telaUsuario import TelaUsuario


class TelaAluno(TelaUsuario):
    def __init__(self, controlador):
        self.__lista_usuarios = []
        self.__texto_acao = 'Escolha uma opção:'
        super().__init__(controlador, self.__lista_usuarios, self.__texto_acao, 'alunos')
        self.init_components()

    def init_components(self):
        super().init_components()

    def tela_opcoes(self):
        return super().tela_opcoes()
