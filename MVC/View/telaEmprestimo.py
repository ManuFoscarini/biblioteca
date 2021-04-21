from MVC.View.tela import Tela


class TelaEmprestimo(Tela):
  def __init__(self, controlador):
    super().__init__(controlador)

  def tela_opcoes(self):
    print("-------- Emprestimos ----------")
    print("Escolha a opcao")
    print("1 - Incluir Emprestimo")
    print("2 - Renovar Emprestimo")
    print("3 - Relatório de Emprestimos")
    print("4 - Excluir Emprestimo")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_emprestimo(self):
    print("-------- INCLUIR EMPRESTIMO ----------")
    titulo = input("Título do livro: ")

    continua = True
    while continua:
      usuario = input("Nome de quem irá emprestá-lo: ")
      continua = any(char.isdigit() for char in usuario) or len(usuario) < 2
      if continua:
        print('Digite um nome válido')

    return {"tituloLivro": titulo, "nomeUsuario": usuario}

  def pega_titulo_exclusao(self):
    print("-------- EXCLUIR EMPRESTIMO ----------")
    titulo = input("Título do livro que deseja excluir: ")
    return titulo


  def mostra_emprestimo(self, dados_emprestimo):
    print('O livro emprestado é: %s' %(dados_emprestimo["tituloLivro"]))
    print('Quem emprestou foi: %s' %(dados_emprestimo["nomeUsuario"]))
    print('A data do emprestimo é: ' + dados_emprestimo['dataInicial'].strftime("%d/%m/%Y"))
    print('A data do fim do emprestimo é: ' + dados_emprestimo['dataFinal'].strftime("%d/%m/%Y"))
    print('E a o status do emprestimo é: %s' %(dados_emprestimo["status"]))
