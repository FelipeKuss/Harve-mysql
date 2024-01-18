import mysql.connector

conn = mysql.connector.connect (
    user='root',
    password='root',
    host='127.0.0.1',
    database='meu',
    port='3307'
)

CREATE TABLE meu.contagem_jogos (
nome_player 		VARCHAR(20),
jogada_player 		VARCHAR(10),
jogada_computador 	VARCHAR(10),
flag_vitoria		VARCHAR(1),
data_registro		DATETIME DEFAULT CURRENT_TIMESTAMP()

);


INSERT INTO contagem_jogos (nome_player,jogada_player,jogada_computador,flag_vitoria)
VALUES ('Jogador','Pedra','Pedra','E')
;


cursor = conn.cursor()
cursor.execute("SELECT * FROM contagem_jogos")
row = cursor.fetchall()
print(row)

