# Generated by Django 4.2.16 on 2024-12-02 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musicas', '0009_rename_albuns_comentario_playlist_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='usuario',
            new_name='usuarios',
        ),
    ]