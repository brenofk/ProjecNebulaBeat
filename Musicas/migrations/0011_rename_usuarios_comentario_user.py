# Generated by Django 4.2.16 on 2024-12-02 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musicas', '0010_rename_usuario_comentario_usuarios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='usuarios',
            new_name='user',
        ),
    ]
