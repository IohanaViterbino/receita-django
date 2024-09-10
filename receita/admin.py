from django.contrib import admin
from receita.models import Category, Rating, Recipe

# Corrigindo o nome das classes de admin para seguir a convenção de nomenclatura
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'publicado', 'autor', 'fk_categoria')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'autor',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'nota', 'fk_usuario', 'fk_receita')
    list_display_links = ('id', 'nota')
    search_fields = ('nota', 'fk_usuario', 'fk_usuario',)

# Registrando os modelos com suas classes personalizadas no Django Admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Rating, RatingAdmin)
