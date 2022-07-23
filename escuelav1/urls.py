from django.urls import path
from .api import RegisterApi
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('api/register', RegisterApi.as_view()),
    path('', views.ApiView, name='home'),
    # url de la vista creada
    path('create/', views.add_materias, name='add-materias'),
    path('all_materias/', login_required(views.ver_materias), name='ver_materias'),
    path('view_materia/<int:pk>/', views.ver_materia, name='ver_materia'),
    path('update/<int:pk>/', views.actualizar_materias, name='actualizar-materias'),
    path('materia/<int:pk>/delete/', views.eliminar_materia, name='eliminar-materias'),
    path('all_alumnos/', views.ver_alumnos, name='Ver alumnos'),
    path('create_alumno/', views.add_alumnos, name='Add Alumno'),
    path('update_alumno/<int:pk>/', views.actualizar_alumnos, name='Actualiza alumnos'),
    path('delete_alumno/<int:pk>/', views.eliminar_alumno, name='Eliminar alumno'),
    path('create_profesor/', views.add_profesor, name='add-profesor'),
    path('all_profesores/', views.ver_profesores, name='Ver_profesores'),
    path('update_profesor/<int:pk>/', views.actualizar_profesor, name='actualizar-profesor'),
    path('delete_profesor/<int:pk>/', views.eliminar_profesor, name='Eliminar-profesor')
    # path('materia/<int:pk>/', actualizar_materia.as_view())
]
