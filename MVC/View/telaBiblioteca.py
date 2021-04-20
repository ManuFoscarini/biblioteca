from MVC.View.tela import Tela
import PySimpleGUI as sg


class TelaBiblioteca(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)
        #self.__window = None
        #self.init_components()

    #def init_components(self):


    def tela_opcoes(self):
        print("-------- BIBLIOTECA ---------")
        print("Escolha sua opcao")
        print("1 - Livros")
        print("2 - Usuários")
        print("3 - Emprestimos")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao: "))
        return opcao




