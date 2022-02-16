create database produtos
default character set utf8
default collate utf8_general_ci;

use produtos;
CREATE TABLE refrigerante (
    sabor VARCHAR(10) NOT NULL UNIQUE,
    tamanho DECIMAL(2 , 1 ) NOT NULL,
    lote DATE NOT NULL,
    vencimento DATE NOT NULL
)  DEFAULT CHARSET=UTF8;

alter table refrigerante
add column id int not null first;

alter table refrigerante
modify column id int auto_increment;

alter table refrigerante
add primary key(id);

SELECT 
    *
FROM
    refrigerante;

CREATE TABLE IF NOT EXISTS sucos (
    id INT NOT NULL AUTO_INCREMENT,
    sabor VARCHAR(10) NOT NULL UNIQUE,
    gramas TINYINT(3) NOT NULL DEFAULT '125',
    PRIMARY KEY (id)
)  DEFAULT CHARSET=UTF8;

alter table sucos
modify sabor varchar(15) not null unique,
modify gramas int unsigned default '125';

SELECT 
    *
FROM
    sucos;
describe sucos;

use produtos;
insert into sucos values
(default, 'laranja', default),
(default, 'limão', default),
(default, 'melão', default),
(default, 'maracuja', default);

SELECT 
    *
FROM
    sucos;

alter table sucos
rename to balas;

alter table balas
add column preco decimal(3, 1) not null default 1.90;

describe balas;
SELECT 
    *
FROM
    balas;

alter table balas
change column gramas peso int unsigned default '125';

SELECT 
    *
FROM
    balas;
