from .models import Categoria, Receita, Avaliacao, User
from rest_framework import serializers
from validate_docbr import CPF
import re
from datetime import time

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'cpf', 'address']
	
		def validate(self, dados):
			cpf = CPF()
			regex_email = re.compile(r'[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?', re.IGNORECASE)
			regex_nome = re.compile(r'^[a-zA-Z ]+$', re.IGNORECASE)

			if re.match(regex_email, dados['email']) == None:
				raise serializers.ValidationError({'email':'O email não está no formato correto!'})
			if re.match(regex_nome, dados['username']) == None:
				raise serializers.ValidationError({'nome':'O nome deve conter apenas letras!'})
			if not cpf.validate(dados['cpf']):
				raise serializers.ValidationError({'cpf':'O cpf deve ter 11 digitos numéricos válidos!'})
			return dados


class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = '__all__'

		def validate_categoria(self, categoria):
			regex_categoria = re.compile(r'^[a-zA-Z ]+$', re.IGNORECASE)
			if re.match(regex_categoria, categoria) == None:
				raise serializers.ValidationError('A categoria deve conter apenas letras!')
		
class ReceitaSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Receita
		fields = '__all__'

		def validate_ingredientes(self, ingredientes):
			if len(ingredientes.split(',')) < 2:
				raise serializers.ValidationError('A lista de ingredientes deve conter pelo menos dois itens separados por vírgula.')
			
		def validate_tempo_preparo(value):
			if value <= time(0, 0):
				raise serializers.ValidationError('O tempo de preparo deve ser maior que zero.')
			if value >= time(23, 59):
				raise serializers.ValidationError('O tempo de preparo deve ser inferior a 24 horas.')

class AvaliacaoSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Avaliacao
		fields = '__all__'