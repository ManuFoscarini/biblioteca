from MVC.View.telaLivro import TelaLivro
import shelve

class CtrlLivro():
    def __init__(self, ctrlBiblioteca):
        self.__ctrlBiblioteca = ctrlBiblioteca
        #self.__telaBiblioteca = TelaBiblioteca(self)
        self.__telaLivro = TelaLivro(self)

        # self.__livros = [Livro('Harry Potter', 'Livros da Manu', 'JK.Rowling'),
        #                 Livro('Capitão cueca', 'Livros da Manu', 'Vitor'),
        #                 Livro('Percy Jackson', 'Livros da Manu', 'Rick Riordan')]
        livros_file = shelve.open('Livros/livrosFile')
        self.livros = livros_file['livros']
        #livros_file['livros'] = self.__livros

        self.lista_livro()

    def abre_tela(self):
        opcao = self.__telaLivro.tela_opcoes()
        if opcao == 1:
            self.__telaLivro.fecha_tela()

    def retornaLivro(self, titulo):
        for livro in self.livros:
            if livro.titulo.upper() == titulo.upper():
                return livro
        return False

    def lista_livro(self):
        lista_livros_tela = []
        if len(self.livros) > 0:
            for livro in self.livros:  # compor o dicionário, passar pra tela
                lista_livros_tela.append(livro.titulo)
        else:
            print('Nenhum livro cadastrado.')
        self.__telaLivro.lista_livros = lista_livros_tela

