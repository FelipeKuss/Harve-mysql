import mysql.connector

conn = mysql.connector.connect (
    user='root',
    password='root',
    host='127.0.0.1',
    database='meu',
    port='3307'
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM contagem_jogos")
row = cursor.fetchall()
print(row)

