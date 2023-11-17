# O objetivo do programa é criar um algoritmo que possa calcular e nos retornar o Indice de Massa Corpórea de um indivíduo.
# O calculo de IMC é: Peso / Altura ^ 2

# Nesta linha é feita a criação da função "calcular_imc", a qual contém o cálculo do IMC em sí, além do bloco de código que será responsavel por informar ao usuário qual o status do IMC do mesmo.
def calcular_imc(peso, altura):

    if altura > 5.0:
        altura = altura / 100
    # Aqui é criado a variavel IMC, e atribuido a ela o resultado da equação para calcular o IMC
    imc = peso / altura ** 2

    # Nas proximas linhas é feito a analise de qual a classificação do IMC resultante dos dados inseridos:
    if imc < 18.5:  # Se o resultado for menor que 18.5 o resultado é "Abaixo do peso"
        class_imc = ("Abaixo do peso")
    elif 18.5 <= imc <= 24.9:  # Se o resultado for menor que 25 o resultado é "Peso normal"
        class_imc = ("Peso normal")
    elif 25 <= imc <= 29.9:  # Se o resultado for menor que 30 o resultado é "acima do peso"
        class_imc = ("Acima do peso")
    elif 30 <= imc < 34.9:  # Se o resultado for menor que 34.9 o resultado é "Obesidade I"
        class_imc = ("Obesidade I")
    else:           # Se o resultado for menor que 34.9 o resultado é "Obesidade II"
        class_imc = ("Obesidade II")

    print(f"IMC: {imc:.2f} \nConsiderado: {class_imc}")


def testar_calculo():

    # Pedimos que o usuario digite o seu peso para atribuir a variavel "peso"
    peso = float(input("Insira seu peso(EX: 90.5): "))

    # Pedimos que o usuario digite o seu peso para atribuir a variavel "altura"
    altura = float(input("Insira sua altura(EX: 1.75): "))

    calcular_imc(peso, altura)


testar_calculo()
