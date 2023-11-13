# Aqui vamos testar a criação e funcionamento das classes

class Saudacao:  # Criamos a nossa classe

    def imprimir_mensagem(self, name):  # Criamos um método para ela
        print(f"Olá {name}! como vai?")


objeto1 = Saudacao()  # instanciamos um objeto com essa classe
# objeto1.imprimir_mensagem('Jonathan') # invocando o objeto


# ================================================== #

class Calculadora:

    def somar(self, n1, n2):
        return n1 + n2

    def subtrair(self, n1, n2):
        return n1 - n2

    def multiplicar(self, n1, n2):
        return n1 * n2

    def divisão(self, n1, n2):
        return n1 / n2

    def dividir_resto(self, n1, n2):
        return n1 % n2


calc = Calculadora()
# print(f"Soma: {calc.somar(5,5)}")
# print(f"Subtracao: {calc.subtrair(100,50)}")

# ==================================================== #


class Televisao:

    def __init__(self):  # Aqui determinamos um estado inicial para a variavel volume dentro da nossa classe
        self.volume = 10

    def aumentar_volume(self):
        # criamos um atributo de instancia (são capazes de receber um valor diferente)
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1


# TV = Televisao()
# print(f'Volume atual da TV: {TV.volume}')
# TV.aumentar_volume()
# print(f"VOlume atual da TV: {TV.volume}")


class Dogs:

    tipo = 'Cachorro'

    def __init__(self, nome):
        self.nome = nome


dog1 = Dogs('Lili')
dog2 = Dogs('Marcos')

# print(dog1.tipo)  # Aqui vemos que o tipo é universal para a classe Dogs
# print(dog2.tipo)  # Aqui vemos que o tipo é universal para a classe Dogs

# print(dog1.nome)  # Mas aqui o nome é individual, pois é uma variavel de instancia
# print(dog2.nome)  # Mas aqui o nome é individual, pois é uma variavel de instancia

# =================================================== #

""" HERANÇA ENTRE CLASSES """


class Pessoa:

    def __init__(self):
        self.cpf = None
        self.nome = None
        self.idade = None


class funcionario(Pessoa):

    def __init__(self):
        self.matricula = None
        self.salario = None

    def bater_ponto(self):
        self.horario = None
        self.data = None


class cliente(Pessoa):

    def __init__(self):
        self.cadastro = None


f1 = funcionario()
f1.nome = 'Jonathan'
f1.cpf = '010101'

# print(f'Esse é o funcionario {f1.nome}, seu cpf é {f1.cpf}')


class int99(int):

    def __init__(self, n):
        int.__init__(n)

    def __add__(a, b):
        return 99

    def __str__(n):
        return '99'


"""
a = int99(22)
b = int99(5)
print(a + b)
print(a)
print(b)

c = int(9)
d = int(1)
print(c + d)
print(c)
print(d)
"""

# ================================================= #
# TESTE DE CLASSES RPG #


class Elf:

    def __init__(self, nome, cidade):
        self.nome = None
        self.cidade = None


class Dwarf:

    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade


class Orc:

    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade


class Knight:

    def __init__(self, forca, destreza, inteligencia):
        self.forca = forca
        self.destreza = destreza
        self.inteligencia = inteligencia


class Archer:

    def __init__(self, forca, destreza, inteligencia):
        self.forca = forca
        self.destreza = destreza
        self.inteligencia = inteligencia


class Barbarian:

    def __init__(self, forca, destreza, inteligencia):
        self.forca = forca
        self.destreza = destreza
        self.inteligencia = inteligencia


class Char1(Dwarf, Knight):
    def __init__(self, nome, cidade, forca, destreza, inteligencia):
        Dwarf.__init__(self, nome, cidade)
        Knight.__init__(self, forca, destreza, inteligencia)


class Char2(Orc, Barbarian):
    def __init__(self, nome, cidade, forca, destreza, inteligencia):
        Orc.__init__(self, nome, cidade)
        Barbarian.__init__(self, forca, destreza, inteligencia)


class Char3(Elf, Archer):
    def __init__(self, nome, cidade, forca, destreza, inteligencia):
        Elf.__init__(self, nome, cidade)
        Archer.__init__(self, forca, destreza, inteligencia)


