class Cachorro:
    def __init__(self, cor, nome, acordado=True):
        print('inicializando a classe')  # sempre sera inicializado primeiro 
        self.cor = cor
        self.nome = nome
        self.acordado = acordado

    def __del__(self):
        print('Removendo a instancia da classe')

    def latir(self):
        print('Au au')

    
dog = Cachorro('Branco', 'Laika')
dog.latir()


dog2 = Cachorro('Preto', 'Lila')
dog2.latir()