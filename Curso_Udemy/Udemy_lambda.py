"""
Lambdas são funções anonimas, sem nome

Função em python:
    def soma(a, b):
        return a + b


# Exemplos expressão lambda - Incomum

calc = lambda x: 3 * x + 1

print(calc(3))

# Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' Jonathan', ' Gabriel '))
print(nome_completo(' Jonathan', ' MELO                        '))



autores = ['Isaac_Asimov', 'Stephen_King', 'H.P_Lovecraft', 'Rick_Riordan', 'Miyamoto_Musashi']

autores.sort(key=lambda sobrenome: sobrenome.split('_')[1].lower())

print(autores)
"""

# gerador de função quadrática


def gerador_funcao_quadratica(a, b, c):
    """
    Retorna uma função quadratica
    :param a: a
    :param b: b
    :param c: c
    """
    return lambda x: a * x ** 2 + (b * x) + c


bala_1 = gerador_funcao_quadratica(2, 3, -5)

print(bala_1(1))


