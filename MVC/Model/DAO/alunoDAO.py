from MVC.Model.DAO.DAO import DAO
from MVC.Model.aluno import Aluno


class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, aluno: Aluno):
        if (isinstance(aluno.nome, str)) and (aluno is not None):
            super().add(aluno.nome + '0', aluno)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key + '0')

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key + '0')
