"""
Docstrings servem para documentar funções
Podemos ver utilizando a propriedade __doc__, ou com a função help(função)
"""


def diz_oi():
    """Aqui vai a descrição que vai ajudar a entender a função:
    Função que faz um print da palavra 'oi'"""
    print('Oi')


def soma(a, b):
    """
    Função que retorna a soma de dois numeros informados
    :param a: Numero A informado como argumento
    :param b: Numero B informado como argumento
    :return: Retorna a soma dos dois numeros informados
    """
    return a + b


print(help(soma))