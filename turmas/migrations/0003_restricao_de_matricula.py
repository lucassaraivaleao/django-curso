# Generated by Django 4.0.3 on 2022-03-16 04:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turmas', '0002_criacao_matricula'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matricula',
            options={'ordering': ['turma', 'data']},
        ),
        migrations.AlterUniqueTogether(
            name='matricula',
            unique_together={('usuario', 'turma')},
        ),
    ]
