# Generated by Django 4.0.3 on 2022-03-12 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=32)),
                ('titulo', models.CharField(max_length=32)),
                ('youtube_link', models.CharField(max_length=50)),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
