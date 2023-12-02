class Veiculos:
    def __init__(self, cor, placa, nmr_rodas):
        self.cor = cor
        self.placa = placa
        self.nmr_rodas = nmr_rodas

    def ligar_motor(self):
        print(f'{self.__class__.__name__} = Ligando motor')


    def __str__(self):
        return self.cor


class Motocicleta(Veiculos):
    def __init__(self, cor, placa, nmr_rodas):
        super().__init__(cor, placa, nmr_rodas)



class Carro(Veiculos):
    pass


class Caminhao(Veiculos):
    def __init__(self, cor, placa, nmr_rodas, carregado):
        super().__init__(cor, placa, nmr_rodas)
        self.carregado = carregado
        

    def esta_carregado(self):
        print(f'{"Sim" if self.carregado else "Nao"} estou carregado')



# carro = Carro('Preto', 'NFS-1234', 4)
# carro.ligar_motor()
# carro.carregar_bau() # Nao possui a funcao e retorna erro

"""caminhao = Caminhao('Azul', 'JQK-5432', 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)"""

moto = Motocicleta('Vermelha', 'KZM-9989', 2)
moto.ligar_motor()
