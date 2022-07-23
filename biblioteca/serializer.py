from .models import Libros, Prestatario, Prestamos
from rest_framework import serializers


class LibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = '__all__'


class PrestatarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestatario
        fields = '__all__'
  

class PrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamos
        fields = '__all__'