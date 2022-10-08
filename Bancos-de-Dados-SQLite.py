# Andrei Pochmann Koenich
# Gustavo Spellmeier Neves

# Fundamentos de Bancos de Dados - Semestre 2022/01 - Turma A

# O programa a seguir representa um banco de dados relacionado ao funcionamento de uma Universidade, permitindo ao
# usuário a realização de algumas consultas e modificações, conforme informado no menu.

import os
import sqlite3
import keyboard

def prepara_banco(cursor): # Remove as tabelas já existentes no banco de dados, com nomes iguais aos das novas tabelas.
    cursor.execute("DROP TABLE IF EXISTS Membro_UFRGS")
    cursor.execute("DROP TABLE IF EXISTS Atividade_extra")
    cursor.execute("DROP TABLE IF EXISTS Comgrad")
    cursor.execute("DROP TABLE IF EXISTS Composicao_turma")
    cursor.execute("DROP TABLE IF EXISTS Curriculo")
    cursor.execute("DROP TABLE IF EXISTS Curso")
    cursor.execute("DROP TABLE IF EXISTS Departamento")
    cursor.execute("DROP TABLE IF EXISTS Discente")
    cursor.execute("DROP TABLE IF EXISTS Disciplina")
    cursor.execute("DROP TABLE IF EXISTS Docente")
    cursor.execute("DROP TABLE IF EXISTS Empresa")
    cursor.execute("DROP TABLE IF EXISTS Matricula")
    cursor.execute("DROP TABLE IF EXISTS Ministracao")
    cursor.execute("DROP TABLE IF EXISTS Tecnico_adm")
    cursor.execute("DROP TABLE IF EXISTS Turma")

    return cursor # Retorna o cursor para o banco de dados atualizado, após as modificações.

