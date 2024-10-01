from django.contrib import admin
from receita.models import Categoria, Receita, Avaliacao

# Corrigindo o nome das classes de admin para seguir a convenção de nomenclatura
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'publicado', 'autor', 'get_categorias')
    list_filter = ['autor', 'publicado']
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'autor',)

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nota', 'fk_usuario', 'fk_receita', 'updated_at')
    list_filter = ['fk_usuario', 'nota']
    list_display_links = ('id', 'nota')
    search_fields = ('nota', 'fk_usuario', 'fk_usuario',)

# Registrando os modelos com suas classes personalizadas no Django Admin
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)
