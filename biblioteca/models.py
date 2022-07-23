from django.db import models
# from django.contrib.auth.models import User


# Create your models here.
class Libros(models.Model):
    nombre_libro = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    # editorial=models.CharField(max_length=100)
    is_prestado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Libro: {self.nombre_libro}, Autor: {self.autor}'


class Prestatario(models.Model):
    # libro_prestado = models.ForeignKey(Libros, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100, null=True)
    libros_prestados = models.ManyToManyField(Libros, through='Prestamos')
    # apellido=models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'Nombre del prestatario: {self.nombre}'


# libro_id,prestatario_id
class Prestamos(models.Model):
    fecha_prestamo = models.DateField(auto_now_add=True)
    nombre_libro_prestado = models.ForeignKey(Libros, on_delete=models.CASCADE, null=True)
    nombre_prestatario = models.ForeignKey(Prestatario, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'Nombre de libro prestado: {self.nombre_libro_prestado}, Fecha de prestamo: {self.fecha_prestamo}, Prestado a {self.nombre_prestatario}'