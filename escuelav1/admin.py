from django.contrib import admin

# Register your models here.
# registrar el modelos que creamos aqui

# from django.contrib import admin
from .models import Alumnos, Materias, Profesores

admin.site.register(Alumnos)
admin.site.register(Profesores)
admin.site.register(Materias)