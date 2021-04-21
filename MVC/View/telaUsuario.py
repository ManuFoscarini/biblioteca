import datetime

from MVC.View.tela import Tela


class TelaUsuario(Tela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def tela_opcoes(self):
        print("-------- USUÁRIOS ----------")
        print("1 - Incluir aluno")
        print("2 - Alterar aluno")
        print("3 - Listar alunos")
        print("4 - Excluir aluno")
        print("5 - Incluir professor")
        print("6 - Alterar professor")
        print("7 - Listar professor")
        print("8 - Excluir professor")
        print("0 - Retornar")

        continua = True
        while continua:
            try:
                opcao = int(input("Escolha a opção: "))
                if len(str(opcao)) != 1:
                    raise ValueError
                continua = False
            except ValueError:
                print('Insira uma opção válida')
        return opcao

    def pega_dados_usuario(self):

        continua = True
        while continua:
            telefone = input("Telefone: ")
            continua = len(telefone) != 11 or not telefone.isdigit()
            if continua:
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
            except ValueError: #falar sobre o Type Error
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
            nome = input("Nome: ")
            continua = any(char.isdigit() for char in nome) or len(nome) < 2
            if continua:
                print('Digite um nome válido')

        return {"Nome": nome}

    def mostra_usuario(self, dados_usuario, tipo):
        print("Nome do %s: %s" % (tipo, dados_usuario["Nome"]))
        print("Fone do %s: %s" % (tipo, dados_usuario["Telefone"]))
        print("E-mail do %s: %s" % (tipo, dados_usuario['Email']))
        print('Nascimento do %s: ' % tipo + dados_usuario['Data de nascimento'].strftime("%d/%m/%Y"))
        print("Ano atual: %d" % (dados_usuario['Ano atual']))