def insere_tuplas(cursor): # Realiza todas as inserções de tuplas nas tabelas criadas.

    cursor.execute("INSERT INTO Membro_UFRGS VALUES('00308680','Andrei Pochmann Koenich','28372134905','8139867469','1999-03-12','Brasileiro','213547892312','andrei.koenich@gmail.com','555134735287','Rua Ernesto Weick,23 - Centro - Esteio','Solteiro')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('00301624','Gustavo Spellmeier Neves','53245878912','5234598721','2001-05-18','Brasileiro','123576891231','gustavo.neves@gmail.com','5551993934592','Rua 24 de Outubro,815 - Moinhos de Vento,Porto Alegre','Separado')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('00324055','Pedro Company Beck','53215478910','9324578910','2004-06-29','Brasileiro','926965342355','pedro.beck@gmail.com','5551993934592','Rua São Manoel,98 - São José - Porto Alegre','Casado')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('00352696','Pietro Benati Carrara','23568798715','3265871251','1997-06-21','Brasileiro','32456789123','pietro.carra@inf.ufrgs,br','555134594478','Av Dr. Nilo Peçanha,2131 - Chácara das Pedras,Porto Alegre','Viúvo')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('00326542','Arthur Kapcizinski Muller','32256878755','1330046547','1999-05-07','Brasileiro','16452784623','arthur.muller@gmail.com','555134289625','Rua Voluntários da Pátria, Av. São Pedro, 2862, Porto Alegre - RS','Solteiro')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('00324121','Thiago Santos da Rosa','63245851282','1674512721','2000-06-02','Brasileiro','516544892311','thiago.rosa@gmail.com','555132910111','R. Buarque de Macedo, 175 - São Geraldo, Porto Alegre - RS, 90230-250','Solteiro')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('00292542','Eduarda Wenzel','25115223542','1449946537','1998-11-11','Brasileiro','679321622214','eduarda.wenzel@gmail.com','555132149527',' Av. Ipiranga, 1600 - Praia de Belas, Porto Alegre - RS','Casado')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('00345627','Alice Brauwers','73225543918','1254242237','1999-12-23','Brasileiro','789321732219','alice.brauwers@gmail.com','555133345297','R. dos Andradas, 1664 - Centro Histórico, Porto Alegre - RS','Solteiro')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('00321567','Gabriel Pereira Bernd','51286673911','3294352778','2000-10-15','Brasileiro','957982222321','gabriel.bernd@gmail.com','555132146225','Av. Dr. Nilo Peçanha, 1777 - Boa Vista, Porto Alegre - RS','Solteiro')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('94614593','Luciano Paschoal Gaspary','35198014542','0339949548','1970-05-28','Brasileiro','307140135478','paschoal@inf.ufrgs.br','555134253292','Av. Assis Brasil,164 - salão 42 - São João,Porto Alegre - RS','Casado')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('16184730','Marcelo Walter','18555968215','1115511754','1982-03-22','Brasileiro','529324517214','marcelo.walter@inf.ufrgs.br','555134689236','R. dos Andradas,1685 - Centro Histórico,Porto Alegre - RS','Solteiro')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('71447770','Antônio Carlos Schneider Beck Filho','84883467321','6881688721','1990-02-25','Brasileiro','161847301245','caco@inf.ufrgs.br','555139321245','Av. Ipiranga,5200 - Azenha,Porto Alegre - RS','Casado')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('51650993','Álvaro Freitas Moreira','12543365215','9581136278','1975-05-08','Brasileiro','125433658751','afmoreira@inf.ufrgs.br','555131245523','Av. Cristóvão Colombo,545 - Independência,Porto Alegre - RS,90560-003','Solteiro')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('14922846','Danielle Lira da Rosa','84883467892','9368814224','1991-12-24','Brasileiro','374848355623','danielle.rosa@inf.ufrgs.br','555133086162','Av. Eduardo Prado,425 - Cavalhada,Porto Alegre - RS','Solteiro')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('11805329','Julia Stuker de Almeida','84527465592','8361123115','1995-08-09','Brasileiro','152848298615','julia.stuker@gmail.com','555133524259','Av. Cristóvão Colombo, 545 - Floresta, Porto Alegre - RS','Casado')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('22605542','Bernardo Frison Spiazzi','36585932582','8363435275','1996-07-07','Brasileiro','352822298792','bernardo.frison@gmail.com','555137895226','Av. Plínio Brasil Milano, 2343 - Passo dAreia, Porto Alegre - RS','Solteiro')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('52687945','Cristian Daniel Piccini','12311660655','9167245926','1998-05-02','Brasileiro','962699086374','cristian.piccini@gmail.com','555134782562','Av. João Pessoa, 1831 - Farroupilha, Porto Alegre - RS','Separado')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('21458768','Joana Rogowski Souza dos Santos','51545775750','1478630453','1997-02-22','Brasileiro','709076648373','joana.rogowski@gmail.com','555134266225','R. Osvaldo Pereira de Freitas, 2-78 - Partenon, Porto Alegre - RS','Solteiro')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('23145678','Juliana Moi Silva','54792738378','1848685513','1996-05-14','Brasileiro','459915230098','juliana.moi@gmail.com','555134262248','Av. Diário de Notícias, 300 - Cristal, Porto Alegre - RS','Solteiro')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('78912478','Débora Leite Rocha','51135484055','9098061047','1995-05-02','Brasileiro','120801051504','debora.rochaleite@gmail.com','555134822952','R. Albion, 111 - Partenon, Porto Alegre - RS','Solteiro')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('21245678','Gabriela Brendel Blum','90159714345','8596920389','1997-12-16','Brasileiro','057285009686','gabriela.blum@gmail.com','555134899255','Av. Guilherme Schell, 6750 - Centro, Canoas - RS','Casado')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('87954327','Enrico Emerim Moretto','78725046415','4620145578','1996-08-18','Brasileiro','155874070043','enrico.moretto@gmail.com','555134211152','Av. Farroupilha, 4545 - Mal. Rondon, Canoas - RS','Viúvo')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('04939534','Sérgio Luis Cechin','02083098595','7839657358','1965-07-27','Brasileiro','869477653434','sergio.cechin@gmail.com','5551977453968', 'Av. Boqueirão, 365 - Igara, Canoas - RS','Casado')")
    cursor.execute("INSERT INTO Membro_UFRGS VALUES('26683079','Diane Carvalho Martins','71671668750','6010457766','1970-01-30','Brasileiro','300982598492','diane.martins@gmail.com','5551908451322', 'R. Quinze de Janeiro, 11 - Centro, Canoas - RS','Solteiro')")

    cursor.execute("INSERT INTO Disciplina VALUES ('MAT01353','Cálculo e Geometria Analítica I - A',90,6)")
    cursor.execute("INSERT INTO Disciplina VALUES ('INF01202','Algoritmos de Programação - CIC',90,6)")
    cursor.execute("INSERT INTO Disciplina VALUES ('INF01127','Engenharia de Software N',60,4)")
    cursor.execute("INSERT INTO Disciplina VALUES ('INF01047','Fundamentos de Computação Gráfica',60,4)")
    cursor.execute("INSERT INTO Disciplina VALUES ('INF01048','Inteligência Artificial',60,4)")
    cursor.execute("INSERT INTO Disciplina VALUES ('INF01121','Modelos de Linguagem de Programação',60,4)")
    cursor.execute("INSERT INTO Disciplina VALUES ('ENG10032','Microcontroladores',60,4)")
    cursor.execute("INSERT INTO Disciplina VALUES ('ENG10051','Dinâmica e Controle de Robôs',60,4)")
    cursor.execute("INSERT INTO Disciplina VALUES ('ENG04434','Arquiteturas Avançadas de Computadores',90,6)")
    cursor.execute("INSERT INTO Disciplina VALUES ('ENG04057','Sistemas Embarcados',75,5)")
    cursor.execute("INSERT INTO Disciplina VALUES ('INF01107','Introdução à Arquitetura de Computadores',60,4)")
    cursor.execute("INSERT INTO Disciplina VALUES ('IPH01014','Gerenciamento de Drenagem Urbana',60,4)")
    cursor.execute("INSERT INTO Disciplina VALUES ('ENG02003','Materiais de Construção Mecânica II - B',60,4)")
    cursor.execute("INSERT INTO Disciplina VALUES ('QUI01014','Química Inorgânica Para Engenheiros B',60,4)")
    cursor.execute("INSERT INTO Disciplina VALUES ('MAT01081','Geometria Projetiva',60,4)")
    cursor.execute("INSERT INTO Disciplina VALUES ('MED05021','Epidemologia I',30,2)")
    cursor.execute("INSERT INTO Disciplina VALUES ('AGR99005','Introdução à Agronomia - C',60,4)")

    cursor.execute("INSERT INTO Empresa VALUES ('07.954.317/0001-06','	Maison Agencia de Viagens e Turismo LTDA','Rua Anita Garibaldi,2340 - Boa Vista - Porto Alegre/RS','555130121969','maison.turismo@gmail.com')")
    cursor.execute("INSERT INTO Empresa VALUES ('14.702.832/0001-64','Celente Sports Management','Rua Guilherme Schell,176 - Santo Antônio - Porto Alegre/RS','555135193993','celente.sports@gmail.com')")
    cursor.execute("INSERT INTO Empresa VALUES ('45.616.077/0001-29','Mega Hold Brasil LTDA','Rua Pinto da Rocha,186 - Partenon - Porto Alegre/RS','555184096061','wilsonnegocios@gmail.com')")
    cursor.execute("INSERT INTO Empresa VALUES ('47.074.522/0001-00','Hermes Inteligência Digital','Rua Vinte e Quatro de Outubro,1121 - Auxiliadora - Porto Alegre/RS','555181505332','hermes.digital@gmail.com')")

    cursor.execute("INSERT INTO Departamento VALUES ('38289622','Departamento de Informática Aplicada','Instituto de Informática - UFRGS - Campus do Vale Bloco IV - Prédio 43412 - Sala 215','555133087033','dep.ina@inf.ufrgs.br')")
    cursor.execute("INSERT INTO Departamento VALUES ('07806220','Departamento de Engenharia Elétrica','Osvaldo Aranha,103,2º andar','555133083515','delet@ufrgs.br')")
    cursor.execute("INSERT INTO Departamento VALUES ('92449402','Departamento de Engenharia Civil','Osvaldo Aranha,99,3º andar','555133083450','chefia.deciv@ufrgs.br')")
    cursor.execute("INSERT INTO Departamento VALUES ('41465428','Departamento de Engenharia de Minas','Av. Bento Gonçalves,9500 – Bloco IV – Prédio 74 – Sala 217 – Campus do Vale','555133089438','demin@ufrgs.br')")

    cursor.execute("INSERT INTO Curso VALUES ('48402254','Ciência da Computação','57585040',152,36,8,2,2580,540,6)")
    cursor.execute("INSERT INTO Curso VALUES ('70123536','Engenharia de Computação','29454207',156,48,12,2,2640,720,10)")
    cursor.execute("INSERT INTO Curso VALUES ('60141072','Engenharia Civil','18354247',222,24,9,2,3750,360,10)")
    cursor.execute("INSERT INTO Curso VALUES ('98139834','Engenharia Elétrica','03499984',216,20,6,2,3490,300,10)")
    cursor.execute("INSERT INTO Curso VALUES ('54235278','Engenharia Mecânica','21548423',221,20,6,2,3575,300,10)")
    cursor.execute("INSERT INTO Curso VALUES ('11264755','Engenharia Química','22458648',220,18,6,2,3560,270,10)")
    cursor.execute("INSERT INTO Curso VALUES ('12167481','Matemática','01232589',136,12,16,2,2040,180,7)")
    cursor.execute("INSERT INTO Curso VALUES ('15648128','Medicina','21235479',589,0,0,0,8835,0,12)")
    cursor.execute("INSERT INTO Curso VALUES ('12564118','Agronomia','98723456',248,5,6,2,4080,75,8)")

    cursor.execute("INSERT INTO Discente VALUES ('00308680','2014')")
    cursor.execute("INSERT INTO Discente VALUES ('00301624','2013')")
    cursor.execute("INSERT INTO Discente VALUES ('00324055','2012')")
    cursor.execute("INSERT INTO Discente VALUES ('00352696','2014')")
    cursor.execute("INSERT INTO Discente VALUES ('00326542','2015')")
    cursor.execute("INSERT INTO Discente VALUES ('00324121','2016')")
    cursor.execute("INSERT INTO Discente VALUES ('00292542','2014')")
    cursor.execute("INSERT INTO Discente VALUES ('00345627','2013')")
    cursor.execute("INSERT INTO Discente VALUES ('00321567','2012')")

    cursor.execute("INSERT INTO Comgrad VALUES ('57585040','COMGRAD-CIC','555133087308','comgrad-cic-l@inf.ufrgs.br','Av. Bento Gonçalves,9500 – Bairro Agronomia Campus do Vale – Bloco 4 – Prédio 43412 – Sala 206','555133086162','48402254', '2020-08-02','00308680')")
    cursor.execute("INSERT INTO Comgrad VALUES ('29454207','COMGRAD-ECP','555133087309','comgrad-ecp@ufrgs.br','Av. Bento Gonçalves,9500 – Bairro Agronomia Campus do Vale – Bloco 4 – Prédio 43412 – Sala 207','555133086163','70123536','2021-09-03','00324055')")
    cursor.execute("INSERT INTO Comgrad VALUES ('18354247','COMGRAD-Engenharia Civil','555133126247','comgradciv@ufrgs.br','Av. Osvaldo Aranha,99. 3º andar. Bairro Bom Fim,Porto Alegre,RS','555133083547','60141072','2019-07-06','00301624')")
    cursor.execute("INSERT INTO Comgrad VALUES ('03499984','COMGRAD-Engenharia Elétrica','555132524269','comgradele@ufrgs.br','Av. Osvaldo Aranha esq. Sarmento Leite,103 Centro – Porto Alegre','555133084440','98139834','2021-12-15','00352696')")
    cursor.execute("INSERT INTO Comgrad VALUES ('21548423','COMGRAD-MEC','555133083168','comgradmec@ufrgs.br','Rua Sarmento Leite, 425 – sala 202 - Bairro Centro - Porto Alegre', '555133083929','54235278','2021-09-06','00326542')")
    cursor.execute("INSERT INTO Comgrad VALUES ('22458648','COMGRAD-ENQ','555133083444','comgrad@enq.ufrgs.br ','Rua Ramiro Barcelos, 2777-Sala 263 (Anexo Campus Saúde) Santana – Porto Alegre','555133085125','11264755','2018-12-15','00324121')")
    cursor.execute("INSERT INTO Comgrad VALUES ('01232589','COMGRAD-MAT','555133086225','mat-comgradmat@ufrgs.br','Av. Bento Gonçalves, 9500 Prédio 43-111 Bairro Agronomia Porto Alegre, RS – BRASIL','555133086189','12167481','2020-05-11','00292542')")
    cursor.execute("INSERT INTO Comgrad VALUES ('21235479','COMGRAD-MED','555133085581','comgrad.medicina@ufrgs.br','Rua Ramiro Barcelos, 2400 sala 416 - Porto Alegre/RS', '555133085581','15648128','2021-04-08','00345627')")
    cursor.execute("INSERT INTO Comgrad VALUES ('98723456','COMGRAD-AGRO','555133086018','cgradagr@ufrgs.br','Av. Bento Gonçalves, 7712 Agronomia – Porto Alegre', '555133087438','12564118','2021-04-04','00321567')")

    cursor.execute("INSERT INTO Docente VALUES ('94614593','Emérito','2002-05-22',NULL,NULL,12622.32,'07806220','Colaborador','57585040','Coordenador','2020-08-09',2500.00)")
    cursor.execute("INSERT INTO Docente VALUES ('16184730','Associado','2005-07-21',NULL,NULL,15789.64,'41465428','Substituto',NULL,NULL,NULL,NULL)")
    cursor.execute("INSERT INTO Docente VALUES ('71447770','Adjunto','2007-02-10',NULL,'2022-08-07',10232.21,'92449402','Colaborador','18354247','Coordenador Substituto','2019-05-14',1200.00)")
    cursor.execute("INSERT INTO Docente VALUES ('51650993','Aposentado','1998-05-22','2022-08-07',NULL,0000.00,NULL,NULL,NULL,NULL,NULL,NULL)")
    cursor.execute("INSERT INTO Docente VALUES ('04939534','Titular','2000-06-19',NULL,NULL,14299.20,'38289622','Substituto', NULL, NULL, NULL, NULL)")
    cursor.execute("INSERT INTO Docente VALUES ('26683079','Titular','2012-11-03',NULL,NULL,13870.34,'38289622','Colaborador','29454207','Coordenador','2018-10-10',2500.00)")

    cursor.execute("INSERT INTO Tecnico_adm VALUES ('14922846','2018-07-19',NULL,NULL,3500.00,'57585040','Técnico em Assuntos Educacionais','2020-05-04',1000.00)")
    cursor.execute("INSERT INTO Tecnico_adm VALUES ('11805329','2018-05-05',NULL,NULL,2500.00,'29454207','Técnico em Questões Acadêmicas','2020-06-07',625.00)")
    cursor.execute("INSERT INTO Tecnico_adm VALUES ('22605542','2019-06-12',NULL,NULL,2600.00,'18354247','Técnico em Administração','2019-06-18',750.00)")
    cursor.execute("INSERT INTO Tecnico_adm VALUES ('52687945','2019-12-19',NULL,NULL,2250.40,'03499984','Técnico em Assuntos Educacionais','2021-07-07',1500.00)")
    cursor.execute("INSERT INTO Tecnico_adm VALUES ('21458768','2018-10-11',NULL,NULL,1800.65,'21548423','Técnico em Administração','2020-11-11',2000.00)")
    cursor.execute("INSERT INTO Tecnico_adm VALUES ('23145678','2019-05-02',NULL,'2022-09-27',2000.00,'22458648','Técnico em Questões Acadêmicas','2022-05-12',1500.00)")
    cursor.execute("INSERT INTO Tecnico_adm VALUES ('78912478','2020-01-19',NULL,NULL,2500.00,'01232589','Técnico em Assuntos Educacionais','2021-09-15',750.00)")
    cursor.execute("INSERT INTO Tecnico_adm VALUES ('21245678','2021-05-12',NULL,NULL,3500.00,'21235479','Técnico em Administração','2022-05-11',525.00)")
    cursor.execute("INSERT INTO Tecnico_adm VALUES ('87954327','2020-12-12',NULL,NULL,3000.00,'98723456','Técnico em Assuntos Educacionais','2022-09-09',800.00)")

    cursor.execute("INSERT INTO Atividade_extra VALUES ('96998732','51650993','00308680','Computação Aproximada - Somadores Aproximados',2,400.00,'2021-08-01',NULL,TRUE,20,NULL)")
    cursor.execute("INSERT INTO Atividade_extra VALUES ('52492491',NULL,'00352696','Estágio em Inteligência Artificial',2,2500.00,'2021-06-06',NULL,TRUE,30,'47.074.522/0001-00')")

    cursor.execute("INSERT INTO Matricula VALUES ('00308680','48402254','2015-1',NULL,'Vestibular','Ampla Concorrência',328,'4')")
    cursor.execute("INSERT INTO Matricula VALUES ('00301624','60141072','2018-1',NULL,'Vestibular','Ampla Concorrência',225,'5')")
    cursor.execute("INSERT INTO Matricula VALUES ('00352696','98139834','2014-1','2022-08-07','Vestibular','Ampla Concorrência',NULL,NULL)")
    cursor.execute("INSERT INTO Matricula VALUES ('00324121','48402254','2020-1',NULL,'Vestibular','L3',29,'1')")
    cursor.execute("INSERT INTO Matricula VALUES ('00326542','48402254','2020-1',NULL,'SISU','L2',13,'1')")
    cursor.execute("INSERT INTO Matricula VALUES ('00324055','70123536','2019-2',NULL,'Vestibular','Ampla Concorrência',30,'1')")
    cursor.execute("INSERT INTO Matricula VALUES ('00292542','70123536','2020-1',NULL,'Vestibular','L5',7,'1')")
    cursor.execute("INSERT INTO Matricula VALUES ('00345627','48402254','2019-2',NULL,'Vestibular','Ampla Concorrência',3,'1')")
    cursor.execute("INSERT INTO Matricula VALUES ('00321567','48402254','2019-2',NULL,'Vestibular','Ampla Concorrência',6,'1')")

    cursor.execute("INSERT INTO Curriculo VALUES ('48402254','MAT01353','Obrigatória')")
    cursor.execute("INSERT INTO Curriculo VALUES ('70123536','INF01202','Obrigatória')")
    cursor.execute("INSERT INTO Curriculo VALUES ('98139834','INF01047','Eletiva')")
    cursor.execute("INSERT INTO Curriculo VALUES ('48402254','INF01107','Obrigatória')")
    cursor.execute("INSERT INTO Curriculo VALUES ('70123536','INF01107','Obrigatória')")
    cursor.execute("INSERT INTO Curriculo VALUES ('60141072','IPH01014','Eletiva')")
    cursor.execute("INSERT INTO Curriculo VALUES ('54235278','ENG02003','Obrigatória')")
    cursor.execute("INSERT INTO Curriculo VALUES ('11264755','QUI01014','Obrigatória')")
    cursor.execute("INSERT INTO Curriculo VALUES ('12167481','MAT01081','Eletiva')")
    cursor.execute("INSERT INTO Curriculo VALUES ('15648128','MED05021','Obrigatória')")
    cursor.execute("INSERT INTO Curriculo VALUES ('12564118','AGR99005','Obrigatória')")

    cursor.execute("INSERT INTO Turma VALUES ('79931033','2020-2','MAT01353',100,75,'10:30-12:10','SNSNS')")
    cursor.execute("INSERT INTO Turma VALUES ('32038497','2021-1','INF01202',40,38,'8:30-10:10','SSNNS')")
    cursor.execute("INSERT INTO Turma VALUES ('54947179','2022-2','INF01127',30,30,'13:15-15:00','SNSNN')")
    cursor.execute("INSERT INTO Turma VALUES ('52658099','2020-1','ENG04434',40,25,'10:30-12:10','SNSNS')")
    cursor.execute("INSERT INTO Turma VALUES ('96483349','2022-1','INF01107',30,29,'8:30-10:10','SNSNN')")
    cursor.execute("INSERT INTO Turma VALUES ('65774833','2022-1','INF01107',30,29,'8:30-10:10','NSNSN')")

    cursor.execute("INSERT INTO Composicao_turma VALUES ('00324055','79931033','2020-2','A')")
    cursor.execute("INSERT INTO Composicao_turma VALUES ('00352696','32038497','2021-1','C')")
    cursor.execute("INSERT INTO Composicao_turma VALUES ('00308680','52658099','2020-1','B')")
    cursor.execute("INSERT INTO Composicao_turma VALUES ('00324121','96483349','2022-1','A')")
    cursor.execute("INSERT INTO Composicao_turma VALUES ('00326542','96483349','2022-1','C')")
    cursor.execute("INSERT INTO Composicao_turma VALUES ('00324055','96483349','2022-1','D')")
    cursor.execute("INSERT INTO Composicao_turma VALUES ('00292542','65774833','2022-1','A')")
    cursor.execute("INSERT INTO Composicao_turma VALUES ('00345627','65774833','2022-1','A')")
    cursor.execute("INSERT INTO Composicao_turma VALUES ('00321567','65774833','2022-1','B')")

    cursor.execute("INSERT INTO Ministracao VALUES ('71447770','52658099','2020-1')")
    cursor.execute("INSERT INTO Ministracao VALUES ('16184730','32038497','2021-1')")
    cursor.execute("INSERT INTO Ministracao VALUES ('51650993','79931033','2020-2')")
    cursor.execute("INSERT INTO Ministracao VALUES ('04939534','54947179','2022-2')")
    cursor.execute("INSERT INTO Ministracao VALUES ('04939534','96483349','2022-1')")
    cursor.execute("INSERT INTO Ministracao VALUES ('26683079','65774833','2022-1')")

    return cursor # Retorna o cursor para o banco de dados atualizado, após as modificações.

