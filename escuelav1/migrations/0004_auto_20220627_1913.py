# Generated by Django 3.2.12 on 2022-06-27 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuelav1', '0003_alumnos_materia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesores',
            name='materia_impartida',
        ),
        migrations.AddField(
            model_name='profesores',
            name='materia_impartida',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='escuelav1.materias'),
        ),
    ]
