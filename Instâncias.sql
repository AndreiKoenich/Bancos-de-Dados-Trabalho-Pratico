-- Fundamentos de Bancos de Dados - Semestre 2022/01 - Turma A
-- Trabalho Prático - Etapa II

-- Andrei Pochmann Koenich
-- Gustavo Spellmeier Neves

DROP VIEW IF EXISTS InfoDiscente;

DROP TABLE IF EXISTS Membro_UFRGS CASCADE;
DROP TABLE IF EXISTS Atividade_extra CASCADE;
DROP TABLE IF EXISTS Comgrad CASCADE;
DROP TABLE IF EXISTS Composicao_turma CASCADE;
DROP TABLE IF EXISTS Curriculo CASCADE;
DROP TABLE IF EXISTS Curso CASCADE;
DROP TABLE IF EXISTS Departamento CASCADE;
DROP TABLE IF EXISTS Discente CASCADE;
DROP TABLE IF EXISTS Disciplina CASCADE;
DROP TABLE IF EXISTS Docente CASCADE;
DROP TABLE IF EXISTS Empresa CASCADE;
DROP TABLE IF EXISTS Matricula CASCADE;
DROP TABLE IF EXISTS Ministracao CASCADE;
DROP TABLE IF EXISTS Tecnico_adm CASCADE;
DROP TABLE IF EXISTS Turma CASCADE;

CREATE TABLE Membro_UFRGS
(codigo_vaga CHAR(8) NOT NULL,
nome VARCHAR(100) NOT NULL,
cpf CHAR(11) NOT NULL UNIQUE,
rg CHAR(10) NOT NULL UNIQUE,
data_nascimento DATE NOT NULL,
nacionalidade VARCHAR(50) NOT NULL,
titulo_eleitor CHAR(12) NOT NULL UNIQUE,
e_mail VARCHAR(100) NOT NULL UNIQUE,
telefone VARCHAR(13) NOT NULL,
endereco VARCHAR(100) NOT NULL,
estado_civil VARCHAR(10) NOT NULL,
PRIMARY KEY (codigo_vaga),
CHECK(estado_civil IN ('Solteiro','Casado','Separado','Divorciado','Viúvo')));

INSERT INTO Membro_UFRGS VALUES
('00308680','Andrei Pochmann Koenich','28372134905','8139867469','1999-03-12','Brasileiro','213547892312','andrei.koenich@gmail.com','555134735287','Rua Ernesto Weick,23 - Centro - Esteio','Solteiro'),
 
('00301624','Gustavo Spellmeier Neves','53245878912','5234598721','2001-05-18','Brasileiro','123576891231','gustavo.neves@gmail.com','5551993934592','Rua 24 de Outubro,815 - Moinhos de Vento,Porto Alegre','Separado'), 

('00324055','Pedro Company Beck','53215478910','9324578910','2004-06-29','Brasileiro','926965342355','pedro.beck@gmail.com','5551993934592','Rua São Manoel,98 - São José - Porto Alegre','Casado'),

('00352696','Pietro Benati Carrara','23568798715','3265871251','1997-06-21','Brasileiro','32456789123','pietro.carra@inf.ufrgs,br','555134594478','Av Dr. Nilo Peçanha,2131 - Chácara das Pedras,Porto Alegre','Viúvo'),

('00326542','Arthur Kapcizinski Muller','32256878755','1330046547','1999-05-07','Brasileiro','16452784623','arthur.muller@gmail.com','555134289625','Rua Voluntários da Pátria, Av. São Pedro, 2862, Porto Alegre - RS','Solteiro'),

('00324121','Thiago Santos da Rosa','63245851282','1674512721','2000-06-02','Brasileiro','516544892311','thiago.rosa@gmail.com','555132910111','R. Buarque de Macedo, 175 - São Geraldo, Porto Alegre - RS, 90230-250','Solteiro'),

('00292542','Eduarda Wenzel','25115223542','1449946537','1998-11-11','Brasileiro','679321622214','eduarda.wenzel@gmail.com','555132149527',' Av. Ipiranga, 1600 - Praia de Belas, Porto Alegre - RS','Casado'),

