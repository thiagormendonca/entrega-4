from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Usuario, Meta, Tarefa, FuncionarioTarefa

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        usuario = Usuario(
        nome=validated_data['nome'],
        matricula=validated_data['matricula'],
        funcao=validated_data['funcao']
        )
        usuario.set_password(validated_data['password'])
        usuario.save()
        Token.objects.create(user=usuario)
        return usuario

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'

class FuncionarioTarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionarioTarefa
        fields = '__all__'

class MetaSerializer(serializers.ModelSerializer):
    tarefas = TarefaSerializer(many=True, read_only=True)
    conclusao = serializers.SerializerMethodField('conclusao_field', read_only=True)

    def conclusao_field(self, meta):
        tarefas = Tarefa.objects.filter(meta=meta)
        concluidas = 0
        n = 0
        for i in tarefas:
            n += 1
            if i.concluido:
                concluidas += 1
        return (concluidas/n)*100

    class Meta:
        model = Meta
        fields = ('id', 'tarefas', 'nome', 'descricao', 'prazo', 'conclusao')