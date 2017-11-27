from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, ra, password, **extra_fields):
        if not ra:
            raise ValueError('RA precisa ser preenchido')
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, ra, password=None, **extra_fields):
        return self._create_user(ra, password, **extra_fields)

    def create_superuser(self, ra, password, **extra_fields):
        return self._create_user(ra, password, **extra_fields)


class Usuario(AbstractBaseUser):
    nome = models.CharField('Nome', max_length=100, blank=True)
    ra = models.IntegerField('RA', unique=True)
    password = models.CharField(max_length=150)
    user_type = models.CharField(
        'Tipo de usuário', max_length=1, default='C')
    ativo = models.BooleanField('Ativo', default=True)
    email = models.EmailField('E-mail', unique=True)

    def __str__(self):
        return self.nome

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.user_type == 'C'

    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome', 'email']
    objects = UsuarioManager()


class Disciplina(models.Model):
    nome = models.CharField(db_column='NOME', unique=True, max_length=240)  # Field name made lowercase.
    carga_horaria = models.SmallIntegerField(db_column='CARGA_HORARIA')  # Field name made lowercase.
    teoria = models.DecimalField(db_column='TEORIA', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pratica = models.DecimalField(db_column='PRATICA', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    competencias = models.TextField(db_column='COMPETENCIAS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilidades = models.TextField(db_column='HABILIDADES', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conteudo = models.TextField(db_column='CONTEUDO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Disciplina'

    def __str__(self):
        return self.nome


class Professor(Usuario):
    parent_link = models.OneToOneField(Usuario, primary_key=True, db_column='user_id', parent_link=True)
    celular = models.CharField('Celular', max_length=11, null=True)
    apelido = models.CharField('Apelido', max_length=30, null=False, unique=True)

    def __str__(self):
        return format(self.nome)

class Coordenador(Usuario):
    parent_link = models.OneToOneField(Usuario, primary_key=True, db_column='user_id', parent_link=True)
    sala = models.CharField(max_length=3)

    def __str__(self):
        return format(self.nome)



class DisciplinaOfertada(models.Model):
    disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING)  # Field name made lowercase.
    ano = models.SmallIntegerField(db_column='ANO')  # Field name made lowercase.
    semestre = models.CharField(db_column='SEMESTRE', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disciplina_Ofertada'
        unique_together = (('ano', 'semestre','disciplina'),)



    def __str__(self):
        return format(self.disciplina)
    

###########################################################################
class Turma(models.Model):
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING)
    identificador = models.CharField(max_length=1)
    turno = models.CharField(max_length=15, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'TURMA'
        unique_together = (('disciplina_ofertada', 'identificador'),)

    def __str__(self):
        return self.identificador  
##########################################################################

class Curso(models.Model):
    sigla = models.CharField(unique=True, max_length=5)
    nome = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'CURSO'

    def __str__(self):
        return self.nome


class Aluno(Usuario):
    parent_link = models.OneToOneField(
        Usuario, primary_key=True, db_column='user_id', parent_link=True)
    curso = models.ForeignKey(Curso, blank=True, null=False)
    celular = models.CharField('Celular', max_length=11, null=False)
    semestre = models.IntegerField('Semestre', null=False, default=1)
    turma = models.ManyToManyField(to=Turma, through='Matricula')

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    ra_aluno = models.ForeignKey(
        'Aluno', models.DO_NOTHING, db_column='ra_aluno', blank=True, null=True)
    nome_disciplina = models.ForeignKey(
        'Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey(
        'DisciplinaOfertada', models.DO_NOTHING, db_column='ano_ofertado', blank=True, null=True, related_name='+')
    semestre_ofertado = models.ForeignKey(
        'DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True, related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'matricula'
        unique_together = (('ra_aluno', 'nome_disciplina',
                            'ano_ofertado', 'semestre_ofertado', 'id_turma'),)


class CursoTurma(models.Model):
    sigla_curso = models.ForeignKey(
        'Curso', models.DO_NOTHING, db_column='sigla_curso', blank=True, null=True)
    nome_disciplina = models.ForeignKey(
        'Disciplina', models.DO_NOTHING, db_column='nome_disciplina', blank=True, null=True)
    ano_ofertado = models.ForeignKey(
        'DisciplinaOfertada', models.DO_NOTHING, db_column='ano_ofertado', blank=True, null=True, related_name='+')
    semestre_ofertado = models.ForeignKey(
        'DisciplinaOfertada', models.DO_NOTHING, db_column='semestre_ofertado', blank=True, null=True, related_name='+')
    id_turma = models.ForeignKey(
        'Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'curso_turma'
        unique_together = (('sigla_curso', 'nome_disciplina',
                            'ano_ofertado', 'semestre_ofertado', 'id_turma'),)