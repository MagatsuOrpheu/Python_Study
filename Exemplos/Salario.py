salario = float(input("Digite o salario inicial: "))
aumento = float(input("Digite quantos porcento de aumento: "))
newSalario = salario + (salario/100 * aumento)

print(f"Resposta: {newSalario}")