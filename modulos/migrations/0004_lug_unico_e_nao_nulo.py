# Generated by Django 4.0.3 on 2022-03-13 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0003_populando_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
