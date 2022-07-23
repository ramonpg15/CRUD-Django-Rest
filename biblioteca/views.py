# importados un decorador
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Libros
from .serializer import LibrosSerializer
from rest_framework import status, serializers
from django.contrib.auth.decorators import login_required


# * Se agrego la url para que puedan consultar un libro por su pk
@api_view(['GET'])
def view(request):
    api_urls = {
        'all_libros': '/all_libros/',
        'add_libro': '/create_libro/',
        'ver_libro': '/ver_libro/pk/',
        'update_libro': '/update_libro/pk/',
        'delete_libro': '/delete_libro/pk/'
    }
    return Response(api_urls)


@api_view(['POST'])
def add_libros(request):
    libro = LibrosSerializer(data=request.data)
    if Libros.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Este libro ya existe')
    if libro.is_valid():
        libro.save()
        return Response(libro.data, status=status.HTTP_201_CREATED)
    else:
        return Response(libro.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required
@api_view(['GET'])
def ver_libros(request):
    libro = Libros.objects.all()
    serializer = LibrosSerializer(libro, many=True)
    return Response({'libros': serializer.data})


# * Agregando funcion para ver libro por pk
@api_view(['GET'])
def ver_libro(request, pk):
    libro = Libros.objects.get(pk=pk)
    serializer = LibrosSerializer(libro)
    return Response({'libro': serializer.data})


# * Agregando funcion para actualizar un libro
@api_view(['PUT'])
def actualizar_libro(request, pk):
    libro = Libros.objects.get(pk=pk)
    data = LibrosSerializer(instance=libro, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response({'Error, libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)


# * Agregando funcion para eliminar libro
@api_view(['DELETE'])
def eliminar_libro(request, pk):
    libro = Libros.objects.get(pk=pk)
    if libro:
        libro.delete()
        Response({"message": 'Eliminado'})
    return Response(status=status.HTTP_404_NOT_FOUND)