def instancia_tabelas(cursor): # Realiza as criações de todas as tabelas da base de dados.
    cursor.execute("CREATE TABLE Membro_UFRGS (codigo_vaga CHAR(8) PRIMARY KEY NOT NULL,"
                   "nome VARCHAR(100) NOT NULL, "
                   "cpf CHAR(11) NOT NULL UNIQUE, "
                   "rg CHAR(10) NOT NULL UNIQUE, "
                   "data_nascimento CHAR(10) NOT NULL, "
                   "nacionalidade VARCHAR(50) NOT NULL, "
                   "titulo_eleitor CHAR(12) NOT NULL UNIQUE, "
                   "e_mail VARCHAR(100) NOT NULL UNIQUE, "
                   "telefone VARCHAR(13) NOT NULL, "
                   "endereco VARCHAR(100) NOT NULL,"
                   "estado_civil VARCHAR(10) NOT NULL)")

    cursor.execute("CREATE TABLE Disciplina (codigo_disciplina CHAR(8) PRIMARY KEY NOT NULL,"
                   "nome VARCHAR(100) NOT NULL UNIQUE, "
                   "carga_horaria SMALLINT NOT NULL, "
                   "creditos SMALLINT NOT NULL)")

    cursor.execute("CREATE TABLE Empresa (cnpj_empresa CHAR(18) PRIMARY KEY NOT NULL,"
                   "nome VARCHAR(100) NOT NULL UNIQUE, "
                   "endereco VARCHAR(100) NOT NULL UNIQUE, "
                   "telefone CHAR(12) NOT NULL UNIQUE, "
                   "e_mail VARCHAR(100) NOT NULL UNIQUE)")

    cursor.execute("CREATE TABLE Departamento (codigo_dpto CHAR(8) PRIMARY KEY NOT NULL,"
                   "nome VARCHAR(100) NOT NULL UNIQUE, "
                   "endereco VARCHAR(100) NOT NULL UNIQUE, "
                   "telefone CHAR(12) NOT NULL UNIQUE, "
                   "e_mail VARCHAR(100) NOT NULL UNIQUE)")

    cursor.execute("CREATE TABLE Curso (codigo_curso CHAR(8) PRIMARY KEY NOT NULL,"
                   "nome_curso VARCHAR(100) NOT NULL UNIQUE, "
                   "codigo_comgrad CHAR(8) NOT NULL, "
                   "creditos_obrigatorios SMALLINT NOT NULL, "
                   "creditos_eletivos SMALLINT NOT NULL, "
                   "creditos_complementares SMALLINT NOT NULL, "
                   "creditos_tipos SMALLINT NOT NULL, "
                   "carga_horaria_obrigatoria SMALLINT NOT NULL, "
                   "carga_horaria_eletiva SMALLINT NOT NULL, "
                   "etapas SMALLINT NOT NULL)")

    cursor.execute("CREATE TABLE Comgrad (codigo_comgrad CHAR(8) PRIMARY KEY NOT NULL,"
                   "nome VARCHAR(100) NOT NULL UNIQUE, "
                   "fax_tecn CHAR(12) NOT NULL UNIQUE, "
                   "e_mail VARCHAR(100) NOT NULL UNIQUE, "
                   "endereco VARCHAR(100) NOT NULL UNIQUE, "
                   "telefone_tecn CHAR(12) NOT NULL UNIQUE, "
                   "codigo_curso CHAR(8) NOT NULL UNIQUE, "
                   "inicio_representacao CHAR(10) NOT NULL, "
                   "codigo_Discente VARCHAR(8) NOT NULL UNIQUE, "
                   "FOREIGN KEY (codigo_curso) REFERENCES Curso(codigo_curso),"
                   "FOREIGN KEY (codigo_Discente) REFERENCES Discente(matricula))")

    cursor.execute("CREATE TABLE Docente (codigo_vaga CHAR(8) PRIMARY KEY NOT NULL,"
                   "titulacao VARCHAR(11) NOT NULL, "
                   "data_inicio CHAR(10) NOT NULL, "
                   "data_fim CHAR(10), "
                   "vacancia CHAR(10), "
                   "remuneracao NUMERIC(7,2) NOT NULL, "
                   "codigo_dpto CHAR(8), "
                   "cargo_dpto VARCHAR(60), "
                   "codigo_comgrad CHAR(8), "
                   "cargo_comgrad VARCHAR(60), "
                   "data_inicio_comgrad CHAR(10), "
                   "remuneracao_comgrad NUMERIC(7,2), "
                   "FOREIGN KEY (codigo_vaga) REFERENCES Membro_UFRGS(codigo_vaga) ON DELETE CASCADE, "
                   "FOREIGN KEY (codigo_dpto) REFERENCES Departamento(codigo_dpto), "
                   "FOREIGN KEY (codigo_comgrad) REFERENCES Comgrad(codigo_comgrad) ON DELETE SET NULL, "
                   "CHECK(titulacao IN ('Emérito','Titular','Associado','Adjunto','Substituto','Aposentado')))")

    cursor.execute("CREATE TABLE Discente (matricula CHAR(8) PRIMARY KEY NOT NULL,"
                   "ano_conclusaoEM CHAR(4) NOT NULL, "
                   "FOREIGN KEY (matricula) REFERENCES Membro_UFRGS(codigo_vaga) ON DELETE CASCADE)")

    cursor.execute("CREATE TABLE Tecnico_adm (codigo_vaga CHAR(8) PRIMARY KEY NOT NULL, "
                   "data_inicio CHAR(10) NOT NULL, "
                   "data_fim CHAR(10), "
                   "vacancia CHAR(10), "
                   "remuneracao NUMERIC(7,2) NOT NULL, "
                   "codigo_comgrad CHAR(8) UNIQUE, "
                   "cargo_comgrad VARCHAR(60), "
                   "data_inicio_comgrad CHAR(10), "
                   "remuneracao_comgrad NUMERIC(7,2), "
                   "FOREIGN KEY (codigo_vaga) REFERENCES Membro_UFRGS(codigo_vaga) ON DELETE CASCADE, "
                   "FOREIGN KEY (codigo_comgrad) REFERENCES Comgrad(codigo_comgrad) ON DELETE SET NULL)")

    cursor.execute("CREATE TABLE Atividade_extra(codigo_atividade CHAR(8) PRIMARY KEY NOT NULL, "
                   "codigo_Docente CHAR(8), "
                   "matricula_Discente CHAR(8) NOT NULL, "
                   "nome VARCHAR(100) NOT NULL, "
                   "creditos_complementares SMALLINT NOT NULL, "
                   "bolsa NUMERIC(7,2) NOT NULL, "
                   "data_inicio CHAR(10) NOT NULL, "
                   "data_fim CHAR(10), "
                   "indicador_ativo BOOLEAN NOT NULL, "
                   "carga_horaria SMALLINT NOT NULL, "
                   "cnpj_empresa CHAR(18), "
                   "FOREIGN KEY (matricula_Discente) REFERENCES Discente(matricula) ON DELETE CASCADE, "
                   "FOREIGN KEY (codigo_Docente) REFERENCES Docente(codigo_vaga) ON DELETE SET NULL, "
                   "FOREIGN KEY (cnpj_empresa) REFERENCES Empresa(cnpj_empresa) ON DELETE SET NULL)")

    cursor.execute("CREATE TABLE Matricula(matricula_Discente CHAR(8) PRIMARY KEY NOT NULL, "
                   "codigo_curso CHAR(8) NOT NULL, "
                   "semestre_inicio CHAR(7) NOT NULL, "
                   "data_fim CHAR(10), "
                   "modalidade_ingresso VARCHAR(30) NOT NULL, "
                   "vaga_ingresso VARCHAR(30) NOT NULL, "
                   "ordem SMALLINT, "
                   "etapa VARCHAR(2), "
                   "FOREIGN KEY (matricula_Discente) REFERENCES Discente(matricula) ON DELETE CASCADE, "
                   "FOREIGN KEY (codigo_curso) REFERENCES Curso(codigo_curso) ON DELETE CASCADE)")

    cursor.execute("CREATE TABLE Curriculo(codigo_curso CHAR(8) NOT NULL, "
                   "codigo_disciplina CHAR(8) NOT NULL, "
                   "carater VARCHAR(11) NOT NULL, "
                    "PRIMARY KEY (codigo_curso, codigo_disciplina),"
                   "FOREIGN KEY (codigo_curso) REFERENCES Curso(codigo_curso) ON DELETE CASCADE,"
                   "FOREIGN KEY (codigo_disciplina) REFERENCES Disciplina(codigo_disciplina) ON DELETE CASCADE,"
                   "CHECK(carater IN ('Obrigatória','Eletiva')))")

    cursor.execute("CREATE TABLE Turma(codigo_turma CHAR(8) NOT NULL,"
                   "semestre CHAR(7) NOT NULL,"
                   "codigo_disciplina CHAR(8) NOT NULL,"
                   "vagas_oferecidas SMALLINT NOT NULL,"
                   "vagas_ocupadas SMALLINT NOT NULL,"
                   "horario CHAR(11) NOT NULL,"
                   "dias CHAR(5) NOT NULL,"
                   "PRIMARY KEY (codigo_turma, semestre),"
                   "FOREIGN KEY (codigo_disciplina) REFERENCES Disciplina(codigo_disciplina) ON DELETE CASCADE)")

    cursor.execute("CREATE TABLE Composicao_turma(matricula_Discente CHAR(8) NOT NULL,"
                   "codigo_turma CHAR(8) NOT NULL,"
                   "semestre CHAR(7) NOT NULL,"
                   "conceito VARCHAR(2),"
                   "PRIMARY KEY (matricula_Discente,codigo_turma,semestre),"
                   "FOREIGN KEY (matricula_Discente) REFERENCES Discente(matricula) ON DELETE CASCADE,"
                   "FOREIGN KEY (codigo_turma,semestre) REFERENCES Turma(codigo_turma,semestre) ON DELETE CASCADE,"
                   "CHECK(conceito IN ('A','B','C','D','FF')))")

    cursor.execute("CREATE TABLE Ministracao(codigo_Docente CHAR(8) NOT NULL,"
                   "codigo_turma CHAR(8) NOT NULL,"
                   "semestre CHAR(7) NOT NULL,"
                   "PRIMARY KEY (codigo_Docente,codigo_turma),"
                   "FOREIGN KEY (codigo_Docente) REFERENCES Docente(codigo_vaga) ON DELETE CASCADE,"
                   "FOREIGN KEY (codigo_turma,semestre) REFERENCES Turma(codigo_turma,semestre) ON DELETE SET NULL)")

    cursor = insere_tuplas(cursor) # Realiza todas as inserções de tuplas nas tabelas criadas.
    return cursor # Retorna o cursor para o banco de dados atualizado, após as modificações.

