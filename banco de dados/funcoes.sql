-- COUNT Mostre quantos alunos estão cadastrados na tabela Aluno. (Use a função COUNT)/*

SELECT COUNT(*) AS TOTAL FROM Aluno;

-- MIN Mostre a menor mensalidade entre todos os cursos cadastrados. (Use a função MIN)~

SELECT MIN(MENSALIDADE), NOME
FROM CURSO;

-- MAX Mostre a maior nota1 registrada entre todos os alunos. (Use a função MAX)
SELECT MAX(NOTA1) FROM ALUNO;

-- SUM Calcule o valor total das mensalidades de todos os cursos. (Use a função SUM)

SELECT SUM(MENSALIDADE) AS VALOR_TOTAL
FROM CURSO;

-- AVG Mostre a média geral da nota2 dos alunos. (Use a função AVG)

SELECT AVG(NOTA2) MEDIA_GERAL_NOTA_2
FROM ALUNO;