# Generated by Django 5.1.1 on 2024-09-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0003_alter_rating_fk_receita_alter_rating_fk_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tempo_preparo',
            field=models.TimeField(),
        ),
    ]
