from MVC.Model.DAO.DAO import DAO
from MVC.Model.livro import Livro


class LivroDAO(DAO):
    def __init__(self):
        super().__init__('livro.pkl')

    def add(self, livro: Livro):
        if (isinstance(livro.titulo, str)) and (livro is not None):
            super().add(livro.titulo, livro)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)