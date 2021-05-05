from MVC.Model.DAO.livroDAO import LivroDAO
from MVC.View.telaLivro import TelaLivro


class CtrlLivro():
    def __init__(self, ctrlBiblioteca):
        self.__ctrlBiblioteca = ctrlBiblioteca
        self.__telaLivro = TelaLivro(self)
        self.__livroDAO = LivroDAO()

        # self.__livroDAO.add(Livro('Harry Potter', 'Livros da Manu', 'JK.Rowling'))
        # self.__livroDAO.add(Livro('Capitão Cueca', 'Livros da Manu', 'Vitor'))
        # self.__livroDAO.add(Livro('Percy Jackson', 'Livros da Manu', 'Rick Riordan'))

        self.lista_livro()

    def abre_tela(self):
        opcao = self.__telaLivro.tela_opcoes()
        if opcao == 1:
            self.__telaLivro.fecha_tela()

    def retornaLivro(self, titulo):
        livro = self.__livroDAO.get(titulo)
        if livro is not None:
            return livro
        return False

    def lista_livro(self):
        livros_dict_values = self.__livroDAO.get_all()
        lista_livros = []
        if len(livros_dict_values) > 0:
            for livro in livros_dict_values:
                lista_livros.append(livro.titulo)
        else:
            lista_livros.append('Nenhum livro cadastrado.')
        self.__telaLivro.lista_livros = lista_livros