# Realiza operações de consultas nas tabelas criadas, de acordo com a escolha do usuário,
# permitindo também colocar o gatilho em funcionamento, além de alterar a data de fim
# das atividades de ensino por parte de algum Docente.
# Consultas parametrizadas: consultas 2,4, 5 e 7.
def armazena_consultas():

    # CONSULTA 1: Para cada Docente que já ministrou uma disciplina de Cálculo, consultar o seu código da vaga, o seu nome
    # e a quantidade de turmas de Cálculo que ele já ministrou em todos os semestres até o momento.
    consulta1 = ("""SELECT codigo_vaga, Membro_UFRGS.nome as nome_Docente, count(codigo_turma) AS total_turmas
                    FROM Membro_UFRGS JOIN Ministracao ON (Membro_UFRGS.codigo_vaga = Ministracao.codigo_Docente) 
                                      JOIN Turma using (codigo_turma, semestre) JOIN Disciplina using (codigo_disciplina)WHERE Disciplina.nome LIKE 'Cálculo%'
                    GROUP BY codigo_vaga
                    ORDER BY nome_Docente""")


    # CONSULTA 2: Considerando as titulações de Docentes que possuem remuneração mensal média superior a um determinado valor,
    # consultar o código da vaga, o nome completo e o departamento dos professores que possuem tais titulações.
    consulta2 = ("""SELECT codigo_vaga, Membro_UFRGS.nome AS nome_Docente, titulacao, Departamento.nome AS nome_departamento
                    FROM Membro_UFRGS NATURAL JOIN Docente JOIN Departamento USING (codigo_dpto)
                    WHERE titulacao IN (SELECT titulacao
                                        FROM Docente
                                        GROUP BY titulacao
                                        HAVING AVG(remuneracao) > ?)
                    ORDER BY titulacao, nome_Docente""")

    # CONSULTA 3: Consultar o código da vaga, a titulação, o nome completo, o departamento correspondente
    # e a data de início das atividades do(s) Docente(s) com a maior remuneração padrão mensal da Universidade.
    consulta3 = ("""SELECT codigo_vaga, titulacao, Membro_UFRGS.nome AS nome_Docente, data_inicio, Departamento.nome AS nome_departamento
                    FROM Membro_UFRGS NATURAL JOIN Docente JOIN Departamento USING (codigo_dpto)
                    WHERE remuneracao = (SELECT MAX(remuneracao) FROM Docente)
                    ORDER BY nome_Docente""")

    # CONSULTA 4: Consultar o número de matrícula, o nome completo, o ano de conclusão do Ensino Médio
    # e o semestre de ingresso dos Discentes ativos que nunca obtiveram um determinado conceito em alguma disciplina qualquer.
    consulta4 = ("""SELECT DISTINCT matricula_Discente, nome_Discente, ano_conclusaoEM, semestre_inicio
                    FROM InfoDiscentes JOIN Discente ON (matricula_Discente = matricula)
                    WHERE data_fim IS NULL AND matricula_Discente NOT IN (SELECT matricula_Discente
                                                                  FROM InfoDiscentes JOIN Composicao_turma USING (matricula_Discente)
                                                                  WHERE conceito = ?)
                    ORDER BY nome_Discente""")

    # CONSULTA 5: Consultar o número de matrícula, o nome, o curso, o ano de conclusão do Ensino Médio e o semestre de ingresso dos
    # Discentes que já foram inseridos em todas as turmas (e talvez em outras) que um determinado aluno já esteve inserido.
    consulta5 = ("""SELECT matricula_Discente, nome_Discente, nome_curso, ano_conclusaoEM, semestre_inicio
                    FROM InfoDiscentes INFO JOIN Discente ON (matricula_Discente = matricula)
                    WHERE nome_Discente <> ? AND NOT EXISTS (SELECT matricula_Discente 
                                                                            FROM InfoDiscentes NATURAL JOIN Composicao_turma
                                                                            WHERE nome_Discente = ? AND codigo_turma NOT IN
                                                                                (SELECT DISTINCT codigo_turma
                                                                                FROM InfoDiscentes NATURAL JOIN Composicao_turma
                                                                                WHERE matricula_Discente = INFO.matricula_Discente))
                    ORDER BY nome_Discente""")


    # CONSULTA 6: Para cada Discente, consultar o número de matrícula, o nome completo e todas as turmas (com o respectivo semestre)
    #  em que já esteve lotado, junto com o nome da disciplina e o conceito obtido.
    consulta6 = ("""SELECT matricula_Discente, nome_Discente, codigo_turma, semestre, Disciplina.nome AS nome_disciplina, conceito 
                    FROM InfoDiscentes NATURAL JOIN Composicao_turma JOIN Turma USING (codigo_turma,semestre) JOIN Disciplina USING (codigo_disciplina)
                    ORDER BY nome_Discente, semestre""")

    # CONSULTA 7: Para cada Docente, consultar o seu código da vaga, o nome completo e a quantidade de alunos que já receberam
    # um determinado conceito na sua disciplina.
    consulta7 = ("""SELECT codigo_vaga, nome AS nome_Discente, COUNT(conceito)
                    FROM Membro_ufrgs NATURAL JOIN Docente NATURAL JOIN Ministracao JOIN Composicao_turma USING (codigo_turma)
                    WHERE conceito = ?
                    GROUP BY codigo_vaga, nome_Discente
                    ORDER BY nome_Discente""")

    # CONSULTA 8: Para cada Discente, consultar o número de matrícula, o nome completo, e a quantidade de créditos obrigatórios
    # já obtida no curso no qual está matriculado.
    consulta8 = ("""SELECT matricula_Discente, nome_Discente, SUM(creditos) AS creditos_obrigatorios
                    FROM InfoDiscentes NATURAL JOIN Composicao_turma JOIN Turma USING (codigo_turma,semestre) JOIN Disciplina USING (codigo_disciplina)
                    WHERE data_fim IS NULL
                    GROUP BY matricula_Discente, nome_Discente
                    ORDER BY nome_Discente
                    """)
    # CONSULTA 9: Para cada Discente realizando uma atividade extra em alguma empresa, consultar o seu número de matrícula, o
    # nome completo, o curso no qual está atualmente matriculado,as datas de início e fim da atividade e, por fim o CNPJ e o nome
    # da empresa em questão.
    consulta9 = ("""SELECT matricula_Discente, nome_Discente, Atividade_extra.data_inicio AS inicio, Atividade_extra.data_fim AS fim, cnpj_empresa, Empresa.nome AS nome_empresa
                    FROM InfoDiscentes JOIN Atividade_extra USING (matricula_Discente) JOIN Empresa USING (cnpj_empresa)
                    ORDER BY nome_Discente""")

    # CONSULTA 10: Para todos os técnicos-administrativos que prestam algum serviço à uma Comissão de Graduação, consultar
    # o número da sua vaga, o seu nome completo, o nome da Comissão de Graduação correspondente, o seu cargo, a data de início
    # da prestação de serviços, e o valor da remuneração recebida unicamente pela prestação de serviços à sua Comissão.
    consulta10 = ("""SELECT codigo_vaga, Membro_UFRGS.nome AS nome_tecnico, Comgrad.nome AS nome_comgrad, cargo_comgrad, data_inicio_comgrad AS data_inicio, remuneracao_comgrad AS remuneracao
                    FROM Membro_UFRGS NATURAL JOIN Tecnico_adm JOIN Comgrad USING (codigo_comgrad)
                    ORDER BY nome_tecnico""")

    # CONSULTA 11: Para cada Docente, consultar o seu código da vaga, o seu nome completo, e, de acordo com
    # o que consta no sistema, os códigos de todas as turmas que já ministrou até o momento, junto com o respectivo semestre.
    consulta11 = ("""SELECT codigo_vaga, Membro_UFRGS.nome AS nome_Docente, codigo_turma, semestre
                    FROM Membro_UFRGS JOIN Ministracao ON (codigo_vaga = codigo_Docente)
                    ORDER BY nome_Docente""")

    # CONSULTA 12: Para cada Docente, consultar o seu código da vaga, nome completo, a sua
    # comissão de graduação e o seu departamento ao qual está vinculado, além da sua data de fim das atividades na Universidade.
    # Todos os Docentes devem ser retornados (mesmo os que não possuem vínculo com uma comissão ou com um departamento).
    consulta12 = ("""SELECT DISTINCT codigo_vaga, Membro_UFRGS.nome AS nome_Docente, Comgrad.nome AS nome_Comgrad, Departamento.nome AS nome_departamento, data_fim
                    FROM Membro_UFRGS NATURAL JOIN Docente LEFT JOIN Comgrad USING (codigo_comgrad) LEFT JOIN Departamento USING (codigo_dpto)
                    ORDER BY nome_Docente""")

    lista_consultas = []
    lista_consultas.append(consulta1) # Armazena todas as consultas definidas em uma lista.
    lista_consultas.append(consulta2)
    lista_consultas.append(consulta3)
    lista_consultas.append(consulta4)
    lista_consultas.append(consulta5)
    lista_consultas.append(consulta6)
    lista_consultas.append(consulta7)
    lista_consultas.append(consulta8)
    lista_consultas.append(consulta9)
    lista_consultas.append(consulta10)
    lista_consultas.append(consulta11)
    lista_consultas.append(consulta12)
    return lista_consultas # Retorna a lista contendo todas as consultas definidas.

