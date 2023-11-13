salario = float(input("Digite quanto o trabalhador vai ganhar por dia: "))
dias = int(input("Quantos dias o trabalhador irá trabalhar: "))

salBruto = salario * float(dias)
salLiq = salBruto - (salBruto / 100 * 8)

print(f"O salario recebido será de: {salLiq}")