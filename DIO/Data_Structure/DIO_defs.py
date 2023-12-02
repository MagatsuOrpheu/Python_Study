"""
def exibir_mensagem():
    print('Ola Mundo!')

def exibir_mensagem2(nome):
    print(f'Ola {nome}')

def exibir_mensagem3(nome='Anonimo'):
    print(f"Ola {nome}")


exibir_mensagem()
exibir_mensagem2('Jonathan')
exibir_mensagem3()         

def calcular_soma(numeros):
    return sum(numeros)

def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func():
    print("ola mundo")



print(calcular_soma([1,2,3,4,5,6,7,5,1]))
print(retorna_antecessor_sucessor(20))
"""

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()} : {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    return mensagem


"""print(exibir_poema(
    'Sunday, 26th november, 2023',
    'Aqui vai a linha 1',
    'Aqui vai a linha 2',
    'Aqui vai a linha 3',
    'Aqui vai a linha 4',
    'Aqui vai a linha 5',
    'Aqui vai a linha 6',
    'Aqui vai a linha 7',
    autor='Jonathan',
    data='2023',
))"""

# Positional only
"""
def carro(modelo, ano, placa, /, marca, motor, combustivel): # arguments before the slash are positional only
    print(modelo, ano, placa, marca, motor, combustivel)


carro('Supra MK 4', '1998', 'ABCD1234', marca='Toyota', motor='2-JZ-GTE', combustivel='Gasolina')
carro(modelo='Supra MK 4', ano='1998', placa='ABCD1234', marca='Toyota', motor='2-JZ-GTE', combustivel='Gasolina')  # return Error
"""


# keyword only
"""
def carro(*, modelo, ano, placa, marca, motor, combustivel): # All keyword must be used
    print(modelo, ano, placa, marca, motor, combustivel)

carro(modelo='Supra MK 5', ano='2017', placa='EFGH9876', marca='Toyota', motor='XXXX', combustivel='Gasolina')
carro('Supra MK 5', ano='2017', placa='EFGH9876', marca='Toyota', motor='XXXX', combustivel='Gasolina')  # Return error 
"""

# positional and keyword
"""def carro(modelo, ano, placa,/,*, marca, motor, combustivel): # All keyword must be used
    print(modelo, ano, placa, marca, motor, combustivel)

carro('Supra MK 4', '1998', 'ABCD1234', marca='Toyota', motor='2-JZ-GTE', combustivel='Gasolina') # Right
carro('Supra MK 4', '1998', 'ABCD1234', 'Toyota', motor='2-JZ-GTE', combustivel='Gasolina') # Wrong
carro('Supra MK 4', '1998', placa='ABCD1234', marca='Toyota', motor='2-JZ-GTE', combustivel='Gasolina') # Wrong
"""

"""
def somar(a,b):
    return a+b

def multiplicar(a,b):
    return a*b

def subtrair(a,b):
    return a-b

def operacao(a, b, funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operacao é: {resultado}")


operacao(10,10,somar)
operacao(10,10,multiplicar)
operacao(10,10,subtrair)
"""

# global 
salario = 2000

def bonus_salario(bonus):
    global salario
    salario += bonus
    return salario

print(bonus_salario(500))