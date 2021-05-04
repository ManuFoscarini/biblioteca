from MVC.Model.DAO.DAO import DAO
from MVC.Model.professor import Professor


class ProfessorDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, professor: Professor):
        if (isinstance(professor.nome, str)) and (professor is not None):
            super().add(professor.nome, Professor)

    # def add(self, alunos):
    #     super().add('alunos', alunos)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)