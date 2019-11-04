from django.urls import path
from .views import UserCreate, LoginView, MetaViewSet, ConcluirTarefa, TarefaViewSet, AssociarFuncionario
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('meta', MetaViewSet, base_name='meta')
router.register('tarefa', TarefaViewSet, base_name='tarefa')

urlpatterns = [
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),
    path('tarefa/<int:pk>/concluir/', ConcluirTarefa.as_view(), name='concluir_tarefa'),
    path('tarefa/<int:pk>/funcionario/', AssociarFuncionario.as_view(), name='associar_funcionario'),
]

urlpatterns += router.urls