# Generated by Django 4.2.16 on 2024-12-02 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musicas', '0011_rename_usuarios_comentario_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='user',
            new_name='usuarios',
        ),
    ]
