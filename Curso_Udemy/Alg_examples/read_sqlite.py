import sqlite3

conn = sqlite3.connect('J:/Trilha JS/DB/database_test.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM fornecedor")
resultado = cursor.fetchall()

print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)

resultado[:2]

for linha in resultado:
    print(linha)

cursor.close()
conn.close()
