class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas
    
    def __str__(self):
        return f"{self.__class__.__name__} = {', '.join([f'{chave}:{valor}' for chave, valor in self.__dict__.items()])}"
    

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)
        


class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)


class falarMixin:
    def falar(self):
        return "Oi, estou falando"



class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave, falarMixin):
    def __init__(self, cor_pelo, nmr_patas, cor_bico):
        print(Ornitorrinco.mro())  # retorna a ordem em que o script vai percorrer

        super().__init__(cor_pelo=cor_pelo,nmr_patas=nmr_patas,cor_bico=cor_bico) 


gato = Gato(nmr_patas = 4, cor_pelo='Preto')
ornitorrinco = Ornitorrinco(nmr_patas= 4, cor_pelo="Vermelho", cor_bico = 'Azul')

print(ornitorrinco)
print(gato)
print(ornitorrinco.falar())