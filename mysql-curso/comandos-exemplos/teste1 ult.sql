insert into refrigerante values
(2, 'laranja', '2', '2021-05-01', '2024-05-01'),
(3, 'maracuja', '2', '2021-05-01', '2024-05-01'),
(4, 'morango', '2', '2021-05-01', '2024-05-01'),
(5, 'banana', '2', '2021-05-01', '2024-05-01');

select * from refrigerante;

update refrigerante
set sabor = 'manga', vencimento = '2025-01-01'
where id = '5';

select * from refrigerante;

delete from refrigerante
where id = '4';

select * from balas;

truncate balas;

drop table balas;

alter table usuarios
drop column senha;

alter table usuarios
add column apelido varchar(10) after username;

create table if not exists pirulito(
id int auto_increment,
sabor varchar(12) unique,
quantidade int not null,
estoque int,
primary key(id)
) charset=utf8;

describe pirulito;

insert into pirulito values
(default, 'uva', 26, 123),
(default, 'laranja', 26, 123),
(default, 'banana', 25, 123),
(default, 'limão', 25, 123),
(default, 'abacate', 25, 123),
(default, 'tangerina', 25, 123),
(default, 'morango', 25, 123);

select * from pirulito;

update pirulito
set sabor = 'manga', estoque = 80
where id = '3';

describe pirulito;

alter table pirulito
modify column quantidade int not null default '25';

alter table pirulito
rename chiclete;
