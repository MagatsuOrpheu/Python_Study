Valor = float(input("Digite o valor do produto: "))
Desconto = float(input("Quantos porcento é o desconto (Desconsidere o simbolo de %): "))
Resultado = Valor - ((Valor / 100) * Desconto)

print(f"Resultado: {Resultado}")