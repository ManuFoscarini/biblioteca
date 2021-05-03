from DAO import DAO

class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    # def add(self, aluno: Aluno):
    #     if (isinstance(aluno.nome, str)) and (aluno is not None):  # and isinstance(aluno, Aluno):
    #         super().add(aluno.nome, Aluno)

    def add(self, alunos):
        super().add('alunos', alunos)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)
    
    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)