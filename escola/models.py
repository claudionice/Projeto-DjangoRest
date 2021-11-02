from django.db import models

class Alunos (models.model):
    nome = models.CharField (max_lenght=30)
    rg = models.CharField (max_lenght=9)
    cpf = models.CharField (max_lenght=11)
    data_nascimento = models.DateField ()

    def _str_ (self):
        return self.nome 

class Curso (models.Model):
    NIVEL = (
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A', 'Avancado'),
    )
    codigo_curso = models.CharField (max_lenght = 10)
    descricao = models.CharField (max_lenght = 100)
    nivel = model.CharField (max_lenght = 1, choices = NIVEL, blank = False, Null = False, default = 'B')

    




# Create your models here.
