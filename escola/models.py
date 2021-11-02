from django.db import models

class Alunos (models.model):
    nome = models.CharField (max_lenght=30)
    rg = models.CharField (max_lenght=9)
    cpf = models.CharField (max_lenght=11)
    data_nascimento = models.DateField ()

    def _str_ (self):
        return self.nome 



# Create your models here.
