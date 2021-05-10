import datetime
import PySimpleGUI as sg
from MVC.View.tela import Tela
from MVC.Model.Exceções.customExceptions import *


class TelaUsuario(Tela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__lista_alunos = []
        self.__texto_acao = 'Escolha uma opção'
        self.init_components()
        self.__window = None

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, value):
        self.__window = value

    @property
    def lista_alunos(self):
        return self.__lista_alunos

    @lista_alunos.setter
    def lista_alunos(self, value):
        self.__lista_alunos = value

    @property
    def texto_acao(self):
        return self.__texto_acao

    @texto_acao.setter
    def texto_acao(self, value):
        self.__texto_acao = value

    def init_components(self):
        sg.theme('LightGrey3')

        layout = [
            [sg.Text('Escolha uma opção', justification='center', size=(56, 1))],
            [sg.Radio('Aluno', "RADIO1", default=True, size=(20, 2)), sg.Radio('Professor', "RADIO1")],
            [sg.Listbox(self.__lista_alunos, size=(62, 5))],
            [sg.Text(self.__texto_acao, justification='center', size=(61, 1))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText()],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText()],
            [sg.Text('E-mail:', size=(15, 1)), sg.InputText()],
            [sg.Text('Data de nascimento:', size=(15, 1)), sg.InputText()],
            [sg.Text('Ano atual:', size=(15, 1)), sg.InputText()],
            [sg.Button('Incluir', size=(61, 1))],
            [sg.Button('Alterar', size=(61, 1))],
            [sg.Button('Excluir', size=(61, 1))],
            [sg.Button('Retornar', size=(61, 1))]
        ]
        self.__window = sg.Window('Usuário').Layout(layout)

    def tela_opcoes(self):
        self.init_components()
        opcao, values = self.__window.Read()

        if opcao is None:
            opcao = 0

        self.__window.Close()
        return {'opcao': opcao, 'values': values}
