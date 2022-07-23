
from django.db import models

# Create your models here.
# Aqui empezaremos a crear los modelos


class Materias(models.Model):

    MATERIAS = [
        ('EC', 'Economia'),
        ('PO', 'Programacion'),
        ('BD', 'Base de datos'),
        ('FI', 'Fisica'),
        ('IA', 'Inteligencia artificial'),
        ('QI', 'Quimica'),
        ('PL', 'Programacion Lineal'),
        ('IP', 'Ingenieria de pruebas'),
        ('RE', 'Redes'),
        ('SI', 'Seguridad informatica'),
        ('SO', 'Sistemas operativos'),
        ('MI', 'Metodologia de la investigacion'),
    ]

    materia = models.CharField(max_length=100, blank=True, choices=MATERIAS)
    cupos = models.CharField(max_length=2)
    area = models.CharField(max_length=100)
    # definir un str para impirmir los datos

    def __str__(self) -> str:
        return f'{self.area}'


class Profesores(models.Model):
    
    # materia_impartida = models.ForeignKey(Materias,on_delete=models.CASCADE,null=True)
    materias_impartidas = models.ManyToManyField(Materias, through='Alumnos')
    nombre_profesor = models.CharField(max_length=100, blank=True)
    # apellido_profesor = models.CharField(max_length=100,blank=True)
    email_profesor = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f'{self.nombre_profesor} {self.email_profesor} '


class Alumnos(models.Model):
    materia_cursada = models.ForeignKey(Materias, on_delete=models.CASCADE, null=True)
    profesor_asignado = models.ForeignKey(Profesores, on_delete=models.CASCADE, null=True)
    nombre_alumno = models.CharField(max_length=100)
    email_alumno = models.CharField(max_length=100)
    boleta_alumno = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.nombre_alumno} {self.materia_cursada} {self.profesor_asignado}"