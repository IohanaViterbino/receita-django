# exemplo 1 de classe

from typing import Any


class Exemplo:
    def __init__(self, a=2, b=3):
        self.a = a
        self.b = b
    
    def f(self, x) -> int:
        return self.a*x + self.b
    
obj = Exemplo()
print(obj.f(2))

# exemplo 2 de classe
class Aluno:
    def __init__(self, nome, matricula, curso) -> None:
        self.nome=nome
        self.matricula=matricula
        self.curso=curso
        print("construindo um objeto", self.__class__.__name__)

    def falar(self):
        return f"{self.nome.upper()} ESTÁ FALANDO...."
    
aluno1 = Aluno("Maria", "a974125", "python fullstack")

print(aluno1.falar())

# exemplo 3
class Pessoa:
    nome: str
    idade: int

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getAnoNascimento(self, anoAtual):
        return anoAtual - self.idade
    
pessoa1 = Pessoa("iohana", 21)
print(pessoa1.getAnoNascimento(2024))