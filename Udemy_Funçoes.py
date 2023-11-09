"""
Funções são trechos do código que realizam tarefas especificas, e podem ser reutilizados
Ex:
- Print()
- Len()
- max()
- min()
- count()

- Podem receber entradas de dados e retornar saidas;
- Usadas para executar procedimentos similares repetidas vezes;

Para definir a função utilizamos a seguinte sintaxe:
    def nome_da_funcao():
        bloco da funcao


Para fazer a chamada da funcao digitamos seu nome, seguido de parenteses.
nome_da_funcao()



def dizer_oi():
    print("Oi!")


# Exemplo 2
for n in range(5):
    dizer_oi()


def dizer_tchau():
    print("Tchau!")


despedida = dizer_tchau

despedida()
"""

"""
RETORNO DE FUNÇÕES
numeros = [1,2,3]

ret_pop = numeros.pop()

print(f'Retorno do pop: {ret_pop}')

ret_pr = print(numeros)

print(f"Retorno de print: {ret_pr}")
"""

"""
def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()
print(f"retorno de quadrado de 7: {ret}")
print(f"Retorno de quadrado de 7: {quadrado_de_7()}")

# Não é necessário criar uma variavel para guardar o retorno de ret
"""


# def diz_oi():
#     return 'Oi!'
#
#
# def diz_oi_2():
#     print('Oi')
#
#
# alguem = ' Pedro'
#
# print(diz_oi() + alguem)
# # print(diz_oi_2() + alguem) # <- aqui irá gerar erro


"""
O return fecha a função
"""

"""
O return sai da função
# def abc():
#     print('A')
#     print('B')
#     return 'Paramos aqui'
#     print('C')
#     print('D')


# print(abc())
"""

"""
# Uma função pode ter diversos return
def variavel_func():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3
    return 2


print(variavel_func())
"""

"""
Return pode retornar varios valores
def outra_func():
    return 2,3,4,5


num1, num2, num3, num4 = outra_func()
print(num1, num2, num3, num4)
"""

# Criar uma função de jogar moeda
from random import random


def jogar_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(jogar_moeda())
