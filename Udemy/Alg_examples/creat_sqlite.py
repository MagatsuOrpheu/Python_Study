import sqlite3

conn = sqlite3.connect('J:/Trilha JS/DB/database_test.db')
cursor = conn.cursor()

metodo_01 = (
    # cursor.execute("""
    # INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro) VALUES ('CPFL', '11.111.111/1111-11', 'São Paulo', 'SP', '11111-111', '2023-23-23')
    # """)

    # cursor.execute("""
    # INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro) VALUES ('ANEEL', '22.222.222/2222-22', 'São Paulo', 'SP', '22222-222', '2023-23-23')
    # """)

    # cursor.execute("""
    # INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro) VALUES ('ENEL', '33.333.333/3333-33', 'São Paulo', 'SP', '33333-333', '2023-23-23')
    # """)

    # cursor.execute("""
    # INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro) VALUES ('EMPRESA 2', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2023-23-23')
    # """)

    # conn.commit()

    # print("Dados inseridos!")
    # print("Descrição do cursor: ", cursor.description)
    # print("Linhas afetadas: ", cursor.rowcount)
    # cursor.close()
    # conn.close()
)

# metodo_02 (adicionando uma GRANDE quantidade)
dados = [
    ('Empresa D', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2023-23-23'),
    ('Empresa E', '54.544.544/5444-54', 'Brasilia', 'DF', '66666-666', '2023-23-23')
    # ETC...
]

cursor.executemany("""
INSERT INTO fornecedor(nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro) VALUES (?, ?, ?, ?, ?, ?)""", dados)

conn.commit()


cursor.close()
conn.close()
