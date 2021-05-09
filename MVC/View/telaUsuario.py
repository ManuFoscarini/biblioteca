import datetime
import PySimpleGUI as sg
from MVC.View.tela import Tela
from MVC.Model.Exceções.customExceptions import *


class TelaUsuario(Tela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__lista_alunos = []
        self.init_components()
        self.__window = None

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, value):
        self.__window = value

    @property
    def lista_alunos(self):
        return self.__lista_alunos

    @lista_alunos.setter
    def lista_alunos(self, value):
        self.__lista_alunos = value

    def init_components(self):
        sg.theme('LightGrey3')

        layout = [
            [sg.Text('Escolha uma opção', justification='center', size=(56, 1))],
            [sg.Radio('Aluno', "RADIO1", default=True, size=(20, 2)), sg.Radio('Professor', "RADIO1")],
            [sg.Listbox(self.__lista_alunos, size=(62, 5))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText()],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText()],
            [sg.Text('E-mail:', size=(15, 1)), sg.InputText()],
            [sg.Text('Data de nascimento:', size=(15, 1)), sg.InputText()],
            [sg.Text('Ano atual:', size=(15, 1)), sg.InputText()],
            [sg.Button('Incluir', size=(56, 1))],
            [sg.Button('Alterar', key=2, size=(56, 1))],
            [sg.Button('Excluir', key=3, size=(56, 1))],
            [sg.Button('Retornar', key=4, size=(56, 1))]
        ]
        self.__window = sg.Window('Usuário').Layout(layout)

    def tela_opcoes(self):

        while True:
            self.init_components()
            opcao, values = self.__window.Read()
            print(opcao)
            if opcao is None:
                opcao = 0


            return {'opcao': opcao, 'values': values}

    def fecha_tela(self):
        self.__window.Close()

    def pega_dados_usuario(self):
        continua = True
        while continua:
            try:
                telefone = input("Telefone: ")

                if not telefone.isdigit() or len(telefone) != 11:
                    raise InvalidPhoneNumberError(not telefone.isdigit(), len(telefone) != 11) #tela
                continua = False
            except InvalidPhoneNumberError:
                print('Telefone inválido')

        continua = True
        while continua:
            email = input("E-mail: ")
            continua = '@' not in email or '.' not in email
            if continua:
                print('E-mail inválido')

        continua = True
        while continua:
            try:
                data_entrada = input("Data de Nacimento (no formato DD/MM/AAAA): ")
                dia, mes, ano = map(int, data_entrada.split('/'))
                data_nascimento = datetime.date(ano, mes, dia)
                continua = False
            except ValueError:  # Type Error
                print('Data inválida')

        continua = True
        while continua:
            try:
                ano_atual = int(input("Ano atual: "))
                if len(str(ano_atual)) != 4:
                    raise ValueError
                continua = False
            except ValueError:
                print('Ano inválido')

        return {"Telefone": telefone, 'Email': email,
                'Data de nascimento': data_nascimento, 'Ano atual': ano_atual}

    def pega_nome(self, tipo: str):
        usuario = tipo.upper()
        print("-------- %s ---------" % usuario)

        continua = True
        while continua:
            try:
                nome = input("Nome: ")
                if any(char.isdigit() for char in nome) or len(nome) < 2:
                    raise InvalidNameError(any(char.isdigit() for char in nome), len(nome) < 2)
                continua = False
            except InvalidNameError:
                print('Digite um nome válido')

        return {"Nome": nome}

    def mostra_usuario(self, dados_usuario, tipo):
        print("Nome do %s: %s" % (tipo, dados_usuario["Nome"]))
        print("Fone do %s: %s" % (tipo, dados_usuario["Telefone"]))
        print("E-mail do %s: %s" % (tipo, dados_usuario['Email']))
        print('Nascimento do %s: ' % tipo + dados_usuario['Data de nascimento'].strftime("%d/%m/%Y"))
        print("Ano atual: %d" % (dados_usuario['Ano atual']))
