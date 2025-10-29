/*1.Mostre todos os registros da tabela Aluno. (Use SELECT e FROM) */
SELECT * FROM Aluno;
/*2. Exiba apenas o nome e a nota1 de todos os alunos. (Use SELECT com colunas específicas)*/
SELECT NOME, NOTA1 FROM ALUNO;
/*3. Liste todos os alunos cuja nota2 seja maior que 8. (Use WHERE)*/
SELECT NOME, NOTA2 FROM ALUNO WHERE NOTA2 > 8;
/*4. Mostre os alunos que nasceram após o ano de 2000. (Use WHERE com data)*/
SELECT * FROM ALUNO WHERE DATA_NASCIMENTO > '2000-12-31';
/*5. Exiba o nome e a mensalidade de todos os cursos que custam mais de 600 reais. (Use WHERE com condição numérica)*/
SELECT NOME, MENSALIDADE
FROM CURSO
WHERE MENSALIDADE > 600;
/*6. Mostre o nome das turmas e o ano correspondente, ordenados pelo ano em ordem crescente. (Use ORDER BY)*/
SELECT NOME, ANO FROM TURMA ORDER BY ANO ASC;
/*7. Liste o ano das turmas e a quantidade de turmas por ano. (Use GROUP BY)*/
SELECT ANO, COUNT(*) AS QUANTIDADE_TURMAS
FROM TURMA
GROUP BY ANO;
/*8. Calcule a média da nota1 dos alunos por turma_id. (Use GROUP BY com função de agregação)*/
SELECT ID_TURMA, AVG(NOTA1) AS MEDIA_NOTA1
FROM ALUNO
GROUP BY ID_TURMA;

/*9. Mostre o ano e a quantidade de turmas apenas para os anos que têm mais de 2 turmas. (Use GROUP BY e HAVING) */
SELECT ANO, COUNT(*) AS QUANTIDADE_TURMAS
FROM TURMA
GROUP BY ANO
HAVING COUNT(*) > 2;
/*10. Exiba o nome dos cursos e suas mensalidades, ordenando primeiro pela mensalidade (decrescente). (Use ORDER BY) */
SELECT NOME, MENSALIDADE
FROM CURSO
ORDER BY MENSALIDADE DESC;