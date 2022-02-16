# --- criação do banco de dados ---
create database empresa
default character set utf8
default collate = utf8_general_ci;

# --- criação da tabela clientes ---
create table clientes(
cpf int not null,
nome varchar(30) not null,
numero varchar(20),
primary key (cpf)
) default charset=utf8;

# --- modificações da tabela clientes ---
alter table clientes
add column carrinho int(9) default '000000000';

alter table clientes
add foreign key (carrinho)
references produtos(cod_barras);

alter table clientes
add column cartao_credit int(16) unique
after numero;

alter table clientes
modify column cpf int(11) not null unique;

# --- criação da segunda tabela, produtos ---
create table if not exists produtos (
cod_barras int(9) not null unique,
nome_produto varchar(30) not null,
primary key (cod_barras) 
) default charset=utf8;

# --- modificação da tabela produtos ---
alter table produtos
add column preco decimal(6,2) default '0,00';

alter table produtos
add column tipo enum('eletro', 'roupas', 'objetos') not null default 'objetos'
after nome_produto;

alter table produtos
modify cod_barras int(9) not null unique;

alter table produtos
change nome_produto n_produto varchar(30) not null unique;

# >>>> manipulação de dados da tabela clientes <<<<
insert into clientes values
('04623252027', 'alex giovani hirsch', '+555199570-2890', '7485757565478399', null);

insert into clientes values
('9', 'vera lucia hirsch', '55166447-7898', '637864563', null);

UPDATE `empresa`.`clientes`
SET `carrinho` = '123456789' 
WHERE (`cpf` = '2147483647');

# >>>> manipulação de dados da tabela produtos <<<<
insert into produtos values
(123456789, 'celular', 'eletro', '1230,99'),
(213456789, 'copo', 'objetos', '23,45'),
(823456719, 'casaco', 'roupas', '200,00');

# --- descrição de colunas das tabelas ---
desc clientes;
desc produtos;
select * from clientes;
select * from produtos;

select clientes.nome, produtos.n_produto from clientes inner join produtos
on produtos.cod_barras = clientes.carrinho;
