from MVC.Model.Exceções.customExceptions import InvalidNameError
from MVC.View.tela import Tela
import PySimpleGUI as sg

class TelaEmprestimo(Tela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__lista_emprestimo = []
        self.init_components()
        self.__window = None

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, value):
        self.__window = value

    @property
    def lista_emprestimo(self):
        return self.__lista_emprestimo

    @lista_emprestimo.setter
    def lista_emprestimo(self, value):
        self.__lista_emprestimo = value

    def init_components(self):
        sg.theme('LightGrey3')

        layout = [
            [sg.Text('Escolha uma opção', justification='center', size=(56, 1))],
            [sg.Listbox(self.__lista_emprestimo, size=(62, 5))],
            [sg.Text('Título do livro:', size=(15, 1)), sg.InputText()],
            [sg.Text('Nome do usuário:', size=(15, 1)), sg.InputText()],
            [sg.Button('Incluir', size=(56, 1))],
            [sg.Button('Renovar', key=2, size=(56, 1))],
            [sg.Button('Excluir', key=3, size=(56, 1))],
            [sg.Button('Retornar', key=4, size=(56, 1))]

        ]
        self.__window = sg.Window('Empréstimo').Layout(layout)


    def tela_opcoes(self):
        while True:
            self.init_components()
            opcao, values = self.__window.Read()

            if opcao is None:
                opcao = 0

            return (opcao)


    def fecha_tela(self):
        self.__window.Close()

    def pega_dados_emprestimo(self):
        print("-------- INCLUIR EMPRESTIMO ----------")
        titulo = input("Título do livro: ")

        continua = True
        while continua:
            try:
                usuario = input("Nome de quem irá emprestá-lo: ")
                if any(char.isdigit() for char in usuario) or len(usuario) < 2:
                    raise InvalidNameError(any(char.isdigit() for char in usuario), len(usuario) < 2)
                continua = False
            except InvalidNameError:
                print('Digite um nome válido')

        return {"tituloLivro": titulo, "nomeUsuario": usuario}

    def pega_titulo_exclusao(self):
        print("-------- EXCLUIR EMPRESTIMO ----------")
        titulo = input("Título do livro que deseja excluir: ")
        return titulo

    def erro_inclusao(self, erro):
        print('%s inexistente(s), empréstimo não efetuado' % erro)

    def mostra_emprestimo(self, dados_emprestimo):
        print('O livro emprestado é: %s' % (dados_emprestimo["tituloLivro"]))
        print('Quem emprestou foi: %s' % (dados_emprestimo["nomeUsuario"]))
        print('A data do emprestimo é: ' + dados_emprestimo['dataInicial'].strftime("%d/%m/%Y"))
        print('A data do fim do emprestimo é: ' + dados_emprestimo['dataFinal'].strftime("%d/%m/%Y"))
        print('E a o status do emprestimo é: %s' % (dados_emprestimo["status"]))
