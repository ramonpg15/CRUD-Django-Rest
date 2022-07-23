from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from escuelav1.views import add_materias
from rest_framework.test import APITestCase
from rest_framework import status
client = Client()


class TestURL(SimpleTestCase):
    # def test_ver_materia(self):
    #     print('--------------------Test de url para ver materia-----------------------------')
    #     url = reverse('ver_materia',kwargs={'ver_materia': {'materia'}})
    #     #print(resolve(url))
    #     self.assertEquals(resolve(url).func, ver_materia)
    #     print('----------------Fin de Test de url para ver materia--------------------------')

    def test_create(self):
        print('----------------Test de url para crear materias-------------------------------')
        
        url = reverse('add-materias')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_materias)
        print('----------------Fin de Test de url para crear materias------------------------')
    
        
class TestRegistroLibro(APITestCase):
    print('------------------Inici test de libros----------------')
    
    def test_registro_libros(self):
        data = {
            "nombre_libro": "El arte de la guerra",
            "autor": "Tzu",
        }
        
        response = self.client.post('http://127.0.0.1:8000/biblioteca/create_libros/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    print('-------------Fin de test de libross--------------------')