def imprime_opcoes(): # Mostra ao usuário todas as opções possíveis de serem realizadas no banco de dados.

    print('--OPERAÇÕES NO BANCO DE DADOS--\n')
    print('Pressione a tecla para escolher a operação a ser realizada:')

    print('\n1 - Para cada Docente que já ministrou uma disciplina de Cálculo, consultar o seu código da vaga, o seu nome,\n'
          'e a quantidade de turmas de Cálculo que ele já ministrou em todos os semestres até o momento.\n')

    print('2 - Considerando as titulações de Docentes que possuem remuneração mensal média superior a um determinado valor,\n'
          'consultar o código da vaga, o nome completo e o departamento dos professores que possuem tais titulações.\n')

    print('3 - Consultar o código da vaga, a titulação, o nome completo, o departamento correspondente'
          'e a data de início\ndas atividades do(s) Docente(s) com a maior remuneração padrão mensal da Universidade.\n')

    print('4 - Consultar o número de matrícula, o nome completo, o ano de conclusão do Ensino Médio '
          'e o semestre de ingresso dos Discentes\nativos que nunca obtiveram um determinado conceito em alguma disciplina qualquer.\n')

    print('5 - Consultar o número de matrícula, o nome, o curso, o ano de conclusão do Ensino Médio e o semestre de ingresso dos '
          'Discentes que já\nforam inseridos em todas as turmas (e talvez em outras) que um determinado aluno já esteve inserido.\n')

    print('6 - Para cada Discente, consultar o número de matrícula, o nome completo e todas as turmas (com o respectivo semestre)\n'
          'em que já esteve lotado, junto com o nome da disciplina e o conceito obtido.\n')

    print('7 - Para cada Docente, consultar o seu código da vaga, o nome completo e a quantidade de alunos que já receberam'
          'um determinado conceito na sua disciplina.\n')

    print('8 - Para cada Discente, consultar o número de matrícula, o nome completo, e a quantidade de créditos obrigatórios'
          ' já obtida no curso no qual está matriculado.\n')

    print('9 - Para cada Discente realizando uma atividade extra em alguma empresa, consultar o seu número de matrícula, o'
          'nome completo, o curso no qual está atualmente matriculado,\n as datas de início e fim da atividade e, por fim, o CNPJ e o nome '
          'da empresa em questão.\n')

    print('Z - Para todos os técnicos-administrativos que prestam algum serviço à uma Comissão de Graduação, consultar'
          'o código da sua vaga, o seu nome completo\n, o nome da Comissão de Graduação correspondente, o seu cargo, a data de início'
          'da prestação de serviços, e o valor da remuneração recebida unicamente pela prestação de serviços à sua Comissão.\n')

    print('X - Para cada Docente, consultar o seu código da vaga, o seu nome completo, e, de acordo com '
          'o que consta no sistema,\nos códigos de todas as turmas que já ministrou até o momento, junto com o respectivo semestre.\n')

    print('C - Para cada Docente, consultar o seu código da vaga, nome completo, a sua'
            'comissão de graduação e o seu departamento ao qual está vinculado, além da sua data de fim das atividades na Universidade.'
          ' Todos os Docentes devem ser retornados (mesmo os que não possuem vínculo com uma comissão ou com um departamento).\n')

    print('V - Consultar a visão definida na base de dados, a qual mostra, para cada um dos Discentes, o seu número de matrícula, \no seu nome completo, os cursos nos quais '
          'já foi matriculado, o semestre de início e a data em que o Discente deixou de estar vinculado ao curso.\n')

    print('G - Colocar em funcionamento o gatilho responsável por remover todas as conexões com comgrad e departamento de um dado Docente quando o mesmo' 
    'tiver programado sua data de fim das atividades como Docente.\n')

    print('D - Atribuir uma data de fim de realização de atividades para um Docente.\n')

    print('ESC - Encerrar execução do programa.\n')

