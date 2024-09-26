from .models import Categoria, Receita, Avaliacao, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username']

class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = '__all__'
		
class ReceitaSerializer(serializers.ModelSerializer):
	user = UserSerializer(source='autor',read_only=True)
	categoria = CategoriaSerializer(source='fk_categoria',read_only=True)
	
	class Meta:
		model = Receita
		fields = '__all__'

class AvaliacaoSerializer(serializers.ModelSerializer):
	user = UserSerializer(source='fk_usuario', read_only=True)
	recipe = ReceitaSerializer(source='fk_recipe', read_only=True)
	
	class Meta:
		model = Avaliacao
		fields = '__all__'