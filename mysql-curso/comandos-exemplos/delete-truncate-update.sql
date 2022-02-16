insert into cursos values
(1, 'python', 'aulas de python 3 ministradas por mim', '1800', 3, 2021),
(2, 'html', 'aulas de html ministradas por mim', '900', 4, 2021),
(3, 'sql', 'aulas de mysql ministradas por mim', '200', 12, 2020),
(4, 'eletrônica', 'aulas de eletrônica ministradas por mim', '400', 2, 2019);

select * from cursos;

update cursos
set nome = 'Python3'
where idcurso = '1';

update cursos
set nome = 'php', descricao = 'aulas de php ministradas por mim', carga = 500
where idcurso = '4'
limit 1;

delete from cursos
where idcurso = '2';

truncate cursos;