def realiza_operacoes(cursor): # Permite ao usuário realizar as operações contidas no menu, na base de dados já criada.

    lista_consultas = armazena_consultas() # Cria a lista contendo todas as consultas possíveis de serem realizadas.

    limpa_visao = ("""DROP VIEW IF EXISTS InfoDiscentes""")
    cursor.execute(limpa_visao) # Elimina uma visão já existente, caso possua o mesmo nome da nova visão.

    visao = ("""CREATE VIEW IF NOT EXISTS InfoDiscentes AS
                  SELECT DISTINCT matricula_Discente, nome AS nome_Discente, nome_curso, semestre_inicio, data_fim
                  FROM Membro_UFRGS JOIN Matricula ON (Membro_UFRGS.codigo_vaga = Matricula.matricula_Discente) NATURAL JOIN Curso
                  ORDER BY nome""")
    cursor.execute(visao) # Realiza a criação da nova visão útil, na base de dados.

    limpa_gatilho = ("DROP TRIGGER IF EXISTS trig_data_fim;") # Elimina um gatilho já existente, caso possua o mesmo nome do novo gatilho.

    # Realiza a criação do novo gatilho útil, na base de dados.
    gatilho = ( """CREATE TRIGGER trig_data_fim
                AFTER UPDATE ON Docente
                FOR EACH ROW
                WHEN(OLD.data_fim IS NULL and NEW.data_fim IS NOT NULL)
                BEGIN
                    UPDATE Docente
                    SET codigo_dpto = NULL, cargo_dpto = NULL, codigo_comgrad = NULL, cargo_comgrad = NULL, data_inicio_comgrad = NULL, remuneracao_comgrad = NULL
                    WHERE(Docente.codigo_vaga = NEW.codigo_vaga);
                END;""")

    # Operação de atualização, para atribuir uma data de fim de atividades para um determinado Docente.
    fim_Docente =  ("""UPDATE Docente
                    SET data_fim = ?
                    WHERE codigo_vaga = ?""")

    imprime_opcoes() # Mostra ao usuário todas as opções possíveis de serem realizadas no banco de dados.

    while True: # Iteração para permitir que o usuário realize as operações na base de dados, até que o programa seja encerrado pressionando ESC.
        if keyboard.is_pressed('1'):
            cursor.execute(lista_consultas[0])
            print(cursor.fetchall())
            input("Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('2'):
            remuneracao = int(input('Digite o valor da remuneracao a ser considerada:\n'))
            cursor.execute(lista_consultas[1], (remuneracao,))
            print(cursor.fetchall())
            input("Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('3'):
            cursor.execute(lista_consultas[2])
            print(cursor.fetchall())
            input("Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('4'):
            conceito = str(input('Digite o conceito a ser considerado (A, B, C, D ou FF):\n'))
            cursor.execute(lista_consultas[3],(conceito,))
            print(cursor.fetchall())
            input("Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('5'):
            nome_aluno = str(input('Digite o nome do aluno a ser considerado:\n'))
            cursor.execute(lista_consultas[4],(nome_aluno,nome_aluno,))
            print(cursor.fetchall())
            input("Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('6'):
            cursor.execute(lista_consultas[5])
            print(cursor.fetchall())
            input("Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('7'):
            conceito = str(input('Digite o conceito a ser considerado (A, B, C, D ou FF):\n'))
            cursor.execute(lista_consultas[6],(conceito,))
            print(cursor.fetchall())
            input("Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('8'):
            cursor.execute(lista_consultas[7])
            print(cursor.fetchall())
            input("Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('9'):
            cursor.execute(lista_consultas[8])
            print(cursor.fetchall())
            input("Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('z') or keyboard.is_pressed('Z'):
            cursor.execute(lista_consultas[9])
            print(cursor.fetchall())
            input("Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('x') or keyboard.is_pressed('X'):
            cursor.execute(lista_consultas[10])
            print(cursor.fetchall())
            input("Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('c') or keyboard.is_pressed('C'):
            cursor.execute(lista_consultas[11])
            print(cursor.fetchall())
            input("Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('v') or keyboard.is_pressed('V'):
            cursor.execute("""SELECT * FROM InfoDiscentes""")
            print(cursor.fetchall())
            input("Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('g') or keyboard.is_pressed('G'):
            cursor.execute(limpa_gatilho)
            cursor.execute(gatilho)
            input("Gatilho em funcionamento. Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('d') or keyboard.is_pressed('D'):
            codigo_vaga = str(input('Digite o codigo da vaga do Docente a ser aposentado:\n'))
            data_fim = str(input('Digite a data de aposentadoria do Docente:\n'))
            cursor.execute(fim_Docente,(data_fim,codigo_vaga,))
            input("Informação atualizada com sucesso. Pressione qualquer tecla para realizar uma nova operação.")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            imprime_opcoes()
        elif keyboard.is_pressed('Esc'):
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o conteudo da tela.
            break

def inicia_programa():  # Inicia as operações DDL, DML e SQL na base de dados.

    bancoUFRGS = sqlite3.connect('banco_UFRGS.db') # Realiza a conexão com o banco de dados.
    cursor = bancoUFRGS.cursor() # Cria o cursor correspondente à base de dados.

    bancoUFRGS.execute("PRAGMA FOREIGN_KEYS = OFF")
    cursor = prepara_banco(cursor) # Remove as tabelas já existentes no banco de dados, com nomes iguais aos das novas tabelas a serem inseridas.

    bancoUFRGS.execute("PRAGMA FOREIGN_KEYS = ON")
    cursor = instancia_tabelas(cursor) # Realiza as criações de todas as tabelas da base de dados.

    realiza_operacoes(cursor) # Permite ao usuário realizar as operações contidas no menu, na base de dados já criada.

    bancoUFRGS.commit()

def main():
    inicia_programa() # Inicia as operações DDL, DML e SQL na base de dados.
    os.system("PAUSE")

main()
