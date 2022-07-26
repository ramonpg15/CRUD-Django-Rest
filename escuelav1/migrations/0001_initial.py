# Generated by Django 3.2.12 on 2022-06-23 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('boleta', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='materias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200)),
                ('cupos', models.CharField(max_length=2)),
                ('area', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='profesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('materia_impartida', models.CharField(max_length=100)),
            ],
        ),
    ]
