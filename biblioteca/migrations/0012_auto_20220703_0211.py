# Generated by Django 3.2.12 on 2022-07-03 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0011_alter_prestatario_libros_prestados'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestatario',
            name='libros_prestados',
        ),
        migrations.RemoveField(
            model_name='prestatario',
            name='nombre',
        ),
    ]
