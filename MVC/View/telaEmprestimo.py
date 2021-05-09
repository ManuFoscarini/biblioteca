from MVC.Model.Exceções.customExceptions import InvalidNameError
from MVC.View.tela import Tela
import PySimpleGUI as sg

class TelaEmprestimo(Tela):
    def __init__(self, controlador):
        super().__init__(controlador)

        self.init_components()
        self.__window = None


    def init_components(self):
        sg.theme('LightGrey3')

        layout = [
            [sg.Text('Escolha uma opção', justification='center', size=(40, 1))],
            [sg.Button('Incluir', key=1, size=(40, 1))],
            [sg.Button('Renovar', key=2, size=(40, 1))],
            [sg.Button('Listar', key=3, size=(40, 1))],
            [sg.Button('Excluir', key=4, size=(40, 1))],
            [sg.Button('Retornar', key=0, size=(40, 1))]

        ]
        self.__window = sg.Window('Empréstimo').Layout(layout)


    def tela_opcoes(self):
        while True:
            self.init_components()
            opcao, values = self.__window.Read()

            if opcao is None:
                opcao = 0

            return int(opcao)


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
