from MVC.Model.DAO.DAO import DAO
from MVC.Model.professor import Professor


class ProfessorDAO(DAO):
    def __init__(self):
        super().__init__('professor.pkl')

    def add(self, professor: Professor):
        if (isinstance(professor.nome, str)) and (professor is not None):
            super().add(professor.nome + '1', professor)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key + '1')

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key + '1')
