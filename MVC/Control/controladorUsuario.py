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
        dia, mes, ano = map(int, '25/01/2001'.split('/'))
        data_nascimento = datetime.date(ano, mes, dia)
        self.__alunoDAO.add(Aluno('Manu', '99999999999', 'manu@.', data_nascimento, 2021))
        self.lista_alunos()

    def valida_dados(self, nome, telefone, email, data_nascimento, ano_atual):
        pass

    def incluir_aluno(self, nome, telefone, email, data_nascimento, ano_atual):
        #nome_aluno = self.__telaUsuario.pega_nome('Aluno')
        dados_validos = self.valida_dados(nome, telefone, email, data_nascimento, ano_atual)
        if dados_validos:
            aluno_existe = self.retornaUsuario(nome, 'aluno')

            if aluno_existe:
                raise UsuarioJaExisteExeption
            else:
                self.__alunoDAO.add(Aluno(nome, telefone, email, data_nascimento, ano_atual))
        #else:
            #raise DadosInvalidoUsuario

    def lista_alunos(self):
        alunos_dict_value = self.__alunoDAO.get_all()
        lista_alunos = []
        if len(alunos_dict_value) > 0:
            for aluno in alunos_dict_value:
                self.__telaUsuario.mostra_usuario({"Nome": aluno.nome, "Telefone": aluno.telefone, 'Email': aluno.email,
                                                   'Data de nascimento': aluno.data_nascimento,
                                                   'Ano atual': aluno.ano_atual}, 'Aluno')
        else:
            print('Nenhum aluno cadastrado.')
        self.__telaUsuario.lista_alunos = lista_alunos

    def retornaUsuario(self, nome, tipo='ambos'):
        if tipo != 'professor':
            aluno = self.__alunoDAO.get(nome)
            if aluno is not None:
                return aluno
        if tipo != 'aluno':
            for professor in self.__professores:
                if professor.nome == nome:
                    return professor
        return False

    def altera_aluno(self):
        print('Insira o nome do aluno que gostaria de alterar.')
        nome_aluno = self.__telaUsuario.pega_nome('Aluno')
        aluno_existe = self.retornaUsuario(nome_aluno['Nome'], 'aluno')

        if aluno_existe:
            dados_aluno = self.__telaUsuario.pega_dados_usuario()
            aluno_alterar = aluno_existe

            aluno_alterar.nome = nome_aluno["Nome"]
            aluno_alterar.telefone = dados_aluno["Telefone"]
            aluno_alterar.email = dados_aluno['Email']
            aluno_alterar.data_nascimento = dados_aluno['Data de nascimento']
            aluno_alterar.ano_atual = dados_aluno['Ano atual']

            self.__alunoDAO.add(aluno_alterar)

            print("Aluno alterado com sucesso.")
        else:
            print("Esse aluno não existe!")

    def exclui_aluno(self):
        print('Insira o nome do aluno que gostaria de excluir.')
        nome_aluno = self.__telaUsuario.pega_nome('Aluno')
        aluno_existe = self.retornaUsuario(nome_aluno['Nome'], 'aluno')

        if aluno_existe:
            self.__alunoDAO.remove(aluno_existe.nome)
            print("Aluno exluído com sucesso.")
        else:
            print("Esse aluno não existe!")

    # Professor
    def incluir_professor(self):
        nome_professor = self.__telaUsuario.pega_nome('Professor')
        professor_existe = self.retornaUsuario(nome_professor['Nome'], 'professor')

        if professor_existe:
            raise UsuarioJaExisteExeption
        else:
            dados_professor = self.__telaUsuario.pega_dados_usuario()
            self.__professorDAO.add(Professor(nome_professor["Nome"], dados_professor["Telefone"], dados_professor['Email'],
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
        dict_usuario = self.__telaUsuario.tela_opcoes()
        opcao = dict_usuario['opcao']
        print(opcao)
        values = dict_usuario['values']
        print(values)
        if opcao == 'Incluir':
            if values[0] == True:
                self.incluir_aluno(values[3], values[4], values[5], values[6], values[7])
        else:
            self.__telaUsuario.fecha_tela()

    # def abre_tela(self):
    #     while True:
    #         opcao = self.__telaUsuario.tela_opcoes()
    #         if opcao == 1:
    #             try:
    #                 self.incluir_aluno()
    #             except UsuarioJaExisteExeption:
    #                 return('Esse aluno já existe.')
    #         elif opcao == 2:
    #             self.altera_aluno()
    #         elif opcao == 3:
    #             self.lista_alunos()
    #         # elif opcao == 4:
    #         #     self.exclui_aluno()
    #         elif opcao == 5:
    #             try:
    #                 self.incluir_professor()
    #             except UsuarioJaExisteExeption:
    #                 return('Esse professor já existe.')
    #         elif opcao == 6:
    #             self.altera_professor()
    #         elif opcao == 7:
    #             self.lista_professores()
    #         elif opcao == 8:
    #             self.exclui_professor()
    #         elif opcao == 4:
    #             self.__telaUsuario.fecha_tela()