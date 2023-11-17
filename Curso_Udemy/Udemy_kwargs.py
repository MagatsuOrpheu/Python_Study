"""
**kwargs

pode ser nomeado como quiser tambem, mas por convenção é chamado de kwargs.
- É um parametro como o args.
- Diferente do args que coloca os valores em uma tupla, o kwargs utiliza-se de parametros nomeados, e transforma em um
dicionario.
"""


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


# cores_favoritas(Jonathan='Preto', gabriel='Azul', Larissa='Vermelho', paulo='cinza', Fernanda='Rosa')
# cores_favoritas()
# cores_favoritas(Fernanda='Rosa')


def serie_favorita(**kwargs):
    for key in kwargs:
        if 'Jonathan' in kwargs and kwargs['Jonathan'] == 'The Office':
            return f"Você tem um bom gosto Jonathan"
        elif 'Jonathan' in kwargs:
            return f"Olá Jonathan!"
        else:
            return "Olá amigo!"


"""
print(serie_favorita(Leticia='Friends'))
print(serie_favorita(Jonathan='The Office', Leticia='Friends'))
print(serie_favorita(Jonathan='Sherlock', Leticia='Friends'))
"""

"""
Existe uma ordem dos parâmetros que podemos seguir:
- Parametros obrigatorios
- *args
- Parametros default
- **kwargs

Veja exemplo:

"""

"""
def nova_funcao(nome, idade, *args, solteiro=False, **kwargs):
    print(f"Usuario: {nome.title()} - Idade: {idade}")
    print(f"Args: {args}")
    if solteiro:
        print("Solteiro")
    else:
        print("Casado")
    print(f"Kwargs: {kwargs}")
    print("_________________________")


nova_funcao('Jonathan', 21, 2, 3, 4, 5, 'teste', Comida='Lasanha')
nova_funcao('Fernanda', 21, solteiro=True, Escola='Bento Quirino')
nova_funcao('Larissa', 21, 'teste')
"""

"""
# Desempacotar com Kwargs
def show_names(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Jonathan', 'sobrenome': 'Melo'}

print(show_names(**nomes))
"""


def soma_nums(a, b, c):
    print(a + b + c)
