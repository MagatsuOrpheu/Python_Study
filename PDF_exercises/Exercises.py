
# Faça o programa receber dois numeros e dizer qual deles é maior

def exercise_01():
    num1 = input('Digite um numero: ')
    num2 = input('Digite um numero: ')

    if num1 > num2:
        print(f"{num1} é maior que {num2}")
    else:
        print(f"{num2} é maior que {num1}")


# Leia um numero fornecido pelo usuário e mostre a raiz quadrada do mesmo. se caso elee for negativo, diga que o numero é invalido.

def exercise_02():
    import math
    x = int(input('Digite um numero: '))

    if x > 0:
        print(math.sqrt(x))
    else:
        print('O numero digitado é invalido.')


# Leia um numero real. se o numero for positivo, imprima a raiz quadrada. caso contrario, imprima o mesmo ao quadrado.

def exercise_03():
    import math
    x = int(input('Digite um numero: '))

    if x > 0:
        print(math.sqrt(x))
    else:
        print(x**2)


# faça um programa que verifique se o numero digitado é impar ou par, caso positivo.

def exercise_04():
    x = int(input('Digite um numero: '))

    if (x % 2) == 0:
        print('Este numero é par')
    else:
        print('Este numero é impar')


# Faca um programa que receba duas notas, verifique se as notas são validas, e exiba a media entre elas.

def exercise_05():
    x = float(input('Digite a primeira nota: '))

    if x >= 0 and x <= 10:
        y = float(input('Digite a segunda nota: '))
        if y >= 0 and y <= 10:
            media = (x + y) / 2
            print(f'A media das notas é de {media}')
        else:
            print('Nota invalida')
    else:
        print('Nota invalida')


# Faça um programa que leia o salario de um trabalhador e uma parcela de um emprestimo. se a parcela for maior que 20% do salario, o emprestimo não é concedido

def exercise_06():
    salario = float(input('Digite o salario do trabalhador: '))
    prestacao = float(input('Digite o valor da prestação: '))
    um_Quinto = (salario - (salario * 0.8))

    if prestacao > um_Quinto:
        print('Emprestimo não concedido.')
    else:
        print('Emprestimo concedido.')


# Faça um programa que recebe o sexo e a altura de uma pessoa e calcule o seu peso ideal

def exercise_07():
    sexo = input('Informe o seu sexo (M/F): ')
    altura = float(input('Informe a sua altura: '))

    if sexo == 'M':
        peso_Ideal = (72.7 * altura) - 58
        print("%.2f" % peso_Ideal)
    else:
        peso_Ideal = (62.1 * altura) - 44.7
        print("%.2f" % peso_Ideal)


# Faça um programa que leia um numero maior que zero e devolva a soma de seus algarismos (IE: 268 = 2+6+8)

def exercise_08():
    soma = 0
    x = input('Digite um numero: ')
    x.split()
    soma = int(x[0]) + int(x[1]) + int(x[2])
    print(soma)


# Faça um programa que leia um numero que calcule o log de numeros positivos, e nos informe que o numero é negativo (caso seja)

def exercise_09():
    import math
    x = int(input('Digite um numero: '))

    if (x > 0):
        print(math.log(x))
    else:
        print('Numero inválido')


# Faça um programa que calcule as 3 notas de um aluno, com pesos 2, 3 e 5 respectivamente.

def exercise_10():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    media = (nota1 * 2) + (nota2 * 3) + (nota3 * 5) / 10

    if (media < 2.9):
        print('Aluno foi reprovado')
    elif (media > 3 and 4.9):
        print('Aluno ficou de recuperação')
    else:
        print('Aluno passou')


# Faça um programa que leia um numero inteiro de 1 a 7, e diga qual dia da semana é baseado no numero.

def trocar_Dia_Da_Semana(x):
    switcher = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado'
    }
    return switcher.get(x, "Número Invalido")


# x = int(input('Digite um numero entre 1 e 7: '))
# print(trocar_Dia_Da_Semana(x))


# Faça um programa que mostre as opções de calculadora e faça a operação.

def exercise_12():
    print('( Soma )')
    print('( Subtração )')
    print('( Divisão )')
    print('( Multiplicação )')
    operacao = input('Selecione uma das 4 operações acima: ')

    if (operacao == 'Soma'):
        x = int(input('Digite o primeiro numero: '))
        y = int(input('Digite o segundo numero: '))
        print(f"{x} + {y} = {x + y}")
    elif (operacao == 'Subtração'):
        x = int(input('Digite o primeiro numero: '))
        y = int(input('Digite o segundo numero: '))
        print(f'{x} - {y} = {x - y}')
    elif (operacao == 'Divisão'):
        x = int(input('Digite o primeiro numero: '))
        y = int(input('Digite o segundo numero: '))
        print(f"{x} / {y} = {x / y}")
    else:
        x = int(input('Digite o primeiro numero: '))
        y = int(input('Digite o segundo numero: '))
        print(f"{x} X {y} = {x * y}")


exercise_12()
