from django.db import models

class alunos (models.Model):
    nome = models.CharField (max_length=30)
    rg = models.CharField (max_length=9)
    cpf = models.CharField (max_length=11)
    data_nascimento = models.DateField ()

    def _str_ (self):
        return self.nome 

class curso (models.Model):
    NIVEL = (
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A', 'Avancado'),
    )
    codigo_curso= models.CharField (max_length = 10)
    descricao= models.CharField (max_length = 100)
    nivel= models.CharField (max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def _str_ (self):
        return self.descricao






# Create your models here.
