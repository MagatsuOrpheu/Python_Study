class Estudantes:
    aula = 'Quimica'  # <- variavel de classe

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
         return f"{self.nome} - ({self.matricula}) : {self.aula}"
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudantes('Jonathan', 1)
aluno_2 = Estudantes('Fernanda', 2)
mostrar_valores(aluno_1, aluno_2)

print('===============================')

Estudantes.aula = 'Matematica'
aluno_3 = Estudantes('Pedrinho', 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)

print('===============================')

aluno_2.matricula = 4  # Metodo de instancia do objeto
mostrar_valores(aluno_1, aluno_2, aluno_3)