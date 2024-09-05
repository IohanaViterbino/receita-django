from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)

class Recipe(models.Model):
    titulo = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)
    ingredientes = models.TextField(null=False, blank=False)
    modo_preparo = models.TextField(null=False, blank=False)
    tempo_preparo = models.IntegerField(null=False, blank=False)
    publicado = models.BooleanField(default=False)
    fk_categoria = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True, blank=False, related_name='receita')
    autor = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, blank=False, related_name='receita')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Rating(models.Model):
    comentario = models.TextField(null=True, blank=True)
    fk_usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='classificao')
    fk_receita = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='classificao')
    nota = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])