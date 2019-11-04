from django.shortcuts import render

# Create your views here.

from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from .serializers import UsuarioSerializer, MetaSerializer, TarefaSerializer, FuncionarioTarefaSerializer
from .models import Meta, FuncionarioTarefa, Tarefa, Usuario

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UsuarioSerializer

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        matricula = request.data.get("matricula")
        senha = request.data.get("senha")
        usuario = authenticate(username=matricula, password=senha)
        if usuario:
            return Response({"token": usuario.auth_token.key})
        else:
            return Response({"error": "Usuário ou senha inválidos"}, status=status.HTTP_400_BAD_REQUEST)

class MetaViewSet(viewsets.ModelViewSet):
    queryset = Meta.objects.all()
    serializer_class = MetaSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

    def create(self, request):
        meta = get_object_or_404(Meta, pk=request.data.get('meta'))
        tarefa = Tarefa(meta=meta, descricao=request.data.get('descricao'))
        tarefa.save()
        data = TarefaSerializer(tarefa).data
        return Response(data)

class ConcluirTarefa(APIView):
    serializer_class = FuncionarioTarefaSerializer

    def patch(self, request, pk):
        instance = FuncionarioTarefa.objects.get(tarefa=pk, funcionario=request.user.pk)
        instance.concluido = True
        instance.save()
        
        data = FuncionarioTarefaSerializer(instance).data

        functarefa = FuncionarioTarefa.objects.filter(tarefa=pk)
        concluido = True
        for i in functarefa:
            if not i.concluido:
                concluido = False
                break
        if concluido:
            tarefa = Tarefa.objects.get(pk=pk)
            tarefa.concluido = True
            tarefa.save()

        return Response(data)

class AssociarFuncionario(APIView):
    def post(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        funcionario = get_object_or_404(Usuario, matricula=request.data.get('matricula'))
        ft = FuncionarioTarefa.objects.filter(tarefa=tarefa, funcionario=funcionario)
        if ft:
            return Response({"error": "Funcionário já associado a essa tarefa!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            functarefa = FuncionarioTarefa(tarefa=tarefa, funcionario=funcionario)
            functarefa.save()

            data = FuncionarioTarefaSerializer(functarefa).data

            return Response(data)