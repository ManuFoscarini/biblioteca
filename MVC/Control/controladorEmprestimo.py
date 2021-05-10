from MVC.Model.DAO.emprestimoDAO import EmprestimoDAO
from MVC.Model.Exceções.customExceptions import InvalidNameError
from MVC.Model.emprestimo import Emprestimo
from MVC.Control.ctrlLivro import CtrlLivro
from MVC.Control.controladorUsuario import ControladorUsuario
from MVC.View.telaEmprestimo import TelaEmprestimo
from MVC.Model.dataEmprestimo import DataEmprestimo
from datetime import timedelta as td


class ControladorEmprestimo():

    def __init__(self, ctrlBiblioteca):
        self.__ctrlBiblioteca = ctrlBiblioteca
        self.__emprestimo = []

        self.__tela_emprestimo = TelaEmprestimo(self)
        self.__controlador_livro = CtrlLivro(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__data_emprestimo = DataEmprestimo()
        self.__emprestimoDAO = EmprestimoDAO()

    def retorna_notificacao(self, mensagem):
        self.__tela_emprestimo.texto_acao = mensagem

    def valida_dados(self, usuario):
        try:
            if any(char.isdigit() for char in usuario) or len(usuario) < 2:
                raise InvalidNameError()
            return True
        except InvalidNameError:
            return False

    def inclui_emprestimo(self, titulo_livro, nome_usuario):
        dados_validos = self.valida_dados(nome_usuario)

        if dados_validos:
            livro = self.__ctrlBiblioteca.ctrlLivro.retornaLivro(titulo_livro)
            usuario = self.__ctrlBiblioteca.controladorUsuario.retornaUsuario(nome_usuario)

            if livro:
                if usuario:
                    self.__emprestimoDAO.add(Emprestimo(livro, usuario, DataEmprestimo()))
                    self.retorna_notificacao('Empréstimo efetuado!')
                else:
                    self.retorna_notificacao('Usuário inexistente, empréstimo não efetuado')
            elif usuario:
                self.retorna_notificacao('Livro inexistente, empréstimo não efetuado')
            else:
                self.retorna_notificacao('Livro e usuário inexistentes, empréstimo não efetuado')
        else:
            self.retorna_notificacao('Digite um nome válido, com no mínimo dois caracteres (apenas letras)')

    def lista_emprestimos(self):
        emprestimos_dict_values = self.__emprestimoDAO.get_all()
        lista_emprestimos = []
        if len(emprestimos_dict_values) > 0:
            for emprestimo in emprestimos_dict_values:
                emprestimo_info = emprestimo.livro.titulo + ' - ' + emprestimo.usuario.nome + ' - ' + emprestimo.dataEmprestimo.dataInicial.strftime(
                    "%d/%m/%Y") + ' - ' + emprestimo.dataEmprestimo.dataFinal.strftime("%d/%m/%Y")
                lista_emprestimos.append(emprestimo_info)
        else:
            lista_emprestimos.append('Nenhum emprestimo cadastrado.')
        self.__tela_emprestimo.lista_emprestimos = lista_emprestimos

    def renova_emprestimo(self, titulo_livro, nome_usuario):
        dados_validos = self.valida_dados(nome_usuario)

        if dados_validos:
            emprestimo_existente = self.retornaEmprestimo(titulo_livro, nome_usuario)
            if emprestimo_existente:
                emprestimo_existente.dataEmprestimo.dataFinal = emprestimo_existente.dataEmprestimo.dataFinal + td(
                    days=7)
                self.__emprestimoDAO.add(emprestimo_existente)
                self.retorna_notificacao('Empréstimo renovado para mais 7 dias!')
            else:
                self.retorna_notificacao('Esse empréstimo ainda não foi criado.')
        else:
            self.retorna_notificacao('Digite um nome válido')

    def retornaEmprestimo(self, titulo_livro, nome_usuario):
        emprestimo = self.__emprestimoDAO.get(titulo_livro + nome_usuario)
        if emprestimo is not None:
            return emprestimo
        return False

    def exclui_emprestimo(self, titulo_livro, nome_usuario):
        dados_validos = self.valida_dados(nome_usuario)

        if dados_validos:
            emprestimo_existente = self.retornaEmprestimo(titulo_livro, nome_usuario)
            if emprestimo_existente:
                self.__emprestimoDAO.remove(emprestimo_existente)
                self.retorna_notificacao('Empréstimo exluído com sucesso.')
            else:
                self.retorna_notificacao('Esse empréstimo não existe!')
        else:
            self.retorna_notificacao('Digite um nome válido')

    def abre_tela(self):
        while True:
            self.lista_emprestimos()
            dict_emprestimo = self.__tela_emprestimo.tela_opcoes()
            opcao = dict_emprestimo['opcao']
            values = dict_emprestimo['values']

            if opcao == 'Incluir':
                self.inclui_emprestimo(values[1], values[2])
            elif opcao == 'Renovar':
                self.renova_emprestimo(values[1], values[2])
            elif opcao == 'Excluir':
                self.exclui_emprestimo(values[1], values[2])
            else:
                self.retorna_notificacao('Escolha uma opção')
                break
