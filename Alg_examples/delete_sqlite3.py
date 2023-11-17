import sqlite3

conn = sqlite3.connect('J:/Trilha JS/DB/database_test.db')
cursor = conn.cursor()

cursor.execute('DELETE FROM fornecedor WHERE id_fornecedor = 2')
conn.commit()

cursor.execute("SELECT * FROM fornecedor")
resultado = cursor.fetchall()
for linha in resultado:
    print(linha)
