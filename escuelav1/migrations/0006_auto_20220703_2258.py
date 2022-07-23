# Generated by Django 3.2.12 on 2022-07-03 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuelav1', '0005_auto_20220703_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesores',
            name='apellido_profesor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profesores',
            name='email_profesor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profesores',
            name='materias_impartidas',
            field=models.ManyToManyField(through='escuelav1.Alumnos', to='escuelav1.Materias'),
        ),
        migrations.AddField(
            model_name='profesores',
            name='nombre_profesor',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]