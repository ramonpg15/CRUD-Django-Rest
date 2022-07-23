from django.urls import path
from . import views

urlpatterns = [
    # path('create/', views.add_libros, name='add-libros'),
    path('all_libros/', views.ver_libros, name='ver_libros'),
    path('', views.view, name='all'),
    path('create_libros/', views.add_libros, name='Add libros'),
    # * Agregando url para ver libro por pk
    path('view_libro/<int:pk>/', views.ver_libro, name='ver_libro'),
    path('update_libro/<int:pk>/', views.actualizar_libro, name='Actualizar libro'),
    path('delete_libro/<int:pk>/', views.eliminar_libro, name='Elimina libro')
]