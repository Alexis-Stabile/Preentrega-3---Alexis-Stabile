# Generated by Django 5.1 on 2024-08-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNueva', '0012_alter_curso_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='comision',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
