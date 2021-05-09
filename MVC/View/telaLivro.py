from MVC.View.tela import Tela
import PySimpleGUI as sg


class TelaLivro(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.__lista_livros = []
        self.init_components()
        self.__window = None

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, value):
       self.__window = value

    @property
    def lista_livros(self):
        return self.__lista_livros

    @lista_livros.setter
    def lista_livros(self, value):
        self.__lista_livros = value

    def init_components(self):
        sg.theme('LightGrey3')


        layout = [
            [sg.Listbox(self.__lista_livros, size=(40, 5))],
            [sg.Button('Retornar', key=1, size=(40, 1))]
        ]

        self.__window = sg.Window('Livros').Layout(layout)

    def tela_opcoes(self):
        self.init_components()
        opcao, values = self.__window.Read()

        if opcao is None:
             opcao = 0

        return int(opcao)

    def fecha_tela(self):
        self.__window.Close()

    def mostra_livro(self, dados_livro):
        print('-------------------------------------------------')
        print("Nome do livro: %s" % (dados_livro["Titulo"]))
        print("Autor do livro: %s" % (dados_livro["Autor"]))
        print("Editora do livro: %s" % (dados_livro['Editora']))


