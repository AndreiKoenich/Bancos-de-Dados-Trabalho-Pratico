-- Fundamentos de Bancos de Dados - Semestre 2022/01 - Turma A
-- Trabalho Prático - Etapa II

-- Andrei Pochmann Koenich
-- Gustavo Spellmeier Neves

-- Etapa 3: Item 2) Manipulação da BASe de Dados: Consultas, Visões, Gatilhos e Procedimentos

-- Item 2 a) Definir uma visão útil a seu universo de discurso, envolvendo no mínimo 2 tabelas.

-- VISÃO: Para cada um dos discentes, deseja-se saber o seu número de matrícula, o seu nome completo, os cursos nos quais
-- já foi matriculado, o semestre de início e a data em que o discente deixou de estar vinculado ao curso.

CREATE VIEW InfoDiscentes AS
SELECT DISTINCT matricula_discente, nome AS nome_discente, nome_curso, semestre_inicio, data_fim
FROM Membro_UFRGS JOIN Matricula ON (Membro_UFRGS.codigo_vaga = Matricula.matricula_discente) NATURAL JOIN Curso
ORDER BY nome_discente

-- Item 2 b) Definir um conjunto de 10 consultas úteis e variadas sobre seu Sistema de Informação, sendo que cada uma
-- delas deve envolver no mínimo 3 tabelas (uma visão conta como uma tabela). Os requisitos quantitativos são:

--------------------------------------------------------------------------------------------------------------------------------------------

-- a) No mínimo duas delas devem necessitar serem respondidas com a cláusula GROUP BY (isto é, a resposta deve
-- combinar atributos e totalizações sobre grupos ). Dentre essas, pelo menos uma deve incluir também a cláusula
-- Having.

-- CONSULTA 1: para cada docente que já ministrou uma disciplina de Cálculo, deseja-se saber o seu código de vaga, o seu nome, 
-- e a quantidade de turmas de Cálculo que ele já ministrou em todos os semestres até o momento.

SELECT codigo_vaga, Membro_UFRGS.nome AS nome_docente, COUNT(codigo_turma) AS total_turmas
FROM Membro_UFRGS JOIN Ministracao ON (Membro_UFRGS.codigo_vaga = Ministracao.codigo_docente) 
				  JOIN Turma USING (codigo_turma, semestre) JOIN Disciplina USING (codigo_disciplina) WHERE Disciplina.nome LIKE 'Cálculo%'
GROUP BY codigo_vaga
ORDER BY nome_docente

-- CONSULTA 2: considerando as titulações de docentes que possuem remuneração mensal média superior
-- à treze mil reais, deseja-se saber o código de vaga, o nome completo e o departamento dos professores
-- que possuem tais titulações.

SELECT codigo_vaga, Membro_UFRGS.nome AS nome_docente, titulacao, Departamento.nome AS nome_departamento
FROM Membro_UFRGS NATURAL JOIN Docente JOIN Departamento USING (codigo_dpto)
WHERE titulacao IN (SELECT titulacao
					FROM Docente
					GROUP BY titulacao
					HAVING AVG(remuneracao) > 13000)
ORDER BY titulacao, nome_docente				

--------------------------------------------------------------------------------------------------------------------------------------------

-- b) No mínimo duas delas devem necessitar serem respondidas com subconsulta (isto é, não existe formulação
-- equivalente usando apenas JOINs);

-- CONSULTA 3: deseja-se saber o código de vaga, a titulação, o nome completo, o departamento correspondente
-- e a data de início das atividades do(s) docente(s) com a maior remuneração padrão mensal da Universidade.

SELECT codigo_vaga, titulacao, Membro_UFRGS.nome AS nome_docente, data_inicio, Departamento.nome AS nome_departamento
FROM Membro_UFRGS NATURAL JOIN Docente JOIN Departamento USING (codigo_dpto)
WHERE remuneracao = (SELECT MAX(remuneracao) FROM Docente)
ORDER BY nome_docente

