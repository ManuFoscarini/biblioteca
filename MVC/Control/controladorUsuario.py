import datetime

from MVC.Model.DAO.professorDAO import ProfessorDAO
from MVC.View.telaUsuario import TelaUsuario
from MVC.Model.aluno import Aluno
from MVC.Model.professor import Professor
from MVC.Model.DAO.alunoDAO import AlunoDAO
from MVC.Model.Exceções.customExceptions import *


class ControladorUsuario():

    def __init__(self, ctrlBiblioteca):
        self.__ctrlBiblioteca = ctrlBiblioteca
        self.__professores = []
        self.__telaUsuario = TelaUsuario(self)
        self.__alunoDAO = AlunoDAO()
        self.__professorDAO = ProfessorDAO()

    def retorna_notificacao(self, mensagem):
        self.__telaUsuario.texto_acao = mensagem

    def retornaUsuario(self, nome, tipo='ambos'):
        if tipo != 'professor':
            aluno = self.__alunoDAO.get(nome)
            if aluno is not None:
                return aluno
        if tipo != 'aluno':
            professor = self.__professorDAO.get(nome)
            if professor is not None:
                return professor

    def valida_nome(self, nome):
        if any(char.isdigit() for char in nome) or len(nome) < 2:
            raise InvalidNameError()

    def valida_dados(self, nome, telefone, email, data_entrada, ano_entrada):

        self.valida_nome(nome)

        if not telefone.isdigit() or len(telefone) != 11:
            raise InvalidPhoneNumberError()

        if '@' not in email or '.' not in email:
            raise InvalidEmailError()

        try:
            dia, mes, ano = map(int, data_entrada.split('/'))
            data_nascimento = datetime.date(ano, mes, dia)
        except ValueError:
            raise InvalidDateError from ValueError

        try:
            ano_atual = int(ano_entrada)
            if len(ano_entrada) != 4:
                raise ValueError
        except ValueError:
            raise InvalidYearError from ValueError

        return {'data_nascimento': data_nascimento, 'ano_atual': ano_atual}

    def incluir_aluno(self, nome, telefone, email, data_nascimento, ano_atual):
        dados_validos = self.valida_dados(nome, telefone, email, data_nascimento, ano_atual)

        aluno_existe = self.retornaUsuario(nome, 'aluno')
        if aluno_existe:
            raise UsuarioJaExisteExeption
        else:
            self.__alunoDAO.add(
                Aluno(nome, telefone, email, dados_validos['data_nascimento'], dados_validos['ano_atual']))
            self.retorna_notificacao('Aluno incluído com sucesso!')

    def lista_alunos(self):
        alunos_dict_value = self.__alunoDAO.get_all()
        lista_alunos = []
        if len(alunos_dict_value) > 0:
            for aluno in alunos_dict_value:
                lista_alunos.append(
                    aluno.nome + ' - ' + aluno.telefone + ' - ' + aluno.email + ' - ' + aluno.data_nascimento.strftime(
                        "%d/%m/%Y") + ' - ' + str(aluno.ano_atual))
        else:
            lista_alunos.append('Nenhum aluno cadastrado.')
        self.__telaUsuario.lista_alunos = lista_alunos

    def altera_aluno(self, nome, telefone, email, data_nascimento, ano_atual):
        dados_validos = self.valida_dados(nome, telefone, email, data_nascimento, ano_atual)

        aluno_existe = self.retornaUsuario(nome, 'aluno')
        if aluno_existe:
            self.__alunoDAO.add(
                Aluno(nome, telefone, email, dados_validos['data_nascimento'], dados_validos['ano_atual']))
            self.retorna_notificacao('Aluno alterado com sucesso!')
        else:
            raise UsuarioNaoExisteExeption

    def exclui_aluno(self, nome):
        self.valida_nome(nome)

        aluno_existe = self.retornaUsuario(nome, 'aluno')
        if aluno_existe:
            self.__alunoDAO.remove(aluno_existe.nome)
            self.retorna_notificacao("Aluno exluído com sucesso.")
        else:
            raise UsuarioNaoExisteExeption

    # Professor
    def incluir_professor(self):
        nome_professor = self.__telaUsuario.pega_nome('Professor')
        professor_existe = self.retornaUsuario(nome_professor['Nome'], 'professor')

        if professor_existe:
            raise UsuarioJaExisteExeption
        else:
            dados_professor = self.__telaUsuario.pega_dados_usuario()
            self.__professorDAO.add(
                Professor(nome_professor["Nome"], dados_professor["Telefone"], dados_professor['Email'],
                          dados_professor['Data de nascimento'],
                          dados_professor['Ano atual']))

    def lista_professores(self):
        lista_professores = self.__professorDAO.get_all()
        if len(lista_professores) > 0:
            for professor in lista_professores:
                self.__telaUsuario.mostra_usuario(
                    {"Nome": professor.nome, "Telefone": professor.telefone, 'Email': professor.email,
                     'Data de nascimento': professor.data_nascimento, 'Ano atual': professor.ano_atual}, 'Professor')
        else:
            print('Nenhum professor cadastrado.')

    def exclui_professor(self):
        print('Insira o nome do professor que gostaria de excluir.')
        nome_professor = self.__telaUsuario.pega_nome('Professor')
        professor_existe = self.retornaUsuario(nome_professor['Nome'], 'professor')

        if professor_existe:
            self.__professorDAO.remove(professor_existe.nome)
            print("Professor exluído com sucesso.")
        else:
            print("Esse professor não existe!")

    def altera_professor(self):
        print('Insira o nome do professor que gostaria de alterar.')
        nome_professor = self.__telaUsuario.pega_nome('Professor')
        professor_existe = self.retornaUsuario(nome_professor['Nome'], 'professor')
        if professor_existe:
            dados_professor = self.__telaUsuario.pega_dados_usuario()
            professor_alterar = professor_existe

            professor_alterar.nome = nome_professor["Nome"]
            professor_alterar.telefone = dados_professor["Telefone"]
            professor_alterar.email = dados_professor['Email']
            professor_alterar.data_nascimento = dados_professor['Data de nascimento']
            professor_alterar.ano_atual = dados_professor['Ano atual']

            self.__professorDAO.add(professor_alterar)

            print("Professor alterado com sucesso.")
        else:
            print("Esse professor não existe!")

    def abre_tela(self):
        while True:
            self.lista_alunos()
            dict_usuario = self.__telaUsuario.tela_opcoes()
            opcao = dict_usuario['opcao']
            values = dict_usuario['values']

            if opcao == 'Incluir':
                try:
                    self.incluir_aluno(values[3], values[4], values[5], values[6], values[7])
                except (InvalidNameError, UsuarioJaExisteExeption, InvalidPhoneNumberError) as error:
                    if error == InvalidNameError:
                        self.retorna_notificacao(
                            'Digite um nome válido, com no mínimo dois caracteres (apenas letras)')
                    elif error is UsuarioJaExisteExeption:
                        self.retorna_notificacao(
                            'Esse aluno já existe, tente alterá-lo')
                    elif error is InvalidPhoneNumberError:
                        self.retorna_notificacao(
                            'Digite um telefone válido, composto de exatamente 11 digitos numéricos')
                    elif error is InvalidEmailError():
                        self.retorna_notificacao(
                            'Digite um e-mail válido, contendo "@" e "."')
                    elif error is InvalidDateError():
                        self.retorna_notificacao(
                            'Digite uma data válida, no formato "DD/MM/YYYY"')
                    elif error is InvalidYearError():
                        self.retorna_notificacao(
                            'Digite um ano válido, composto de exatamente 4 digitos numéricos')
                    else:
                        self.retorna_notificacao(
                            'Não foi possível incluir este aluno')
            elif opcao == 'Alterar':
                try:
                    self.altera_aluno(values[3], values[4], values[5], values[6], values[7])
                except (InvalidNameError, UsuarioJaExisteExeption, InvalidPhoneNumberError) as e:
                    print('entrou nas exceptions')
                    if e is InvalidNameError:
                        self.retorna_notificacao(
                            'Digite um nome válido, com no mínimo dois caracteres (apenas letras)')
                    elif e is UsuarioNaoExisteExeption:
                        self.retorna_notificacao('Esse aluno não existe!')
                    elif e is InvalidPhoneNumberError:
                        self.retorna_notificacao(
                            'Digite um telefone válido, composto de exatamente 11 digitos numéricos')
                    elif e is InvalidEmailError():
                        self.retorna_notificacao(
                            'Digite um e-mail válido, contendo "@" e "."')
                    elif e is InvalidDateError():
                        self.retorna_notificacao(
                            'Digite uma data válida, no formato "DD/MM/YYYY"')
                    elif e is InvalidYearError():
                        self.retorna_notificacao(
                            'Digite um ano válido, composto de exatamente 4 digitos numéricos')
                    else:
                        self.retorna_notificacao(
                            'Não foi possível alterar este aluno')
            elif opcao == 'Excluir':
                try:
                    self.exclui_aluno(values[3])
                except (InvalidNameError, UsuarioNaoExisteExeption) as e:
                    if e is InvalidNameError:
                        self.retorna_notificacao(
                            'Digite um nome válido, com no mínimo dois caracteres (apenas letras)')
                    elif e is UsuarioNaoExisteExeption:
                        self.retorna_notificacao('Esse aluno não existe!')
                    else:
                        self.retorna_notificacao(
                            'Não foi possível excluir este aluno')
            else:
                break
