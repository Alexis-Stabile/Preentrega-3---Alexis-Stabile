# Generated by Django 5.1 on 2024-08-21 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppNueva', '0010_alter_curso_comision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='comision',
        ),
    ]
