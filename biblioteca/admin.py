from django.contrib import admin

# Register your models here.
from .models import Libros, Prestatario, Prestamos

admin.site.register(Libros)
admin.site.register(Prestatario)
admin.site.register(Prestamos)
