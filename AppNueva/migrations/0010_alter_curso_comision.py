# Generated by Django 5.1 on 2024-08-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNueva', '0009_remove_estudiante_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='comision',
            field=models.IntegerField(),
        ),
    ]
