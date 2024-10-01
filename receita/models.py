from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome
    
class Receita(models.Model):
    titulo = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)
    ingredientes = models.TextField(null=False, blank=False)
    modo_preparo = models.TextField(null=False, blank=False)
    tempo_preparo = models.TimeField(null=False, blank=False)
    publicado = models.BooleanField(default=False)
    fk_categoria = models.ManyToManyField(Categoria, related_name='categorias')
    autor = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, blank=False, related_name='recipe')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_categorias(self):
        return ", ".join([categoria.nome for categoria in self.fk_categoria.all()])
    get_categorias.short_description = 'categorias' 

    def __str__(self):
        return f'{self.titulo} - {self.autor}'
    
class Avaliacao(models.Model):
    comentario = models.TextField(null=True, blank=True)
    fk_usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='rating')
    fk_receita = models.ForeignKey(Receita, on_delete=models.CASCADE, related_name='rating')
    nota = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    
    def __str__(self):
        return self.comentario