# Generated by Django 4.1 on 2022-12-10 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Campus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuariomodels',
            old_name='password',
            new_name='contraseña',
        ),
    ]
