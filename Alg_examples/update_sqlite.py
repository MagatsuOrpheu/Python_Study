import sqlite3

conn = sqlite3.connect('J:/Trilha JS/DB/database_test.db')
cursor = conn.cursor()

cursor.execute(
    "UPDATE fornecedor SET cidade = 'Campinas' WHERE id_fornecedor= 1")
conn.commit()

cursor.execute('SELECT * FROM fornecedor')
for linha in cursor.fetchall():
    print(linha)
