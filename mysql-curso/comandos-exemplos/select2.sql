select * from gafanhotos
where nome like 'camila'; # like = ter/tenha

select * from gafanhotos
where nome like 'ca%'; # % = qualquer coisa ou nada / ca% = começa com ca

select * from gafanhotos
where nome like '%a'; # = termina com a

select * from gafanhotos
where nome like '%a%'; # que possui a em qualquer parte da palavra

select * from cursos
where nome like 'ph%p%'; # que comece com ph, termine com p e tenha qualquer coisa no final

select * from cursos
where nome like 'ph%p_'; # começa com ph termina com p e obrigatóriamente _ tenha qualquer caractere no final

select distinct nacionalidade from gafanhotos
order by nacionalidade; # distinct = distinguir / une toda a informação para mostrar como unica

select distinct carga from cursos
order by carga;

select count(*) from cursos
where carga > 40; # count(*) = conta todos os valores iguais definidos

select count(*), nacionalidade from gafanhotos
where nacionalidade = 'brasil';

select max(carga) from cursos; # max() = retorna o valor maximo

select max(ano) from cursos;

select min(totaulas) from cursos; # min() = retorna o valor minimo

select min(totaulas), nome from cursos
where ano = '2016';

select sum(totaulas) from cursos
where ano = '2016'; # sum() = retorna a soma de todos os campos numericos

select avg(totaulas) from cursos
where ano = '2016'; # avg() = media aritmetica

select nome, nascimento from gafanhotos
where nascimento >= '2001-01-01' and nascimento <= '2015-12-31' order by nascimento;