class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade


    @classmethod
    def criar_a_partir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2023 - ano
        return Pessoa(nome,idade)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_a_partir_data_nascimento(2002,10,3,'Jonathan')
print(p.nome, p.idade)


print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(7))