('00345627','Alice Brauwers','73225543918','1254242237','1999-12-23','Brasileiro','789321732219','alice.brauwers@gmail.com','555133345297','R. dos Andradas, 1664 - Centro Histórico, Porto Alegre - RS','Solteiro'),

('00321567','Gabriel Pereira Bernd','51286673911','3294352778','2000-10-15','Brasileiro','957982222321','gabriel.bernd@gmail.com','555132146225','Av. Dr. Nilo Peçanha, 1777 - Boa Vista, Porto Alegre - RS','Solteiro'),

('94614593','Luciano Paschoal Gaspary','35198014542','0339949548','1970-05-28','Brasileiro','307140135478','paschoal@inf.ufrgs.br','555134253292','Av. Assis Brasil,164 - salão 42 - São João,Porto Alegre - RS','Casado'),

('16184730','Marcelo Walter','18555968215','1115511754','1982-03-22','Brasileiro','529324517214','marcelo.walter@inf.ufrgs.br','555134689236','R. dos Andradas,1685 - Centro Histórico,Porto Alegre - RS','Solteiro'),

('71447770','Antônio Carlos Schneider Beck Filho','84883467321','6881688721','1990-02-25','Brasileiro','161847301245','caco@inf.ufrgs.br','555139321245','Av. Ipiranga,5200 - Azenha,Porto Alegre - RS','Casado'),

('51650993','Álvaro Freitas Moreira','12543365215','9581136278','1975-05-08','Brasileiro','125433658751','afmoreira@inf.ufrgs.br','555131245523','Av. Cristóvão Colombo,545 - Independência,Porto Alegre - RS,90560-003','Solteiro'),

('14922846','Danielle Lira da Rosa','84883467892','9368814224','1991-12-24','Brasileiro','374848355623','danielle.rosa@inf.ufrgs.br','555133086162','Av. Eduardo Prado,425 - Cavalhada,Porto Alegre - RS','Solteiro'),

('11805329','Julia Stuker de Almeida','84527465592','8361123115','1995-08-09','Brasileiro','152848298615','julia.stuker@gmail.com','555133524259',
'Av. Cristóvão Colombo, 545 - Floresta, Porto Alegre - RS','Casado'),

('22605542','Bernardo Frison Spiazzi','36585932582','8363435275','1996-07-07','Brasileiro','352822298792','bernardo.frison@gmail.com','555137895226',
'Av. Plínio Brasil Milano, 2343 - Passo dAreia, Porto Alegre - RS','Solteiro'),

('52687945','Cristian Daniel Piccini','12311660655','9167245926','1998-05-02','Brasileiro','962699086374','cristian.piccini@gmail.com','555134782562',
'Av. João Pessoa, 1831 - Farroupilha, Porto Alegre - RS','Separado'),

('21458768','Joana Rogowski Souza dos Santos','51545775750','1478630453','1997-02-22','Brasileiro','709076648373','joana.rogowski@gmail.com','555134266225','R. Osvaldo Pereira de Freitas, 2-78 - Partenon, Porto Alegre - RS','Solteiro'),

('23145678','Juliana Moi Silva','54792738378','1848685513','1996-05-14','Brasileiro','459915230098','juliana.moi@gmail.com','555134262248','Av. Diário de Notícias, 300 - Cristal, Porto Alegre - RS','Solteiro'),

('78912478','Débora Leite Rocha','51135484055','9098061047','1995-05-02','Brasileiro','120801051504','debora.rochaleite@gmail.com','555134822952','R. Albion, 111 - Partenon, Porto Alegre - RS','Solteiro'),

('21245678','Gabriela Brendel Blum','90159714345','8596920389','1997-12-16','Brasileiro','057285009686','gabriela.blum@gmail.com','555134899255','Av. Guilherme Schell, 6750 - Centro, Canoas - RS','Casado'),

('87954327','Enrico Emerim Moretto','78725046415','4620145578','1996-08-18','Brasileiro','155874070043','enrico.moretto@gmail.com','555134211152','Av. Farroupilha, 4545 - Mal. Rondon, Canoas - RS','Viúvo'),

('04939534','Sérgio Luis Cechin','02083098595','7839657358','1965-07-27','Brasileiro','869477653434','matheus.mews@gmail.com','5551977453968', 'Av. Boqueirão, 365 - Igara, Canoas - RS','Casado'),

