# Generated by Django 3.2.12 on 2022-06-26 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuelav1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesores',
            name='materia_impartida',
        ),
        migrations.AddField(
            model_name='profesores',
            name='materia_impartida',
            field=models.ManyToManyField(to='escuelav1.materias'),
        ),
    ]
