create database cadastro
default character set utf8
default collate utf8_general_ci;

use `cadastro`;
CREATE TABLE `pessoas` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nome` VARCHAR(30),
    `nascimento` DATE,
    `sexo` ENUM('M', 'F'),
    `peso` DECIMAL(5 , 2 ),
    `altura` DECIMAL(3 , 2 ),
    `nacionalidade` VARCHAR(20) DEFAULT 'Brasil',
    PRIMARY KEY (id)
)  DEFAULT CHARSET=UTF8;
