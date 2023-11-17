########### Condicionais em Python ###########
"""
  Estruturas condicionais em Python
  Ex: IF, ELIF, ELSE

        idade = 8

        if idade < 18:
            print("Menor de idade")
        elif idade == 18:
            print("Idade igual a 18")
        else:
            print("Maior de idade")
"""

########### Estruturas Logicas em Python ###########
"""
  Estruturas Logicas em Python
  Ex: And (E), Or (Ou), Not (Não), Is (é)  

AND = Os valores precisam ambos estar como True
OR = Qualquer um dos dois valores precisam estar como True 
"""


"""
ativo = True
logado = False

if ativo and logado:
    print("Bem vindo Usuário!")
elif ativo:
    print("Você precisa ativar a sua conta. Por favor cheque o seu email.")
elif logado:
    print("Sua conta foi suspendida por violar algumas politicas da comunidade. Para mais informações, consulte a aba de dúvidas.")
else:
    print("O usuário não se encontra ativo e/ou logado.")
"""


"""
# NOT = O valor do booleano é invertido
desligado = False

if not desligado:
    print("Você precisa ligar o computador")
"""


"""
# IS = Confirma um booleano {Ex: Ativo is True = ativo é True ?}
resposta = True
if resposta is True:
    print("A resposta é Verdadeira")
else:s
    print("A resposta é Falsa")
"""


"""
ativo = True
logado = True
if ativo is True:
    print(not ativo)
else:
    print(not ativo)
"""


# ATIVO É TRUE ?
ativo = False
print(ativo is True)
