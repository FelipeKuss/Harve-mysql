import mysql.connector

conn = mysql.connector.connect (
    user='root',
    password='root',
    host='127.0.0.1',
    database='meu',
    port='3307'
)

print("Este é um jogo de pedra, papel ou tesoura")
print("Por favor insira seu nome:")
nome_jogador = input()

print("Insira a sua jogada (PEDRA,PAPEL,TESOURA):")
jogador = input()
computador = "Pedra"
if jogador == computador:
    resultado = 'Empate'
elif jogador == 'PAPEL':
    resultado = 'VITÓRIA'
else:
    resultado = 'Derrota'
    
print(resultado)
    
cursor = conn.cursor()

query = f"""
    INSERT INTO contagem_jogos
        (nome_player,jogada_player,jogada_computador,resultado)
    VALUES
        ('{nome_jogador}','{jogador}','{computador}','{resultado[0]}')
"""


cursor.execute(query)
conn.commit()
cursor.close()
