# Generated by Django 5.0.3 on 2024-11-22 21:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musicas', '0004_remove_albuns_musicas_remove_musicas_album_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicasAlbuns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albuns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musicas.albuns')),
                ('musicas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musicas.musicas')),
            ],
        ),
    ]
