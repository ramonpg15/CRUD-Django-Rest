# Generated by Django 3.2.12 on 2022-07-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0008_alter_prestatario_libros_prestados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestatario',
            name='libros_prestados',
            field=models.ManyToManyField(through='biblioteca.Prestamos', to='biblioteca.Libros'),
        ),
    ]