('26683079','Diane Carvalho Martins','71671668750','6010457766','1970-01-30','Brasileiro','300982598492','diane.martins@gmail.com','5551908451322', 'R. Quinze de Janeiro, 11 - Centro, Canoas - RS','Solteiro');


-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Disciplina
(codigo_disciplina CHAR(8) NOT NULL,
nome VARCHAR(100) NOT NULL UNIQUE,
carga_horaria SMALLINT NOT NULL,
creditos SMALLINT NOT NULL,
PRIMARY KEY (codigo_disciplina));

INSERT INTO Disciplina VALUES
('MAT01353','Cálculo e Geometria Analítica I - A',90,6),
('INF01202','Algoritmos de Programação - CIC',90,6),
('INF01127','Engenharia de Software N',60,4),
('INF01047','Fundamentos de Computação Gráfica',60,4),
('INF01048','Inteligência Artificial',60,4),
('INF01121','Modelos de Linguagem de Programação',60,4),
('ENG10032','Microcontroladores',60,4),
('ENG10051','Dinâmica e Controle de Robôs',60,4),
('ENG04434','Arquiteturas Avançadas de Computadores',90,6),
('ENG04057','Sistemas Embarcados',75,5),
('INF01107','Introdução à Arquitetura de Computadores',60,4),
('IPH01014','Gerenciamento de Drenagem Urbana',60,4),
('ENG02003','Materiais de Construção Mecânica II - B',60,4),
('QUI01014','Química Inorgânica Para Engenheiros B',60,4),
('MAT01081','Geometria Projetiva',60,4),
('MED05021','Epidemologia I',30,2),
('AGR99005','Introdução à Agronomia - C',60,4);

-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Empresa
(cnpj_empresa CHAR(18) NOT NULL,
nome VARCHAR(100) NOT NULL UNIQUE,
endereco VARCHAR(100) NOT NULL UNIQUE,
telefone CHAR(12) NOT NULL UNIQUE,
e_mail VARCHAR(100) NOT NULL UNIQUE,
PRIMARY KEY (cnpj_empresa));

INSERT INTO Empresa VALUES
('07.954.317/0001-06','	Maison Agencia de Viagens e Turismo LTDA','Rua Anita Garibaldi,2340 - Boa Vista - Porto Alegre/RS','555130121969','maison.turismo@gmail.com'),
('14.702.832/0001-64','Celente Sports Management','Rua Guilherme Schell,176 - Santo Antônio - Porto Alegre/RS','555135193993','celente.sports@gmail.com'),
('45.616.077/0001-29','Mega Hold Brasil LTDA','Rua Pinto da Rocha,186 - Partenon - Porto Alegre/RS','555184096061','wilsonnegocios@gmail.com'),
('47.074.522/0001-00','Hermes Inteligência Digital','Rua Vinte e Quatro de Outubro,1121 - Auxiliadora - Porto Alegre/RS','555181505332','hermes.digital@gmail.com');

-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Departamento
(codigo_dpto CHAR(8) NOT NULL,
nome VARCHAR(100) NOT NULL UNIQUE,
endereco VARCHAR(100) NOT NULL UNIQUE,
telefone CHAR(12) NOT NULL UNIQUE,
e_mail VARCHAR(100) NOT NULL UNIQUE,
PRIMARY KEY (codigo_dpto));

