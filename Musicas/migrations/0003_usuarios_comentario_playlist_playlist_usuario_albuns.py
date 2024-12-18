# Generated by Django 5.0.3 on 2024-11-22 05:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musicas', '0002_comentario_playlist_alter_musicas_album_and_more'),
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=9)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Musicas.playlist'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Usuarios.usuarios'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Albuns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('musicas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musicas.musicas')),
            ],
        ),
    ]
