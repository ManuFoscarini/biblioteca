
from MVC.View.telaLivro import TelaLivro
import shelve

class CtrlLivro():
    def __init__(self, ctrlBiblioteca):
        self.__ctrlBiblioteca = ctrlBiblioteca
        #self.__telaBiblioteca = TelaBiblioteca(self)
        self.__telaLivro = TelaLivro(self)
        # self.__livros = [Livro('Harry Potter', 'Livros da Manu', 'JK.Rowling'),
        #                  Livro('Capitão cueca', 'Livros da Manu', 'Vitor'),
        #                  Livro('Percy Jackson', 'Livros da Manu', 'Rick Riordan')]
        livros_file = shelve.open('livrosFile')
        self.__livros = livros_file['livros']

    def abre_tela(self):
        while True:
            opcao = self.__telaLivro.tela_opcoes()
            if opcao == 1:
                self.lista_livro()
            elif opcao == 0:
                self.__ctrlBiblioteca.abre_tela()
                break

    def retornaLivro(self, titulo):
        for livro in self.__livros:
            if livro.titulo.upper() == titulo.upper():
                return livro
        return False

    def lista_livro(self):
         if len(self.__livros) > 0:
             for livro in self.__livros:
                 self.__telaLivro.mostra_livro(
                     {'Titulo': livro.titulo, 'Autor': livro.autor, 'Editora': livro.editora})
         else:
             print('Nenhum livro cadastrado.')
        #self.__telaLivro.lista_livros = self.__livros

