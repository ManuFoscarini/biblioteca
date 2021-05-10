import PySimpleGUI as sg
from MVC.View.tela import Tela


class TelaUsuario(Tela):
    def __init__(self, controlador, lista_usuarios, texto_acao, tipo):
        super().__init__(controlador)
        self.__lista_usuarios = lista_usuarios
        self.__texto_acao = texto_acao
        self.__tipo = tipo
        self.init_components()
        self.__window = None

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, value):
        self.__window = value

    @property
    def lista_usuarios(self):
        return self.__lista_usuarios

    @lista_usuarios.setter
    def lista_usuarios(self, value):
        self.__lista_usuarios = value

    @property
    def texto_acao(self):
        return self.__texto_acao

    @texto_acao.setter
    def texto_acao(self, value):
        self.__texto_acao = value

    def init_components(self):
        sg.theme('LightGrey3')

        layout = [
            [sg.Text('Lista de ' + self.__tipo, size=(40, 1))],
            [sg.Listbox(self.__lista_usuarios, size=(62, 5))],
            [sg.Text(self.__texto_acao, justification='center', size=(55, 1))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText()],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText()],
            [sg.Text('E-mail:', size=(15, 1)), sg.InputText()],
            [sg.Text('Data de nascimento:', size=(15, 1)), sg.InputText()],
            [sg.Text('Ano atual:', size=(15, 1)), sg.InputText()],
            [sg.Button('Incluir', size=(55, 1))],
            [sg.Button('Alterar', size=(55, 1))],
            [sg.Button('Excluir', size=(55, 1))],
            [sg.Button('Retornar', size=(55, 1))]
        ]
        self.__window = sg.Window('Usuário').Layout(layout)

    def tela_opcoes(self):
        self.init_components()
        opcao, values = self.__window.Read()

        if opcao is None:
            opcao = 0

        self.__window.Close()
        return {'opcao': opcao, 'values': values}
