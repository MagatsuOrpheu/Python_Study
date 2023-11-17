import sqlite3

conn = sqlite3.connect('J:/Trilha JS/DB/database_test.db')
print(type(conn))

ddl_create = """
CREATE TABLE fornecedor (
    id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_fornecedor TEXT NOT NULL,
    cnpj VARCHAR(18),
    cidade TEXT,
    estado VARCHAR(2) NOT NULL,
    cep VARCHAR(9) NOT NULL,
    data_cadastro DATE NOT NULL
);
"""

cursor = conn.cursor()
cursor.execute(ddl_create)
print(type(cursor))

print("Tabela Criada!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)
cursor.close()
conn.close()
