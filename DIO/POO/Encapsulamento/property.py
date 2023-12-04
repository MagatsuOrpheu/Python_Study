"""class Foo():

    def __init__(self, x=None):
        self._x = x
        

    @property
    def x(self):
        return self._x or 1000
    
    @x.setter
    def x(self, valor):
        _x = self._x or 0
        _valor = valor or 0
        self._x = _x + _valor

    @x.deleter
    def x(self):
        self._x = -1



foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)

"""


class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento


    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        ano_atual = 2023
        return ano_atual - self._ano_nascimento
    



jonathan = Pessoa('Jonathan', 2002)

print(f"Pessoa: {jonathan.nome}, Idade: {jonathan.idade}")