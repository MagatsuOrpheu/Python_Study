from abc import ABC, abstractclassmethod

class ControleRemoto(ABC):
    @abstractclassmethod
    def ligar(self):
        pass

    @abstractclassmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")

    def desligar(self):
        print('Desligando a TV...')


class ControleAr(ControleRemoto):
    def ligar(self):
        print('Ligando o Ar...')

    def desligar(self):
        print('Desligando o Ar...')


controle = ControleTV()
controle.ligar()
controle.desligar()

ar = ControleAr()
ar.ligar()
ar.desligar()