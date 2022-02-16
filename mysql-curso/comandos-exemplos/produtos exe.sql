create database `produtos`
default character set `utf8`
default collate `utf8_general_ci`;

use `produtos`;
CREATE TABLE `jogos` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nome` VARCHAR(40) NOT NULL,
    `fabricante` VARCHAR(20) NOT NULL,
    `ano` DATE NOT NULL,
    gênero VARCHAR(10) NOT NULL,
    preço DECIMAL(5 , 3 ),
    plataforma ENUM('PC', 'PS4', 'XBOX'),
    estoque TINYINT(4),
    PRIMARY KEY (id)
)  DEFAULT CHARSET=UTF8;
