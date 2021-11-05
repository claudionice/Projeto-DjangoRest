from rest_framework import serializers 
from escola.models import alunos, curso


class AlunoSerializer (serializers.ModelSerializers):
    class Meta ():
        model= alunos
        fields = '__all__'

class CursoSerializer (serializers.ModelSerializers):
    class Meta ():
        model= curso 
        fields = '__all__'