-- CONSULTA 4: deseja-se saber o número de matrícula, o nome completo, o ano de conclusão do Ensino Médio
--  e o semestre de ingresso dos discentes ativos que nunca obtiveram conceito 'D' ou 'FF' em nenhuma disciplina, na Universidade.

SELECT DISTINCT matricula_discente, nome_discente, ano_conclusaoEM, semestre_inicio
FROM InfoDiscentes JOIN Discente ON (matricula_discente = matricula)
WHERE data_fim IS NULL AND matricula_discente NOT IN (SELECT matricula_discente
                                              FROM InfoDiscentes JOIN Composicao_turma USING (matricula_discente)
                                              WHERE conceito = 'D' OR conceito = 'FF')
ORDER BY nome_discente
										   
--------------------------------------------------------------------------------------------------------------------------------------------

-- c) No mínimo uma delas (diferente das consultas acima) deve necessitar do operador NOT EXISTS para
-- responder questões do tipo TODOS ou NENHUM que <referencia> (isto é, não existe formulação
-- equivalente usando simplesmente JOINs ou subconsultas com (NOT) IN ou demais operadores relacionais)

-- CONSULTA 5: deseja-se saber o número de matrícula, o nome, o curso, o ano de conclusão do Ensino Médio e o semestre de ingresso dos 
-- discentes que já foram inseridos em todas as turmas (e talvez em outras) que o aluno "Thiago Santos da Rosa" já esteve inserido.

SELECT matricula_discente, nome_discente, nome_curso, ano_conclusaoEM, semestre_inicio
FROM InfoDiscentes INFO JOIN Discente ON (matricula_discente = matricula)
WHERE nome_discente <> 'Thiago Santos da Rosa' AND NOT EXISTS (SELECT matricula_discente 
														FROM InfoDiscentes NATURAL JOIN Composicao_turma
														WHERE nome_discente = 'Thiago Santos da Rosa' AND codigo_turma NOT IN
															(SELECT DISTINCT codigo_turma
															FROM InfoDiscentes NATURAL JOIN Composicao_turma
															WHERE matricula_discente = INFO.matricula_discente))
ORDER BY nome_discente														
																											
--------------------------------------------------------------------------------------------------------------------------------------------

-- CONSULTA 6: para cada discente, deseja-se saber o número de matrícula, o nome completo e todas as turmas (com o respectivo semestre)
-- em que já esteve lotado, junto com o nome da disciplina e o conceito obtido.

SELECT matricula_discente, nome_discente, codigo_turma, semestre, Disciplina.nome AS nome_disciplina, conceito 
FROM InfoDiscentes NATURAL JOIN Composicao_turma JOIN Turma USING (codigo_turma,semestre) JOIN Disciplina USING (codigo_disciplina)
ORDER BY nome_discente, semestre

-- CONSULTA 7: para cada docente, deseja-se saber o seu código de vaga, o nome completo e a quantidade de alunos que já foram reprovados 
-- (ou seja, que obtiveram conceito 'D' ou 'FF') em suas disciplinas.

SELECT codigo_vaga, nome AS nome_discente, COUNT(conceito)
FROM Membro_ufrgs NATURAL JOIN Docente NATURAL JOIN Ministracao JOIN Composicao_turma USING (codigo_turma)
WHERE conceito = 'D' OR conceito = 'FF'
GROUP BY codigo_vaga, nome_discente
ORDER BY nome_discente

-- CONSULTA 8: para cada discente, deseja-se saber o número de matrícula, o nome completo, e a quantidade de créditos obrigatórios
-- já obtida no curso no qual está matriculado.

SELECT matricula_discente, nome_discente, SUM(creditos) AS creditos_obrigatorios
FROM InfoDiscentes NATURAL JOIN Composicao_turma JOIN Turma USING (codigo_turma,semestre) JOIN Disciplina USING (codigo_disciplina)
WHERE data_fim IS NULL
GROUP BY (matricula_discente, nome_discente)
ORDER BY nome_discente

