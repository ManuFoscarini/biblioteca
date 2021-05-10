import datetime

from MVC.Model.DAO.professorDAO import ProfessorDAO
from MVC.View.telaAluno import TelaAluno
from MVC.View.telaProfessor import TelaProfessor
from MVC.Model.aluno import Aluno
from MVC.Model.professor import Professor
from MVC.Model.DAO.alunoDAO import AlunoDAO
from MVC.Model.Exceções.customExceptions import *


class ControladorUsuario():

    def __init__(self, ctrlBiblioteca):
        self.__ctrlBiblioteca = ctrlBiblioteca
        self.__telaProfessor = TelaProfessor(self)
        self.__telaAluno = TelaAluno(self)
        self.__alunoDAO = AlunoDAO()
        self.__professorDAO = ProfessorDAO()

    def retorna_notificacao_tela_professor(self, mensagem):
        self.__telaProfessor.texto_acao = mensagem

    def retorna_notificacao_tela_aluno(self, mensagem):
        self.__telaAluno.texto_acao = mensagem

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
            self.retorna_notificacao_tela_aluno('Aluno incluído com sucesso!')

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
        self.__telaAluno.lista_usuarios = lista_alunos

    def altera_aluno(self, nome, telefone, email, data_nascimento, ano_atual):
        dados_validos = self.valida_dados(nome, telefone, email, data_nascimento, ano_atual)

        aluno_existe = self.retornaUsuario(nome, 'aluno')
        if aluno_existe:
            self.__alunoDAO.add(
                Aluno(nome, telefone, email, dados_validos['data_nascimento'], dados_validos['ano_atual']))
            self.retorna_notificacao_tela_aluno('Aluno alterado com sucesso!')
        else:
            raise UsuarioNaoExisteExeption

    def exclui_aluno(self, nome):
        self.valida_nome(nome)

        aluno_existe = self.retornaUsuario(nome, 'aluno')
        if aluno_existe:
            self.__alunoDAO.remove(aluno_existe.nome)
            self.retorna_notificacao_tela_aluno("Aluno exluído com sucesso.")
        else:
            raise UsuarioNaoExisteExeption

    # Professor
    def incluir_professor(self, nome, telefone, email, data_nascimento, ano_atual):
        dados_validos = self.valida_dados(nome, telefone, email, data_nascimento, ano_atual)
        print('tentou incluir e dados validos')
        professor_existe = self.retornaUsuario(nome, 'professor')
        if professor_existe:
            print('professor já existe baiano')
            raise UsuarioJaExisteExeption
        else:
            print('incluiu')
            self.__professorDAO.add(
                Professor(nome, telefone, email, dados_validos['data_nascimento'], dados_validos['ano_atual']))
            self.retorna_notificacao_tela_professor('Professor incluído com sucesso!')

    def lista_professores(self):
        professor_dict_value = self.__professorDAO.get_all()
        lista_professores = []
        if len(professor_dict_value) > 0:
            for professor in professor_dict_value:
                lista_professores.append(
                    professor.nome + ' - ' + professor.telefone + ' - ' + professor.email + ' - ' + professor.data_nascimento.strftime(
                        "%d/%m/%Y") + ' - ' + str(professor.ano_atual))
        else:
            lista_professores.append('Nenhum professor cadastrado.')
        self.__telaProfessor.lista_usuarios = lista_professores

    def exclui_professor(self, nome):
        self.valida_nome(nome)

        professor_existe = self.retornaUsuario(nome, 'professor')
        if professor_existe:
            self.__professorDAO.remove(professor_existe.nome)
            self.retorna_notificacao_tela_professor("Professor exluído com sucesso.")
        else:
            raise UsuarioNaoExisteExeption

    def altera_professor(self, nome, telefone, email, data_nascimento, ano_atual):
        dados_validos = self.valida_dados(nome, telefone, email, data_nascimento, ano_atual)

        professor_existe = self.retornaUsuario(nome, 'professor')
        if professor_existe:
            self.__professorDAO.add(
                Professor(nome, telefone, email, dados_validos['data_nascimento'], dados_validos['ano_atual']))
            self.retorna_notificacao_tela_professor('Professor alterado com sucesso!')
        else:
            raise UsuarioNaoExisteExeption

    def abre_tela_professor(self):
        while True:
            self.lista_professores()
            dict_usuario = self.__telaProfessor.tela_opcoes()
            opcao = dict_usuario['opcao']
            values = dict_usuario['values']

            if opcao == 'Incluir':
                try:
                    self.incluir_professor(values[1], values[2], values[3], values[4], values[5])
                except (InvalidNameError, UsuarioJaExisteExeption, InvalidPhoneNumberError) as error:
                    if error is InvalidNameError:
                        self.retorna_notificacao_tela_professor(
                            'Digite um nome válido, com no mínimo dois caracteres (apenas letras)')
                    elif error is UsuarioJaExisteExeption:
                        self.retorna_notificacao_tela_professor(
                            'Esse professor já existe, tente alterá-lo')
                    elif error is InvalidPhoneNumberError:
                        self.retorna_notificacao_tela_professor(
                            'Digite um telefone válido, composto de exatamente 11 digitos numéricos')
                    elif error is InvalidEmailError():
                        self.retorna_notificacao_tela_professor(
                            'Digite um e-mail válido, contendo "@" e "."')
                    elif error is InvalidDateError():
                        self.retorna_notificacao_tela_professor(
                            'Digite uma data válida, no formato "DD/MM/YYYY"')
                    elif error is InvalidYearError():
                        self.retorna_notificacao_tela_professor(
                            'Digite um ano válido, composto de exatamente 4 digitos numéricos')
                    else:
                        self.retorna_notificacao_tela_professor(
                            'Não foi possível incluir este professor')
            elif opcao == 'Alterar':
                try:
                    self.altera_professor(values[1], values[2], values[3], values[4], values[5])
                except (InvalidNameError, UsuarioJaExisteExeption, InvalidPhoneNumberError) as e:
                    print('entrou nas exceptions')
                    if e is InvalidNameError:
                        self.retorna_notificacao_tela_professor(
                            'Digite um nome válido, com no mínimo dois caracteres (apenas letras)')
                    elif e is UsuarioNaoExisteExeption:
                        self.retorna_notificacao_tela_professor('Esse professor não existe!')
                    elif e is InvalidPhoneNumberError:
                        self.retorna_notificacao_tela_professor(
                            'Digite um telefone válido, composto de exatamente 11 digitos numéricos')
                    elif e is InvalidEmailError():
                        self.retorna_notificacao_tela_professor(
                            'Digite um e-mail válido, contendo "@" e "."')
                    elif e is InvalidDateError():
                        self.retorna_notificacao_tela_professor(
                            'Digite uma data válida, no formato "DD/MM/YYYY"')
                    elif e is InvalidYearError():
                        self.retorna_notificacao_tela_professor(
                            'Digite um ano válido, composto de exatamente 4 digitos numéricos')
                    else:
                        self.retorna_notificacao_tela_professor(
                            'Não foi possível alterar este professor')
            elif opcao == 'Excluir':
                try:
                    self.exclui_professor(values[1])
                except (InvalidNameError, UsuarioNaoExisteExeption) as e:
                    if e is InvalidNameError:
                        self.retorna_notificacao_tela_professor(
                            'Digite um nome válido, com no mínimo dois caracteres (apenas letras)')
                    elif e is UsuarioNaoExisteExeption:
                        self.retorna_notificacao_tela_professor('Esse professor não existe!')
                    else:
                        self.retorna_notificacao_tela_professor(
                            'Não foi possível excluir este professor')
            else:
                break

    def abre_tela_aluno(self):
        while True:
            self.lista_alunos()
            dict_usuario = self.__telaAluno.tela_opcoes()
            opcao = dict_usuario['opcao']
            values = dict_usuario['values']

            if opcao == 'Incluir':
                try:
                    self.incluir_aluno(values[1], values[2], values[3], values[4], values[5])
                except (InvalidNameError, UsuarioJaExisteExeption, InvalidPhoneNumberError) as error:
                    if error is InvalidNameError:
                        self.retorna_notificacao_tela_aluno(
                            'Digite um nome válido, com no mínimo dois caracteres (apenas letras)')
                    elif error is UsuarioJaExisteExeption:
                        self.retorna_notificacao_tela_aluno(
                            'Esse aluno já existe, tente alterá-lo')
                    elif error is InvalidPhoneNumberError:
                        self.retorna_notificacao_tela_aluno(
                            'Digite um telefone válido, composto de exatamente 11 digitos numéricos')
                    elif error is InvalidEmailError():
                        self.retorna_notificacao_tela_aluno(
                            'Digite um e-mail válido, contendo "@" e "."')
                    elif error is InvalidDateError():
                        self.retorna_notificacao_tela_aluno(
                            'Digite uma data válida, no formato "DD/MM/YYYY"')
                    elif error is InvalidYearError():
                        self.retorna_notificacao_tela_aluno(
                            'Digite um ano válido, composto de exatamente 4 digitos numéricos')
                    else:
                        self.retorna_notificacao_tela_aluno(
                            'Não foi possível incluir este aluno')
            elif opcao == 'Alterar':
                try:
                    self.altera_aluno(values[1], values[2], values[3], values[4], values[5])
                except (InvalidNameError, UsuarioJaExisteExeption, InvalidPhoneNumberError) as e:
                    if e is InvalidNameError:
                        self.retorna_notificacao_tela_aluno(
                            'Digite um nome válido, com no mínimo dois caracteres (apenas letras)')
                    elif e is UsuarioNaoExisteExeption:
                        self.retorna_notificacao_tela_aluno('Esse aluno não existe!')
                    elif e is InvalidPhoneNumberError:
                        self.retorna_notificacao_tela_aluno(
                            'Digite um telefone válido, composto de exatamente 11 digitos numéricos')
                    elif e is InvalidEmailError():
                        self.retorna_notificacao_tela_aluno(
                            'Digite um e-mail válido, contendo "@" e "."')
                    elif e is InvalidDateError():
                        self.retorna_notificacao_tela_aluno(
                            'Digite uma data válida, no formato "DD/MM/YYYY"')
                    elif e is InvalidYearError():
                        self.retorna_notificacao_tela_aluno(
                            'Digite um ano válido, composto de exatamente 4 digitos numéricos')
                    else:
                        self.retorna_notificacao_tela_aluno(
                            'Não foi possível alterar este aluno')
            elif opcao == 'Excluir':
                try:
                    self.exclui_aluno(values[1])
                except (InvalidNameError, UsuarioNaoExisteExeption) as e:
                    if e is InvalidNameError:
                        self.retorna_notificacao_tela_aluno(
                            'Digite um nome válido, com no mínimo dois caracteres (apenas letras)')
                    elif e is UsuarioNaoExisteExeption:
                        self.retorna_notificacao_tela_aluno('Esse aluno não existe!')
                    else:
                        self.retorna_notificacao_tela_aluno(
                            'Não foi possível excluir este aluno')
            else:
                break
