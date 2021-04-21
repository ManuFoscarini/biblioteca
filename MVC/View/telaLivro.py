from MVC.View.tela import Tela
import PySimpleGUI as sg


class TelaLivro(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()
        self.__lista_livros = [1,2]

    @property
    def lista_livros(self):
        return self.__lista_livros

    @lista_livros.setter
    def lista_livros(self, value):
        self.__lista_livros = value

    def init_components(self):
        sg.theme('LightGrey3')

        # [sg.Column(listaLivros, size=(300,300), scrollable=True)]
        layout = [
            [sg.Listbox(self.__lista_livros,size=(40, 5))], #acessar essa lista
            [sg.Button('Retornar', key = 2, size=(40, 1))]
        ]


        Tela.window = sg.Window('Livros').Layout(layout)
        #Tela.window[f'-COL{layout}-'].update(visible=False)
        #Tela.window[f'-COL{layout}-'].update(visible=True)

    def tela_opcoes(self):
        self.init_components()
        opcao, values = Tela.window.Read()

        if opcao is None:
            opcao = 0

        return int(opcao)

    def mostra_livro(self, dados_livro):
        print('-------------------------------------------------')
        print("Nome do livro: %s" % (dados_livro["Titulo"]))
        print("Autor do livro: %s" % (dados_livro["Autor"]))
        print("Editora do livro: %s" % (dados_livro['Editora']))


