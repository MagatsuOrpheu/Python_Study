# Criar uma função que converte a data numérico para extenso
# Create a function to convert day.
"""
data = input("Digite uma data (Ex: 01/01/2000): ")
data = data.split('/')
try:
    dia = int(data.pop(0))
    mes = data.pop(0)
    ano = data.pop()


    def convert_date(day, month, year):
        if day <= 31:
            if month == '01':
                month = 'Janeiro'
                return f"Data: {day} de {month} de {year}"
            elif month == '02':
                if day > 29:
                    return "Digite uma data válida"
                month = 'Fevereiro'
                return f"Data: {day} de {month} de {year}"
            elif month == '03':
                month = 'Março'
                return f"Data: {day} de {month} de {year}"
            elif month == '04':
                month = 'Abril'
                return f"Data: {day} de {month} de {year}"
            elif month == '05':
                month = 'Maio'
                return f"Data: {day} de {month} de {year}"
            elif month == '06':
                month = 'Junho'
                return f"Data: {day} de {month} de {year}"
            elif month == '07':
                month = 'Julho'
                return f"Data: {day} de {month} de {year}"
            elif month == '08':
                month = 'Agosto'
                return f"Data: {day} de {month} de {year}"
            elif month == '09':
                month = 'Setembro'
                return f"Data: {day} de {month} de {year}"
            elif month == '10':
                month = 'Outubro'
                return f"Data: {day} de {month} de {year}"
            elif month == '11':
                month = 'Novembro'
                return f"Data: {day} de {month} de {year}"
            elif month == '12':
                month = 'Dezembro'
                return f"Data: {day} de {month} de {year}"
            else:
                return "Digite uma data válida"
        else:
            return "Digite uma data válida"


    print(convert_date(dia, mes, ano))

except ValueError:
    print("Somente datas são aceitos")
"""

# Criar uma função que verifique se o número digitado é um quadrado perfeito
# Create a function to verify if the number is a perfect square
"""
number = int(input('Digite um numero para verificar se é um quadrado perfeito: '))


def perfect_square(number):
    raiz_q = int(number ** (1 / 2))
    if (raiz_q ** 2) == number:
        print(f"{number} é um quadrado perfeito!")
    else:
        print(f"{number} não é um quadrado perfeito")


perfect_square(number)
"""