from MVC.Model.Exceções.customExceptions import InvalidNameError
from MVC.View.tela import Tela


class TelaEmprestimo(Tela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def tela_opcoes(self):
        print("-------- Emprestimos ----------")
        print("Escolha a opcao")
        print("1 - Incluir Emprestimo")
        print("2 - Renovar Emprestimo")
        print("3 - Relatório de Emprestimos")
        print("4 - Excluir Emprestimo")
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

    def pega_dados_emprestimo(self):
        print("-------- INCLUIR EMPRESTIMO ----------")
        titulo = input("Título do livro: ")

        continua = True
        while continua:
            try:
                usuario = input("Nome de quem irá emprestá-lo: ")
                if any(char.isdigit() for char in usuario) or len(usuario) < 2:
                    raise InvalidNameError(any(char.isdigit() for char in usuario), len(usuario) < 2)
                continua = False
            except InvalidNameError:
                print('Digite um nome válido')

        return {"tituloLivro": titulo, "nomeUsuario": usuario}

    def pega_titulo_exclusao(self):
        print("-------- EXCLUIR EMPRESTIMO ----------")
        titulo = input("Título do livro que deseja excluir: ")
        return titulo

    def erro_inclusao(self, erro):
        print('%s inexistente(s), empréstimo não efetuado' % erro)

    def mostra_emprestimo(self, dados_emprestimo):
        print('O livro emprestado é: %s' % (dados_emprestimo["tituloLivro"]))
        print('Quem emprestou foi: %s' % (dados_emprestimo["nomeUsuario"]))
        print('A data do emprestimo é: ' + dados_emprestimo['dataInicial'].strftime("%d/%m/%Y"))
        print('A data do fim do emprestimo é: ' + dados_emprestimo['dataFinal'].strftime("%d/%m/%Y"))
        print('E a o status do emprestimo é: %s' % (dados_emprestimo["status"]))
