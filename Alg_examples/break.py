# Serve para forçar o programa a sair de um loop, de maneira planejada

for numero in range(1, 10):
    if numero == 6:
        break
    else:
        print(numero)
print('Estou fora do loop')


while True:
    resposta = input("Digite 'sair' para sair: ")
    if resposta == 'sair':
        break
print('Saiu')
