CREATE DATABASE usuario;

CREATE TABLE dados(
id SERIAL PRIMARAY KEY,
nome VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
criado_em TIMESTAMP DEFAULT NOW()
)

INSERT INTO dados(nome, email)
VALUES('Ana Silva', 'felixnetoximenes@gmail.com')

INSERT INTO dados (nome, emial)
VALUES('felix', 'ximenes@gmail.com')

SELECT * FROM dados