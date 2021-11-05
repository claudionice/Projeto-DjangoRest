from django.contrib import admin
from escola.models import alunos, curso

class AlunosAdmin (admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register (alunos, AlunosAdmin)


class CursoAdmin (admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register (curso, CursoAdmin)    

# Register your models here.
