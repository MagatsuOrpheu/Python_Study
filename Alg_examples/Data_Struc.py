# Tipos sequenciais = String
texto = 'Esse é um texto exemplo para testar sequências'


def teste_sequencia01():
    print(f"Tamanho do texto: {len(texto)}")
    print(f"Existe Jonathan no texto: {'Jonathan' in texto}")
    print(f"Não existe Jonathan no texto: {'Jonathan' not in texto}")

    # ELE DIFERENCIA LETRAS COM SIMBOLOS (É, Ê, È, ETC)
    print(f"Quantos E's existem no texto ? {texto.count('e')}")

    # COMEÇA SEMPRE NO ZERO
    print(f"10 primeiras letras: {texto[0:20]}")

    print(texto.upper())
    print(texto.lower())
    print(texto.replace('e', '@'))
    texto_cut = texto.split()
    print(texto_cut)
    print(len(texto_cut))

    texto2 = """Operadores de String
    Python oferece operadores para processar texto (ou seja, valores de string).
    Assim como os números, as strings podem ser comparadas usando operadores de comparação:
    ==, !=, <, > e assim por diante.
    O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016).
    """
    # O texto necessita receber ele mesmo
    texto2 = texto2.lower()
    texto2 = texto2.replace(":", "").replace("=", "").replace("(", "").replace(
        ")", "").replace(".", "").replace("!", "").replace("<", "").replace(">", "").replace(",", "")
    texto_f = texto2.split()

    print(
        f"Vezes em que a palavra string foi dita: {texto2.count('string' or 'strings')}")
    print(len(texto_f))


def Listas():
    lista01 = [1, 2, 3, 4, 5]
    lista02 = ['aco', 'maça', 'banana', 'uva', 'pera']
    lista03 = []
    lista04 = ['existente']

    print(f"Maça esta na lista01 ? {'maça' in lista01}")
    print(f"Maça esta na lista02 ? {'maça' in lista02}")

    print(f"Minimo da lista (MAIUSCULAS VEM PRIMEIRO): {min(lista02)}")

    print(f"Tamanho da lista: {len(lista02)}")

    # Posso concatenar duas listas em uma só
    lista03 = (lista02 + lista01)
    print(lista03)

    # Entretanto ao usar append, ele coloca a lista inteira (com colchetes)
    lista04.append(lista01)
    print(lista04)


def fatiamento():
    lista01 = list(range(0, 30))
    print(lista01)

    for i, data in enumerate(lista01):
        print(f"Indice: {i} ----> Dado: {data}")
        if i > 10:
            print(". \n. \n.")
            break

    print(f"Tamanho da lista: {len(lista01)}")

    print('Exemplos de slice:')
    print(f"Slice [0:2]: {lista01[0:2]}")
    print(f"Slice [2:4]: {lista01[2:4]}")
    # O 6 dado não existe, mas não é retornado um erro
    print(f"Slice [2:6]: {lista01[2:6]}")
    print(f"Slice [:4]: {lista01[:4]}")
    print(f"Slice [4:26:2]: {lista01[4:26:2]}")
    print(f"Slice [::2]: {lista01[::2]}")


def fatiamento2():
    lista02 = [1, 2, 3, 4, 5, 6, 'Jonathan', [7, 8, 9, 10, 11]]

    print(f"Slice de lista dentro de outra lista: {lista02[7][3]}")


def list_comprehension():
    linguagens = ['galinha', 'pena', 'hamster', 'rato']
    # print(linguagens)
    linguagens2 = 'A B C D E'.split()

    bichos_com_o = [item for item in linguagens if "o" in item]

    print(f"Se algum dado tiver a letra 'O' print: {bichos_com_o}")

    print(f'Antes da list_comp: {linguagens2}')
    linguagens2 = [item.lower() for item in linguagens2]
    print(f'Depois da list_comp: {linguagens2}')


def list_comprehension2():
    lista_nomes = ['JONATHAN', 'MELO', 'SOUZA', 'VICTORIA']

    nova_lista = map(lambda x: x.lower(), lista_nomes)
    print(f"Essa é a nova lista {nova_lista}")
    # É preciso transformar um map em lista após a operação
    nova_lista = list(nova_lista)
    print(f"Ops, essa é a nova lista: {nova_lista}")


def filter_list():
    ListaNumbers = list(range(0, 41))
    pares = list(filter(lambda x: x % 2 == 0, ListaNumbers))
    print(f"Numeros pares: {pares}")


def tuplas():
    vogais = ('a', 'e', 'i', 'o', 'u')
    print(type(vogais))

    print(tuple(enumerate(vogais)))
    print(list(enumerate(vogais)))


def sets():
    componentes_verificados = set(['caixas de som', 'cooler', 'dissipador de calor', 'cpu', 'hd', 'estabilizador', 'gabinete', 'hub', 'impressora', 'joystick', 'memória ram',
                                  'microfone', 'modem', 'monitor', 'mouse', 'no-break', 'placa de captura', 'placa de som', 'placa de vídeo', 'placa mãe', 'scanner', 'teclado', 'webcam'])
    componentes_defeito = set(['cooler', 'microfone', 'placa mãe', 'joystick'])

    print(f"Componentes verificados: {len(componentes_verificados)}")
    print(f"Componentes defeituosos: {len(componentes_defeito)}")

    componentes_ok = componentes_verificados.difference(componentes_defeito)
    # OU
    componentes_ok = componentes_verificados - componentes_defeito

    print(f"Possiveis componentes a venda: {len(componentes_ok)}")

    for item in componentes_ok:
        print(item)


def dictionary():
    dici01 = {'Nome': 'João', 'Idade': '20'}
    dici02 = dict([('Nome', 'João'), ('Idade', '20')])
    dici03 = {}
    dici03['Nome'] = 'João'
    dici03['Idade'] = '20'
    print(f'Dicionario 1: {dici01}')
    print(type(dici01))
    print(f'Dicionario 2: {dici02}')
    print(type(dici02))
    print(f'Dicionario 3: {dici03}')
    print(type(dici03))

    print(dici01 == dici02 == dici03)


def dictionary2():
    Dados = {
        'Nome': ['João', 'Pedro', 'Jonathan', 'Bianca'],
        'Cidade': ['Campinas', 'São Paulo', 'Valinhos'],
        'Idade': [20, 18, 30, 15, 99]
    }
    print(f'Length Dados: {len(Dados)}')

    print(f'Dados [Nome]:', Dados['Nome'])
    print(f'Dados [Nome][2]:', Dados['Nome'][2])
    print(f'Dados [Idade]:', Dados['Idade'][:2])

    qtd_chaves = sum([len(Dados[chave]) for chave in Dados])
    print(f"Soma do valor das chaves: {qtd_chaves}")


"""
    print("Dados.keys() =", Dados.keys())
    print("Dados.values() =", Dados.values())
    print("Dados.items() =", Dados.items())
"""
