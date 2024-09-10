from django.contrib import admin
from receita.models import Category, Rating, Recipe

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Rating)