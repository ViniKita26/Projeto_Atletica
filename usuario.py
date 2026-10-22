
class Usuario:
    def __init__(self, nome, matricula, tipo):
        self.nome = nome
        self.matricula = matricula
        self.tipo = tipo
        self.itens_emprestados = []
        self.historico = []

    def limite_itens(self):
        return 0

    def pode_pegar(self):
        return len(self.itens_emprestados) < self.limite_itens()


class Estudante(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula, "Estudante")

    def limite_itens(self):
        return 2  # Limite de 2 itens para estudantes


class Servidor(Usuario):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula, "Servidor")

    def limite_itens(self):
        return 4  # Limite de 4 itens para servidores
