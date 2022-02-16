CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT,
    nome VARCHAR(10) NOT NULL,
    midnome VARCHAR(10) DEFAULT NULL,
    sobrenome VARCHAR(10) NOT NULL,
    username VARCHAR(10) NOT NULL UNIQUE,
    email VARCHAR(16) NOT NULL,
    senha VARCHAR(16) NOT NULL,
    PRIMARY KEY (id)
)  DEFAULT CHARSET=UTF8;

SELECT 
    *
FROM
    usuarios;

alter table usuarios
add column info text after username;

insert into usuarios values
(default, 'alex', 'giovani', 'hirsch', 'alex4gtx', 'olá mundo!', 'alexgiovani35@gmail.com', '96301324alex.');