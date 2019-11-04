from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    username = None
    nome = models.CharField(max_length=30)
    matricula = models.IntegerField(unique=True)
    gerente = models.BooleanField(default=False)
    funcao = models.TextField(blank=True)

    USERNAME_FIELD = 'matricula'