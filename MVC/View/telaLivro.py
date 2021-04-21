from MVC.View.tela import Tela

class TelaLivro(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)

    def tela_opcoes(self):
        print("-------- LIVROS ----------")
        print("1 - Mostrar livro")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostra_livro(self, dados_livro):
        print('-------------------------------------------------')
        print("Nome do livro: %s" % (dados_livro["Titulo"]))
        print("Autor do livro: %s" % (dados_livro["Autor"]))
        print("Editora do livro: %s" % (dados_livro['Editora']))


