class Passaro():
    def voar(self):
        print('Estou voando')

class Pardal(Passaro):
    def voar(self):
        super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print('Nao posso voar')


def plano_de_voo(objeto):
    objeto.voar()


avestruz = Avestruz()
pardal = Pardal()


plano_de_voo(pardal)
plano_de_voo(avestruz)