from MVC.View.tela import Tela
import PySimpleGUI as sg

class TelaBiblioteca(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.theme('LightGrey3')

        layout = [
            [sg.Text('Escolha uma opção', justification='center', size=(40, 1))],
            [sg.Button('Livros', key = 1, size=(40, 1))],
            [sg.Button('Usuários', key = 2, size=(40, 1))],
            [sg.Button('Empréstimos', key = 3,  size=(40, 1))]
        ]
        Tela.window = sg.Window('Biblioteca').Layout(layout)

    def tela_opcoes(self):
        self.init_components()
        opcao, values = Tela.window.Read()

        if opcao is None:
            opcao = 0

        return int(opcao)





