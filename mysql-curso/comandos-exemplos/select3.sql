select totaulas, count(*) from cursos
group by totaulas # group = agrupar/ tipo distinct mas pode ter acesso a funcao count()
order by totaulas;

select carga, totaulas, count(*) from cursos
where totaulas = 30
group by carga;

select carga, count(nome) from cursos
group by carga
having count(nome) > 3; # having = tendo / tendo a contagem do nome maior que 3, / o having só funciona com o group.

select ano, count(*) from cursos
where totaulas > 30
group by ano
having ano > 2013
order by count(*) desc;

select carga, count(*) from cursos
where ano > 2015
group by carga
having carga > (select avg(carga) from cursos);

# exercicios

select count(*), profissao from gafanhotos
group by profissao
order by profissao;

select sexo, count(*) from gafanhotos
where nascimento > '2005-01-01'
group by sexo;

select nacionalidade, count(*) from gafanhotos
where nacionalidade != 'brasil'
group by nacionalidade
having count(*) > 3
order by nacionalidade;

select altura, peso, count(*) from gafanhotos
where peso > 100.00
group by altura
having altura > (select avg(altura) from gafanhotos)
order by altura desc;

