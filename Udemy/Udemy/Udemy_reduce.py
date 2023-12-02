"""
Depois da versão 3 do Python, a funcao reduce não é mais integrada (built-in).
Agora a mesma deve ser importada para ser utilizada.
import functools

Guido Van Rossum: Utiliza a funcao reduce() somente quando você realmente precisar dela. Na maioria dos casos
utilize um loop for, que é mais legivel.

Imagine uma coleção de dados

dados = [a1, a2, a3,...., an]

voce tem uma funcao que recebe dois parametros.

def funcao(x, y):
    return x * y


a funcao reduce funcionada da seguinte forma:
(Assim como map e filter, a funcao reduce recebe dois parametros)

passo 1 : res1 = f(a1, a2) # Aplica a funcao nos dois primeiros elementos da coleção e guarda o resultado
passo 2: res2 = f(res1, a3) # Aplica a funcao passando o resultado anterior (res1) mais o terceiro elemento
isso é repetido até o final
passo 3: res3 = f(res2, a4)
.....
passo n: resn = f(resm, an)

no final, reduce ira retornar o resultado final.

alternativamente, podemos ver reduce como:
funcao(funcao(funcao(a1, a2), a3), a4),......an)

"""
from functools import reduce as rdc

dados = [1, 2, 3, 4, 5, 6, 7, 8]

# precisamos de uma funcao que recebe dois parametros

res = rdc(lambda x, y: x + y, dados)
print(res)


# utilizando loop for
res1 = 0
for n in dados:
    res1 = res1 + n

print(res1)