""" 
torin = Char3('Torin', 'Mordor', 0, 0, 0)

if isinstance(torin, Knight):
    char_str = 13
    char_dex = 7
    char_int = 5
elif isinstance(torin, Barbarian):
    char_str = 15
    char_dex = 5
    char_int = 5
else:
    char_str = 5
    char_dex = 5
    char_int = 15

torin.forca = char_str
torin.destreza = char_dex
torin.inteligencia = char_int

print(f"Meu nome é {torin.nome}, vim de {torin.cidade}")
print(
    f"Meus atributos são: \nForça = {torin.forca}\nDestreza = {torin.destreza}\ninteligencia = {torin.inteligencia}")
"""

# =============================================================== #


class Elf:

    def __init__(self, nome, cidade):
        self.nome = None
        self.cidade = None


class Dwarf:

    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade


class Orc:

    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade


class Knight:

    def __init__(self, forca, destreza, inteligencia):
        self.forca = forca
        self.destreza = destreza
        self.inteligencia = inteligencia


class Archer:

    def __init__(self, forca, destreza, inteligencia):
        self.forca = forca
        self.destreza = destreza
        self.inteligencia = inteligencia


class Barbarian:

    def __init__(self, forca, destreza, inteligencia):
        self.forca = forca
        self.destreza = destreza
        self.inteligencia = inteligencia


class Char1(Dwarf, Knight):
    def __init__(self, nome, cidade, forca, destreza, inteligencia):
        Dwarf.__init__(self, nome, cidade)
        Knight.__init__(self, forca, destreza, inteligencia)


class Char2(Orc, Barbarian):
    def __init__(self, nome, cidade, forca, destreza, inteligencia):
        Orc.__init__(self, nome, cidade)
        Barbarian.__init__(self, forca, destreza, inteligencia)


class Char3(Elf, Archer):
    def __init__(self, nome, cidade, forca, destreza, inteligencia):
        Elf.__init__(self, nome, cidade)
        Archer.__init__(self, forca, destreza, inteligencia)


Personagem1 = Char1('Torin', 'Mordor', 10, 10, 10)

# print(f"Char1 é um, Knight ? {isinstance(Personagem1, Knight)}")
# print(f"Char1 é um, Archer ? {isinstance(Personagem1, Archer)}")


# ================================================ #

class Conta_Corrente:

    def __init__(self, nome):
        self.nome = nome
        self.email = None
        self.telefone = None
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    def _checar_saldo(self, valor):
        # Vai checar se o valor que tem na conta é maior que VALOR, se sim, retornará true
        return self._saldo >= valor

    def sacar(self, valor):
        # Se o valor que está na conta é maior que VALOR, então será feito o saque
        if self._checar_saldo(valor):
            self._saldo -= valor
            return True
        else:
            return False

    def obter_saldo(self):
        return self._saldo  # retornará o saldo da conta


class contaPF(Conta_Corrente):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf

    def solicitar_emprestimo(self, valor):
        return self.obter_saldo() >= 500


class contaPJ(Conta_Corrente):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj

    # Se o empréstimo requisitado for menor que 5000 será feito o empréstimo
    def sacar_emprestimo(self, valor):
        return valor <= 5000


"""
PessoaFisica1 = contaPF("Jonathan", '111.111.111-11')
PessoaFisica1.depositar(1000)
print(f'Seu saldo atual é = {PessoaFisica1.obter_saldo()}')
print(f'Recebera emprestimo = {PessoaFisica1.solicitar_emprestimo(2000)}')


PessoaFisica1.sacar(800)
print(f'Saldo atual é = {PessoaFisica1.obter_saldo()}')
print(f'Receberá empréstimo = {PessoaFisica1.solicitar_emprestimo(2000)}')
"""

Conta_CNPJ = contaPJ('Empresa A', '11.111.111/1111-11')
print(f'Saldo atual é = {Conta_CNPJ.obter_saldo()}')
print(f'Recebera emprestimo = {Conta_CNPJ.sacar_emprestimo(3000)}')
