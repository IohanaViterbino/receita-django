from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.conf import settings
from django.contrib.auth.models import UserManager, AbstractUser, PermissionsMixin

class UserManager(UserManager):
    def create_user(self, email, username, cpf, password=None, **extra_fields):
        """
        Cria e salva um usuário com o email, nome de usuário, cpf e senha fornecidos.
        """
        if not email:
            raise ValueError('O campo Email deve ser preenchido')
        if not cpf:
            raise ValueError('O campo CPF deve ser preenchido')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, cpf, password=None, **extra_fields):
        """
        Cria e salva um superusuário com o email, nome de usuário, cpf e senha fornecidos.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário precisa ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário precisa ter is_superuser=True.')

        return self.create_user(email, username, cpf, password, **extra_fields)

class User(AbstractUser, PermissionsMixin):
    cpf = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cpf']

    objects = UserManager()

    def __str__(self):
        return self.username

class Categoria(models.Model):
    categoria = models.CharField(max_length=255, null=False, blank=False, validators=[MinLengthValidator(3)], unique=True)

    def __str__(self):
        return self.categoria

class Receita(models.Model):
    titulo = models.CharField(max_length=255, null=False, blank=False, validators=[MinLengthValidator(5)])
    descricao = models.TextField(null=True, blank=True, validators=[MaxLengthValidator(1000)])
    ingredientes = models.TextField(null=False, blank=False)
    modo_preparo = models.TextField(null=False, blank=False, validators=[MinLengthValidator(10)])
    tempo_preparo = models.TimeField(null=False, blank=False)
    publicado = models.BooleanField(default=False)
    fk_categoria = models.ManyToManyField(Categoria, related_name='receita', blank=False)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False, related_name='receita')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_categorias(self):
        return ", ".join([categoria.categoria for categoria in self.fk_categoria.all()])
    get_categorias.short_description = 'categorias' 

    def __str__(self):
        return f'{self.titulo} - {self.autor}'
    
class Avaliacao(models.Model):
    comentario = models.TextField(null=False, blank=False, validators=[MinLengthValidator(5)])
    fk_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='avaliacao')
    fk_receita = models.ForeignKey(Receita, on_delete=models.CASCADE, related_name='avaliacao')
    nota = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comentario