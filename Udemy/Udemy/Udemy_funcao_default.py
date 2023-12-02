"""
Funções com parâmetro Default

- A passagem de parâmetro é opcional
"""

"""
def potenciacao(numero=0, potencia=2): # Os parâmetros são passados na definição da funcao
    return numero ** potencia


print(potenciacao(4))
print(potenciacao(4, 3))
print(potenciacao(4, 4))
print(potenciacao())
"""

"""
def potenciacao(numero=0, potencia):  # Os default devem estar sempre na direita, depois dos parâmetros obrigatórios
    return numero ** potencia


print(potenciacao(2))
"""

"""
def boas_vindas(user=None, login=False):
    if user is None and not login:
        return 'Usuário não logado.'
    elif user is None and login:
        return "Bem vindo novo usúario, vamos fazer o seu cadastro!"
    else:
        login = True
        return f"Bem vindo {user}!"


print(boas_vindas(login=True))
"""

"""
Usando uma função como parâmetro

def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def math(num1, num2, fun=soma):
    return fun(num1, num2)


print(soma(2, 2))
print(subtracao(4, 2))
print(math(8, 4, subtracao))
"""


"""
Variaveis locais tem mais prioridade que as globais

nome = 'Alan'

def pessoa():
    nome = 'Gabriel'
    return f"Oi {nome}!"


print(pessoa())
"""