-- CONSULTA 9: para cada discente realizando uma atividade extra em alguma empresa, deseja-se saber o seu número de matrícula, o
-- nome completo, o curso no qual está atualmente matriculado, a datas de início e fim da atividade e, por fim, o CNPJ e o nome 
-- da empresa em questão.

SELECT matricula_discente, nome_discente, Atividade_extra.data_inicio AS inicio, Atividade_extra.data_fim AS fim, cnpj_empresa, Empresa.nome AS nome_empresa
FROM InfoDiscentes JOIN Atividade_extra USING (matricula_discente) JOIN Empresa USING (cnpj_empresa)
ORDER BY nome_discente	

-- CONSULTA 10: para todos os técnicos-administrativos que prestam algum serviço à uma Comissão de Graduação, deseja-se
-- saber o número da sua vaga, o seu nome completo, o nome da Comissão de Graduação correspondente, o seu cargo, a data de início
-- da prestação de serviços, e o valor da remuneração recebida unicamente pela prestação de serviços à sua Comissão.

SELECT codigo_vaga, Membro_UFRGS.nome AS nome_tecnico, Comgrad.nome AS nome_comgrad, cargo_comgrad, data_inicio_comgrad AS data_inicio, remuneracao_comgrad AS remuneracao
FROM Membro_UFRGS NATURAL JOIN Tecnico_adm JOIN Comgrad USING (codigo_comgrad)
ORDER BY nome_tecnico

-- Item 2 c) Definir um procedimento armazenado (stored procedure) que deve ser disparado por um gatilho ao atualizar
-- uma tabela (e.g. inserção, atualização ou remoção de tuplas). Você deve pesquisar a linguagem do SGBD escolhido
-- para definir este procedimento, e programar este procedimento nesta linguagem.

-- PROCEDIMENTO ARMAZENADO: deseja-se remover todas as conexões com comgrad e departamento de um dado professor quando o mesmo 
-- tiver programado sua data de fim das atividades como docente, pois, conforme estabelecido no Universo de Discurso:
-- "Nos casos em que um servidor deixa de prestar serviços para a UFRGS, os seus
-- dados permanecem armazenados no sistema, com exceção dos dados referentes à 
-- vinculação a um departamento ou à uma Comissão de Graduação."

-- Para a elaboração do procedimento, foi utilizada a linguagem referente ao PostgreSQL.

CREATE FUNCTION tira_departamento_comgrad()
RETURNS TRIGGER
LANGUAGE plpgsql
AS
$$
BEGIN
	UPDATE docente
	SET codigo_dpto = NULL, cargo_dpto = NULL, codigo_comgrad = NULL, cargo_comgrad = NULL, data_inicio_comgrad = NULL, remuneracao_comgrad = NULL
	WHERE(docente.codigo_vaga = NEW.codigo_vaga);
	RETURN NEW;
END;
$$;

CREATE TRIGGER trig_data_fim
AFTER UPDATE
ON docente
FOR EACH ROW
WHEN(OLD.data_fim IS NULL and NEW.data_fim IS NOT NULL)
EXECUTE PROCEDURE
tira_departamento_comgrad();

-- A consulta abaixo pode ser utilizada para visualizar de forma mais direta os efeitos do procedimento armazenado na base de dados,
-- nos casos em que é atribuída uma data de término de atividades para um docente.

-- CONSULTA EXTRA: para cada docente, deseja-se saber o seu código de vaga, nome completo, a sua 
-- comissão de graduação e o seu departamento ao qual está vinculado. Todos os docentes devem ser retornados (mesmo os que
-- não possuem vínculo com uma comissão ou com um departamento). 

SELECT DISTINCT codigo_vaga, Membro_UFRGS.nome AS nome_docente, Comgrad.nome AS nome_Comgrad, Departamento.nome AS nome_departamento
FROM Membro_UFRGS NATURAL JOIN Docente LEFT JOIN Comgrad USING (codigo_comgrad) LEFT JOIN Departamento USING (codigo_dpto)
ORDER BY nome_docente