INSERT INTO Departamento VALUES
('38289622','Departamento de Informática Aplicada','Instituto de Informática - UFRGS - Campus do Vale
Bloco IV - Prédio 43412 - Sala 215','555133087033','dep.ina@inf.ufrgs.br'),
('07806220','Departamento de Engenharia Elétrica','Osvaldo Aranha,103,2º andar','555133083515','delet@ufrgs.br'),
('92449402','Departamento de Engenharia Civil','Osvaldo Aranha,99,3º andar','555133083450','chefia.deciv@ufrgs.br'),
('41465428','Departamento de Engenharia de Minas','Av. Bento Gonçalves,9500 – Bloco IV – Prédio 74 – Sala 217 – Campus do Vale','555133089438','demin@ufrgs.br');

-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Curso
(codigo_curso CHAR(8) NOT NULL,
nome_curso VARCHAR(100) NOT NULL UNIQUE,
codigo_comgrad CHAR(8) NOT NULL,
creditos_obrigatorios SMALLINT NOT NULL,
creditos_eletivos SMALLINT NOT NULL,
creditos_complementares SMALLINT NOT NULL,
creditos_tipos SMALLINT NOT NULL,
carga_horaria_obrigatoria SMALLINT NOT NULL,
carga_horaria_eletiva SMALLINT NOT NULL,
etapas SMALLINT NOT NULL,
PRIMARY KEY (codigo_curso));

INSERT INTO Curso VALUES
('48402254','Ciência da Computação','57585040',152,36,8,2,2580,540,6),
('70123536','Engenharia de Computação','29454207',156,48,12,2,2640,720,10),
('60141072','Engenharia Civil','18354247',222,24,9,2,3750,360,10),
('98139834','Engenharia Elétrica','03499984',216,20,6,2,3490,300,10),
('54235278','Engenharia Mecânica','21548423',221,20,6,2,3575,300,10),
('11264755','Engenharia Química','22458648',220,18,6,2,3560,270,10),
('12167481','Matemática','01232589',136,12,16,2,2040,180,7),
('15648128','Medicina','21235479',589,0,0,0,8835,0,12),
('12564118','Agronomia','98723456',248,5,6,2,4080,75,8);

-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Comgrad
(codigo_comgrad CHAR(8) NOT NULL,
nome VARCHAR(100) NOT NULL UNIQUE,
fax_tecn CHAR(12) NOT NULL UNIQUE,
e_mail VARCHAR(100) NOT NULL UNIQUE,
endereco VARCHAR(100) NOT NULL UNIQUE,
telefone_tecn CHAR(12) NOT NULL UNIQUE,
codigo_curso CHAR(8) NOT NULL UNIQUE,
inicio_representacao DATE NOT NULL,
codigo_discente VARCHAR(8) NOT NULL UNIQUE,
PRIMARY KEY (codigo_comgrad),
FOREIGN KEY (codigo_curso) REFERENCES Curso(codigo_curso));

INSERT INTO Comgrad VALUES
('57585040','COMGRAD-CIC','555133087308','comgrad-cic-l@inf.ufrgs.br','Av. Bento Gonçalves,9500 – Bairro Agronomia
Campus do Vale – Bloco 4 – Prédio 43412 – Sala 206','555133086162','48402254', '2020-08-02','00308680'),

('29454207','COMGRAD-ECP','555133087309','comgrad-ecp@ufrgs.br','Av. Bento Gonçalves,9500 – Bairro Agronomia
Campus do Vale – Bloco 4 – Prédio 43412 – Sala 207','555133086163','70123536','2021-09-03','00324055'),

('18354247','COMGRAD-Engenharia Civil','555133126247','comgradciv@ufrgs.br','Av. Osvaldo Aranha,99. 3º andar.
Bairro Bom Fim,Porto Alegre,RS','555133083547','60141072','2019-07-06','00301624'),

('03499984','COMGRAD-Engenharia Elétrica','555132524269','comgradele@ufrgs.br','Av. Osvaldo Aranha esq. Sarmento Leite,103
Centro – Porto Alegre','555133084440','98139834','2021-12-15','00352696'),

('21548423','COMGRAD-MEC','555133083168','comgradmec@ufrgs.br','Rua Sarmento Leite, 425 – sala 202 - Bairro Centro - Porto Alegre',
'555133083929','54235278','2021-09-06','00326542'),

('22458648','COMGRAD-ENQ','555133083444','comgrad@enq.ufrgs.br ','Rua Ramiro Barcelos, 2777-Sala 263 (Anexo Campus Saúde)
Santana – Porto Alegre','555133085125','11264755','2018-12-15','00324121'),

('01232589','COMGRAD-MAT','555133086225','mat-comgradmat@ufrgs.br','Av. Bento Gonçalves, 9500 Prédio 43-111
Bairro Agronomia Porto Alegre, RS – BRASIL','555133086189','12167481','2020-05-11','00292542'),

('21235479','COMGRAD-MED','555133085581','comgrad.medicina@ufrgs.br','Rua Ramiro Barcelos, 2400 sala 416 - Porto Alegre/RS',
'555133085581','15648128','2021-04-08','00345627'),

('98723456','COMGRAD-AGRO','555133086018','cgradagr@ufrgs.br','Av. Bento Gonçalves, 7712 Agronomia – Porto Alegre',
'555133087438','12564118','2021-04-04','00321567');

ALTER TABLE Curso ADD FOREIGN KEY (codigo_comgrad) REFERENCES Comgrad(codigo_comgrad);

-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Docente
(codigo_vaga CHAR(8) NOT NULL,
titulacao VARCHAR(11) NOT NULL,
data_inicio DATE NOT NULL,
data_fim DATE,
vacancia DATE,
remuneracao NUMERIC(7,2) NOT NULL,
codigo_dpto CHAR(8),
cargo_dpto VARCHAR(60),
codigo_comgrad CHAR(8),
cargo_comgrad VARCHAR(60),
data_inicio_comgrad DATE,
remuneracao_comgrad NUMERIC(7,2),
PRIMARY KEY (codigo_vaga),
FOREIGN KEY (codigo_vaga) REFERENCES Membro_UFRGS(codigo_vaga) ON DELETE CASCADE,
FOREIGN KEY (codigo_dpto) REFERENCES Departamento(codigo_dpto),
FOREIGN KEY (codigo_comgrad) REFERENCES Comgrad(codigo_comgrad) ON DELETE SET NULL,
CHECK(titulacao IN ('Emérito','Titular','Associado','Adjunto','Substituto','Aposentado')));

INSERT INTO Docente VALUES
('94614593','Emérito','2002-05-22',NULL,NULL,12622.32,'07806220','Colaborador','57585040','Coordenador','2020-08-09',2500.00),
('16184730','Associado','2005-07-21',NULL,NULL,15789.64,'41465428','Substituto',NULL,NULL,NULL,NULL),
('71447770','Adjunto','2007-02-10',NULL,'2022-08-07',10232.21,'92449402','Colaborador','18354247','Coordenador Substituto','2019-05-14',1200.00),
('51650993','Aposentado','1998-05-22','2022-08-07',NULL,0000.00,NULL,NULL,NULL,NULL,NULL,NULL),
('04939534','Titular','2000-06-19','2025-01-12',NULL,14299.20,NULL,'Substituto', NULL, NULL, NULL, NULL),
('26683079','Titular','2012-11-03',NULL,NULL,13870.34,'38289622','Colaborador','29454207','Coordenador','2018-10-10',2500.00);


-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Discente
(matricula CHAR(8) NOT NULL,
ano_conclusaoEM CHAR(4) NOT NULL,
PRIMARY KEY (matricula),
FOREIGN KEY (matricula) REFERENCES Membro_UFRGS(codigo_vaga) ON DELETE CASCADE);

INSERT INTO Discente VALUES
('00308680','2014'),
('00301624','2013'),
('00324055','2012'),
('00352696','2014'),
('00326542','2015'),
('00324121','2016'),
('00292542','2014'),
('00345627','2013'),
('00321567','2012');

ALTER TABLE Comgrad ADD FOREIGN KEY (codigo_discente) REFERENCES Discente(matricula);

-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Tecnico_adm
(codigo_vaga CHAR(8) NOT NULL,
data_inicio DATE NOT NULL,
data_fim DATE,
vacancia DATE,
remuneracao NUMERIC(7,2),
codigo_comgrad CHAR(8) UNIQUE,
cargo_comgrad VARCHAR(60),
data_inicio_comgrad DATE,
remuneracao_comgrad NUMERIC(7,2),
PRIMARY KEY (codigo_vaga),
FOREIGN KEY (codigo_vaga) REFERENCES Membro_UFRGS(codigo_vaga) ON DELETE CASCADE,
FOREIGN KEY (codigo_comgrad) REFERENCES Comgrad(codigo_comgrad) ON DELETE SET NULL);

INSERT INTO Tecnico_adm VALUES
('14922846','2018-07-19',NULL,NULL,3500.00,'57585040','Técnico em Assuntos Educacionais','2020-05-04',1000.00),
('11805329','2018-05-05',NULL,NULL,2500.00,'29454207','Técnico em Questões Acadêmicas','2020-06-07',625.00),
('22605542','2019-06-12',NULL,NULL,2600.00,'18354247','Técnico em Administração','2019-06-18',750.00),
('52687945','2019-12-19',NULL,NULL,2250.40,'03499984','Técnico em Assuntos Educacionais','2021-07-07',1500.00),
('21458768','2018-10-11',NULL,NULL,1800.65,'21548423','Técnico em Administração','2020-11-11',2000.00),
('23145678','2019-05-02',NULL,'2022-09-27',2000.00,'22458648','Técnico em Questões Acadêmicas','2022-05-12',1500.00),
('78912478','2020-01-19',NULL,NULL,2500.00,'01232589','Técnico em Assuntos Educacionais','2021-09-15',750.00),
('21245678','2021-05-12',NULL,NULL,3500.00,'21235479','Técnico em Administração','2022-05-11',525.00),
('87954327','2020-12-12',NULL,NULL,3000.00,'98723456','Técnico em Assuntos Educacionais','2022-09-09',800.00);

-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Atividade_extra
(codigo_atividade CHAR(8) NOT NULL,
codigo_docente CHAR(8),
matricula_discente CHAR(8) NOT NULL,
nome VARCHAR(100) NOT NULL,
creditos_complementares SMALLINT NOT NULL,
bolsa NUMERIC(7,2) NOT NULL,
data_inicio DATE NOT NULL,
data_fim DATE,
indicador_ativo BOOLEAN NOT NULL,
carga_horaria SMALLINT NOT NULL,
cnpj_empresa CHAR(18),
PRIMARY KEY (codigo_atividade),
FOREIGN KEY (matricula_discente) REFERENCES Discente(matricula) ON DELETE CASCADE,
FOREIGN KEY (codigo_docente) REFERENCES Docente(codigo_vaga) ON DELETE SET NULL,
FOREIGN KEY (cnpj_empresa) REFERENCES Empresa(cnpj_empresa) ON DELETE SET NULL);

INSERT INTO Atividade_extra VALUES
('96998732','51650993','00308680','Computação Aproximada - Somadores Aproximados',2,400.00,'2021-08-01',NULL,TRUE,20,NULL),
('52492491',NULL,'00352696','Estágio em Inteligência Artificial',2,2500.00,'2021-06-06',NULL,TRUE,30,'47.074.522/0001-00');

-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Matricula
(matricula_discente CHAR(8) NOT NULL,
codigo_curso CHAR(8) NOT NULL,
semestre_inicio CHAR(7) NOT NULL,
data_fim DATE,
modalidade_ingresso VARCHAR(30) NOT NULL,
vaga_ingresso VARCHAR(30) NOT NULL,
ordem SMALLINT,
etapa VARCHAR(2),
PRIMARY KEY(matricula_discente,codigo_curso),
FOREIGN KEY (matricula_discente) REFERENCES Discente(matricula) ON DELETE CASCADE,
FOREIGN KEY (codigo_curso) REFERENCES Curso(codigo_curso) ON DELETE CASCADE);

INSERT INTO Matricula VALUES
('00308680','48402254','2015-1',NULL,'Vestibular','Ampla Concorrência',328,'4'),
('00301624','60141072','2018-1',NULL,'Vestibular','Ampla Concorrência',225,'5'),
('00352696','98139834','2014-1','2022-08-07','Vestibular','Ampla Concorrência',NULL,NULL),
('00324121','48402254','2020-1',NULL,'Vestibular','L3',29,'1'),
('00326542','48402254','2020-1',NULL,'SISU','L2',13,'1'),
('00324055','70123536','2019-2',NULL,'Vestibular','Ampla Concorrência',30,'1'),
('00292542','70123536','2020-1',NULL,'Vestibular','L5',7,'1'),
('00345627','48402254','2019-2',NULL,'Vestibular','Ampla Concorrência',3,'1'),
('00321567','48402254','2019-2',NULL,'Vestibular','Ampla Concorrência',6,'1');

-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Curriculo
(codigo_curso CHAR(8) NOT NULL,
codigo_disciplina CHAR(8) NOT NULL,
carater VARCHAR(11) NOT NULL,
PRIMARY KEY (codigo_curso,codigo_disciplina),
FOREIGN KEY (codigo_curso) REFERENCES Curso(codigo_curso) ON DELETE CASCADE,
FOREIGN KEY (codigo_disciplina) REFERENCES Disciplina(codigo_disciplina) ON DELETE CASCADE,
CHECK(carater IN ('Obrigatória','Eletiva')));

INSERT INTO Curriculo VALUES
('48402254','MAT01353','Obrigatória'),
('70123536','INF01202','Obrigatória'),
('98139834','INF01047','Eletiva'),
('48402254','INF01107','Obrigatória'),
('70123536','INF01107','Obrigatória'),
('60141072','IPH01014','Eletiva'),
('54235278','ENG02003','Obrigatória'),
('11264755','QUI01014','Obrigatória'),
('12167481','MAT01081','Eletiva'),
('15648128','MED05021','Obrigatória'),
('12564118','AGR99005','Obrigatória');

-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Turma
(codigo_turma CHAR(8) NOT NULL,
semestre CHAR(7) NOT NULL,
codigo_disciplina CHAR(8) NOT NULL,
vagas_oferecidas SMALLINT NOT NULL,
vagas_ocupadas SMALLINT NOT NULL,
horario CHAR(11) NOT NULL,
dias CHAR(5) NOT NULL,
PRIMARY KEY (codigo_turma, semestre),
FOREIGN KEY (codigo_disciplina) REFERENCES Disciplina(codigo_disciplina) ON DELETE CASCADE);

INSERT INTO Turma VALUES
('79931033','2020-2','MAT01353',100,75,'10:30-12:10','SNSNS'),
('32038497','2021-1','INF01202',40,38,'8:30-10:10','SSNNS'),
('54947179','2022-2','INF01127',30,30,'13:15-15:00','SNSNN'),
('52658099','2020-1','ENG04434',40,25,'10:30-12:10','SNSNS'),
('96483349','2022-1','INF01107',30,29,'8:30-10:10','SNSNN'),
('65774833','2022-1','INF01107',30,29,'8:30-10:10','NSNSN');

-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Composicao_turma
(matricula_discente CHAR(8) NOT NULL,
codigo_turma CHAR(8) NOT NULL,
semestre CHAR(7) NOT NULL,
conceito VARCHAR(2),
PRIMARY KEY (matricula_discente,codigo_turma,semestre),
FOREIGN KEY (matricula_discente) REFERENCES Discente(matricula) ON DELETE CASCADE,
FOREIGN KEY (codigo_turma,semestre) REFERENCES Turma(codigo_turma,semestre) ON DELETE CASCADE,
CHECK(conceito IN ('A','B','C','D','FF')));

INSERT INTO Composicao_turma VALUES
('00324055','79931033','2020-2','A'),
('00352696','32038497','2021-1','C'),
('00308680','52658099','2020-1','B'),
('00324121','96483349','2022-1','A'),
('00326542','96483349','2022-1','C'),
('00324055','96483349','2022-1','D'),
('00292542','65774833','2022-1','A'),
('00345627','65774833','2022-1','A'),
('00321567','65774833','2022-1','B');

-- ----------------------------------------------------------------------------------------------------

CREATE TABLE Ministracao
(codigo_docente CHAR(8) NOT NULL,
codigo_turma CHAR(8) NOT NULL,
semestre CHAR(7) NOT NULL,
PRIMARY KEY (codigo_docente,codigo_turma),
FOREIGN KEY (codigo_docente) REFERENCES Docente(codigo_vaga) ON DELETE CASCADE,
FOREIGN KEY (codigo_turma,semestre) REFERENCES Turma(codigo_turma,semestre) ON DELETE SET NULL);

INSERT INTO Ministracao VALUES
('71447770','52658099','2020-1'),
('16184730','32038497','2021-1'),
('51650993','79931033','2020-2'),
('04939534','54947179','2022-2'),
('04939534','96483349','2022-1'),
('26683079','65774833','2022-1')

-- ----------------------------------------------------------------------------------------------------