class bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro


    def buzinar(self):
        print('plim plimm')

    
    def correr(self):
        print('Correndo..')


    def parar(self):
        print('Parando..')


    def __str__(self):
        return f" {self.__class__.__name__}:{', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    
    
    def listar_objeto(listar):
        print(listar)



bike1 = bicicleta('Vermelha', 'Caloi', 2010, 1340.00, 18)
bike2 =bicicleta('Azul', 'Monark', 1999, 1000.00, 20)

# print(bike1.cor, bike1.modelo, bike1.ano, bike1.valor)
# bike1.buzinar()
# bike1.correr()
# bike1.parar()
# bicicleta.buzinar(bike1)  # é equivalente à b1.buzinar()
# bicicleta.buzinar(bike2)  # é equivalente à b2.buzinar()
# print(bike1.__str__())

bike1.listar_objeto()