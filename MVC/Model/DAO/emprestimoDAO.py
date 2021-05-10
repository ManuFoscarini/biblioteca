from MVC.Model.DAO.DAO import DAO
from MVC.Model.emprestimo import Emprestimo


class EmprestimoDAO(DAO):
    def __init__(self):
        super().__init__('emprestimo.pkl')

    def add(self, emprestimo: Emprestimo):
        if isinstance(emprestimo.usuario.nome, str) and isinstance(emprestimo.livro.titulo, str) and (emprestimo is not None):
            super().add(emprestimo.livro.titulo + emprestimo.usuario.nome, emprestimo)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, emprestimo: Emprestimo):
        if isinstance(emprestimo.usuario.nome, str) and isinstance(emprestimo.livro.titulo, str):
            return super().remove(emprestimo.livro.titulo + emprestimo.usuario.nome)