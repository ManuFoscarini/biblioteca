from MVC.View.tela import Tela
import PySimpleGUI as sg


class TelaEmprestimo(Tela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__lista_emprestimos = []
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
    def lista_emprestimos(self):
        return self.__lista_emprestimos

    @lista_emprestimos.setter
    def lista_emprestimos(self, value):
        self.__lista_emprestimos = value

    @property
    def texto_acao(self):
        return self.__texto_acao

    @texto_acao.setter
    def texto_acao(self, value):
        self.__texto_acao = value

    def init_components(self):
        sg.theme('LightGrey3')

        layout = [
            [sg.Text('Emprestimos [Título - Usuário - Data inicial - Data final]', size=(45, 1)), ],
            [sg.Listbox(self.__lista_emprestimos, size=(60, 5))],
            [sg.Text('Título do livro:', size=(15, 1)), sg.InputText()],
            [sg.Text('Nome do usuário:', size=(15, 1)), sg.InputText()],
            [sg.Text(self.__texto_acao, justification='center', size=(61, 1))],
            [sg.Button('Incluir', size=(61, 1))],
            [sg.Button('Renovar', size=(61, 1))],
            [sg.Button('Excluir', size=(61, 1))],
            [sg.Button('Retornar', size=(61, 1))]

        ]
        self.__window = sg.Window('Empréstimo').Layout(layout)

    def tela_opcoes(self):
        self.init_components()
        opcao, values = self.__window.Read()

        if opcao is None:
            opcao = 0

        self.__window.Close()
        return {'opcao': opcao, 'values': values}