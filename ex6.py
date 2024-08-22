class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __repr__(self):
        return f"Aluno(nome={self.nome}, cpf={self.cpf})"

class Equipe:
    def __init__(self, participantes, projeto):
        self.participantes = participantes  # Lista de objetos Aluno
        self.projeto = projeto

    def __repr__(self):
        return f"Equipe(participantes={self.participantes}, projeto={self.projeto})"

class GerenciadorEquipes:
    def __init__(self):
        self.equipes = []  # Lista de objetos Equipe

    def criarEquipe(self, novos_participantes, novo_projeto):
        # Verificar se algum dos novos participantes já está em uma equipe com o mesmo projeto
        for equipe in self.equipes:
            if equipe.projeto == novo_projeto:
                if any(aluno in equipe.participantes for aluno in novos_participantes):
                    print("Não é possível criar a equipe: algum aluno já está em uma equipe com o mesmo projeto.")
                    return

        # Se não houver conflitos, criar e adicionar a nova equipe
        nova_equipe = Equipe(novos_participantes, novo_projeto)
        self.equipes.append(nova_equipe)
        print("Equipe criada com sucesso!")

    def __repr__(self):
        return f"GerenciadorEquipes(equipes={self.equipes})"

# Exemplo de uso:
if __name__ == "__main__":
    aluno1 = Aluno("João", "12345678900")
    aluno2 = Aluno("Maria", "09876543211")
    aluno3 = Aluno("Pedro", "11122334455")
    
    gerenciador = GerenciadorEquipes()

    # Tentar criar uma nova equipe
    gerenciador.criarEquipe([aluno1, aluno2], "Projeto A")

    # Tentar criar uma equipe com aluno já em outra equipe com o mesmo projeto
    gerenciador.criarEquipe([aluno1, aluno3], "Projeto A")

    # Tentar criar uma equipe com um projeto diferente
    gerenciador.criarEquipe([aluno3], "Projeto B")

    print(gerenciador)
