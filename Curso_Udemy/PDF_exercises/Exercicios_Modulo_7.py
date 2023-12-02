"""
1 - Um vetor chamado A que armazene 6 numeros
A) atribua ao vetor os numeros: 1, 0, 5, -2, -5, 7.
B) Armazene em uma variavel a soma das posições A[0], A[1] e A[5]
C) Modifique o vetor na posição 4, atribuindo o valor 100
D) Mostre na tela cada valor do vetor A, um em cada linha

A = [1, 0, 5, -2, -5, 7]
--
Soma = A[0] + A[1] + A[5]
print(Soma)
--
A[4] = 100
print(A)
--
for numero in A:
    print(numero)
"""  # Exercicio 1

"""
Crie um programa que leia 6 valores inteiros e imprima os na tela
"""

A = [0]*6
for numero in A:
    A = input(f"Digite um numero: ")

for numero in A:
    print(f"Numero = {numero}")
