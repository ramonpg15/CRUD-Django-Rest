# Generated by Django 3.2.12 on 2022-07-03 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0013_auto_20220703_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestatario',
            name='libros_prestados',
            field=models.ManyToManyField(through='biblioteca.Prestamos', to='biblioteca.Libros'),
        ),
    ]
