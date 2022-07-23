from django.shortcuts import get_object_or_404
# importados un decorador
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Alumnos, Materias, Profesores
from .serializer import AlumnosSerializer, ProfesoresSerializer, MateriasSerializer
from rest_framework import status, serializers, permissions
from django.contrib.auth.decorators import login_required
# Create your views here.

# usando el decorador


@api_view(['GET'])
def ApiView(request):
    api_urls = {
        'all_materias': '/all_materias/',
        'view_materia': 'view_materia/pk/',
        'add_materia': '/create/',
        'update_materia': '/update/pk/',
        'delete_materia': '/materia/pk/delete/',
        'all_alumnos': 'all_alumnos/',
        'add_alumno': 'create_alumno/',
        'update_alumno': 'update_alumno/pk/',
        'delete_alumno': 'delete_alumno/pk/',
        'all_profesores': 'all_profesores/',
        'update_profesor': 'update_profesor/pk/',
        'delete_profesor': 'delete_profesor/pk/'
    }
    return Response(api_urls)


""" Funcion para hacer una insercion a la base de datos """


@api_view(['POST'])
def add_materias(request):
    materia = MateriasSerializer(data=request.data)
    if Materias.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Esta materia ya existe')
    if materia.is_valid():
        materia.save()
        return Response(materia.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


""" Funcion para visualizar los objetos que hemos insertado a nuestra bd """


@login_required
@api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
def ver_materias(request):
    materia = Materias.objects.all()
    serializer = MateriasSerializer(materia, many=True)
    return Response({'materias': serializer.data})


""" Para ver solo una materia por pk """


@api_view(['GET'])
# @login_required
# @permission_classes([permissions.IsAuthenticated])
def ver_materia(request, pk):
    materia = Materias.objects.get(pk=pk)
    print(materia)
    serializer = MateriasSerializer(materia)
    # return Response({'materia': serializer.data})
    return Response(serializer.data)


""" Usamos el metodo POST para actualizar un elemnto en particular de la bd """


@api_view(['PUT'])
# @login_required
# @permission_classes([permissions.IsAuthenticated])
def actualizar_materias(request, pk):
    materia = Materias.objects.get(pk=pk)
    data = MateriasSerializer(instance=materia, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


""" Funcion para eliminar una materia """


@api_view(['DELETE'])
# @permission_classes([permissions.IsAuthenticated])
def eliminar_materia(request, pk):
    materia = get_object_or_404(Materias, pk=pk)
    materia.delete()
    return Response({'Materia eliminada'})
    # return Response(status=status.HTTP_204_NO_CONTENT)


# -------Alumnos---------

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def ver_alumnos(request):
    alumno = Alumnos.objects.all()
    serializer = AlumnosSerializer(alumno, many=True)
    return Response({'alumnos': serializer.data})


@api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
def add_alumnos(request):
    alumno = AlumnosSerializer(data=request.data)
    if Alumnos.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Este alumno ya existe')
    if alumno.is_valid():
        alumno.save()
        return Response(alumno.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
# @permission_classes([permissions.IsAuthenticated])
def actualizar_alumnos(request, pk):
    alumno = Alumnos.objects.get(pk=pk)
    data = AlumnosSerializer(instance=alumno, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
# @permission_classes([permissions.IsAuthenticated])
def eliminar_alumno(request, pk):
    alumno = get_object_or_404(Alumnos, pk=pk)
    alumno.delete()
    return Response(status=status.HTTP_404_NOT_FOUND)

# -------------------Profesores--------------------------


@api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
def ver_profesores(request):
    profesor = Profesores.objects.all()
    serializer = ProfesoresSerializer(profesor, many=True)
    return Response({'profesores': serializer.data})


@api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
def add_profesor(request):
    profesor = ProfesoresSerializer(data=request.data)
    if Profesores.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Este profesor ya existe')
    if profesor.is_valid():
        profesor.save()
        return Response(profesor.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
# @permission_classes([permissions.IsAuthenticated])
def actualizar_profesor(request, pk):
    profesor = Profesores.objects.get(pk=pk)
    data = ProfesoresSerializer(instance=profesor, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

  
@api_view(['DELETE'])
# @permission_classes([permissions.IsAuthenticated])
def eliminar_profesor(request, pk):
    profesor = get_object_or_404(Profesores, pk=pk)
    profesor.delete()
    return Response(status=status.HTTP_404_NOT_FOUND)