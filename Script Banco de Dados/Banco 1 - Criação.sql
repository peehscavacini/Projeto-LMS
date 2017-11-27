CREATE DATABASE LMS_FACULDADE;

GO 

USE LMS_FACULDADE;

GO

CREATE TABLE USUARIO (
    id    integer identity(1,1) not null,
	ra	  integer not null,
	password varchar(255) not null,
    nome  varchar(150) not null,
	email varchar(50) not null,
	celular char(11),
	perfil char(1) not null,
	ativo bit not null default 1,
    CONSTRAINT pk_usuario primary key (id),
    CONSTRAINT un_usuario UNIQUE (ra)
);

CREATE TABLE PROFESSOR (
    usuario_id  integer not null primary key,
    apelido varchar(3) not null,
    CONSTRAINT uq_professor UNIQUE (apelido),
    CONSTRAINT fk_professor_usuario
    FOREIGN KEY (usuario_id)
    REFERENCES USUARIO (id)
);


CREATE TABLE COORDENADOR (
    usuario_id  integer not null,
    sala	varchar(3) not null,
    CONSTRAINT pk_coordenador primary key (usuario_id),
    CONSTRAINT fk_coordenador_usuario
    FOREIGN KEY (usuario_id)
    REFERENCES USUARIO (id)
);

CREATE TABLE CURSO (
    id    integer identity(1,1) not null,
    sigla varchar(5) not null,
    nome  varchar(50) not null,
	CONSTRAINT pk_curso PRIMARY KEY (id),
    CONSTRAINT un_curso_sigla UNIQUE (sigla),
    CONSTRAINT un_curso_nome UNIQUE (nome)
);

CREATE TABLE GRADE_CURRICULAR (
    id integer identity not null ,
    curso_id integer not null,
    ano smallint not null,
    semestre char(1) not null,
	CONSTRAINT pk_grade_curricular PRIMARY KEY (id),
    CONSTRAINT un_grade_curricular UNIQUE (ano, semestre, curso_id),
    CONSTRAINT fk_grade_curricular_curso
    FOREIGN KEY (curso_id)
    REFERENCES CURSO (id)
);

CREATE TABLE PERIODO (
    id integer identity(1,1) not null,
    grade_curricular_id integer not null,
    numero tinyint not null,
	CONSTRAINT pk_periodo_ PRIMARY KEY (id),
    CONSTRAINT periodo_unique UNIQUE (grade_curricular_id, numero),
    CONSTRAINT fk_periodo_grade_curricular
    FOREIGN KEY (grade_curricular_id)
    REFERENCES GRADE_CURRICULAR (id)
);

CREATE TABLE ALUNO (
    usuario_id  integer not null,
    curso_id integer not null,
    CONSTRAINT pk_aluno primary key (usuario_id),
    CONSTRAINT fk_aluno_usuario
    FOREIGN KEY (usuario_id)
    REFERENCES USUARIO (id),
    CONSTRAINT fk_aluno_curso
    FOREIGN KEY (curso_id)
    REFERENCES CURSO (id)
);

CREATE TABLE DISCIPLINA (
    id integer identity(1,1) not null primary key,
    nome varchar(240) not null,
    carga_horaria TINYINT not null,
    teoria DECIMAL(3),
    pratica DECIMAL(3),
    competencias TEXT,
    habilidades TEXT,
    conteudo TEXT,
    bibliografia_basica TEXT,
    bibliografia_complementar TEXT,
    CONSTRAINT disciplina_unique UNIQUE (nome)
);

CREATE TABLE PERIODO_DISCIPLINA (
    periodo_id integer not null,
    disciplina_id integer not null,
    CONSTRAINT pk_periodo PRIMARY KEY (periodo_id, disciplina_id),
    CONSTRAINT fk_periodo_disciplina_periodo
    FOREIGN KEY (periodo_id) REFERENCES PERIODO (id),
    CONSTRAINT fk_periodo_disciplina_disciplina
    FOREIGN KEY (disciplina_id) REFERENCES DISCIPLINA (id)
);

CREATE TABLE DISCIPLINA_OFERTADA (
    id integer identity(1,1) not null,
    disciplina_id integer not null,
    ano smallint not null,
    semestre CHAR(1) not null
	CONSTRAINT pk_disciplina_ofertada PRIMARY KEY (id),
    CONSTRAINT uq_disciplina_ofertada UNIQUE (disciplina_id, ano, semestre),
    CONSTRAINT fk_disciplina_ofertada_disciplina
    FOREIGN KEY (disciplina_id) REFERENCES DISCIPLINA (id)
);

CREATE TABLE TURMA (
    id  integer identity(1,1) not null,
    disciplina_ofertada_id integer not null,
    identificador CHAR(1) not null,
    turno VARCHAR(15),
    professor_id integer,
	CONSTRAINT pk_turma PRIMARY KEY (id),
    CONSTRAINT uq_turma UNIQUE (disciplina_ofertada_id, identificador),
    CONSTRAINT fk_turma_disciplina_ofertada
    FOREIGN KEY (disciplina_ofertada_id) REFERENCES DISCIPLINA_OFERTADA (id),
    CONSTRAINT fk_turma_professor
    FOREIGN KEY (professor_id) REFERENCES PROFESSOR (usuario_id)
);

CREATE TABLE CURSO_TURMA (
    curso_id  integer not null,
    turma_id integer not null,
    CONSTRAINT pk_curso_turma primary key (curso_id, turma_id),
    CONSTRAINT fk_curso_turma_curso
    FOREIGN KEY (curso_id)
    REFERENCES CURSO (id),
    CONSTRAINT fk_curso_turma_turma
    FOREIGN KEY (turma_id)
    REFERENCES TURMA (id)
);

CREATE TABLE MATRICULA (
    aluno_id  integer not null,
    turma_id integer not null,
    CONSTRAINT pk_matricula primary key (aluno_id, turma_id),
    CONSTRAINT fk_matricula_aluno
    FOREIGN KEY (aluno_id)
    REFERENCES ALUNO (usuario_id),
    CONSTRAINT fk_matricula_turma
    FOREIGN KEY (turma_id)
    REFERENCES TURMA (id)
);

