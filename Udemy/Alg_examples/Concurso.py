premio = float(input("Qual o valor do premio: "))
primeiro = float(input("Quantos porcentos o primeiro irá ganhar: "))
segundo = float(input("Quantos porcentos o segundo irá ganhar: "))
terceiro = float(input("Quantos porcentos o terceiro irá ganhar: "))

primeiro_premio = (premio / 100) * primeiro
segundo_premio = (premio / 100) * segundo
terceiro_premio = premio - (primeiro_premio + segundo_premio)
print(primeiro_premio)
print(segundo_premio)
print(terceiro_premio)
