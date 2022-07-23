
import json
# from typing_extensions import Self
from django.test import Client, TestCase
from django.urls import reverse
from escuelav1.models import Materias
from escuelav1.serializer import MateriasSerializer


class test_creacion_materias(TestCase):

    def test_crear_materia(self, materia="QI", cupos="20", area="Quimica"):
        print('Inicio test de creacion de materias')
        return Materias.objects.create(cupos=cupos, area=area)

    # * Este test funciona en conjunto con el test_crear_materia
    def test_materia_creacion(self):
        print('----- Test de creacion de Materias con metodo __str__ -------')
        m = self.test_crear_materia()
        print('m', m)
        self.assertTrue(isinstance(m, Materias))
        self.assertEqual(m.__str__(), m.area)
        print('---------Fin de Test de creacion de materias con metodo __str_------------')


client = Client()


# * Test de la creacion de materias
class creacion_materias(TestCase):
    def setUp(self) -> None:
        self.payload = {
            'id': 1,
            'materia': 'IA',
            'cupos': '22',
            'area': 'Inteligencia artificial'
        }
# * Aqui se prueba que el test de la creacion haya sido exitoso

    def test_get_materias(self):
        response = client.post(
            reverse('add-materias'),
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        # s = MateriasSerializer(instance=self.payload).data
        # print('s',s)
        serializer = json.loads(response.content)
        self.assertEqual(self.payload, serializer)
        # print('******************************************************', response.content)


# * Test para ver una materia por pk
class consulta_materias(TestCase):
    def setUp(self):
        self.materia = Materias.objects.create(
            materia='PO', cupos='10', area='Programacion'
        )

    def test_get_materia(self):
        response = client.get(
            reverse('ver_materia', kwargs={'pk': self.materia.pk})
        )
        mat = Materias.objects.get(pk=self.materia.pk)
        serializer = MateriasSerializer(mat)
        # print(serializer,'seriaiaiaii')
        self.assertEqual(response.data, serializer.data)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)


# * Test para la actualizacion de materia
class actualiza_Materias(TestCase):
    def setUp(self) -> None:
        self.materia = Materias.objects.create(
            materia="QI", cupos="20", area="Quimica"
        )
        self.valid_data = {
            "id": 1,
            "materia": "FI",
            "cupos": "22",
            "area": "Fisica"
        }

    def test_materia_valida(self):
        response = client.put(
            reverse('actualizar-materias', kwargs={'pk': self.materia.pk}),
            data=json.dumps(self.valid_data),
            content_type='application/json'
        )
        
        data = json.loads(response.content)
        # self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.valid_data, data)


# * Test para la eliminacion de una materia
class delete_materia(TestCase):
    def setUp(self) -> None:
        self.materia = Materias.objects.create(
            materia='QI', cupos='20', area='Quimicas'
        )

    def test_eliminacion_valida(self):
        response = client.delete(
            reverse('eliminar-materias', kwargs={'pk': self.materia.pk})
        )
       
        # print('data', response.data)
        # self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, {'Materia eliminada'})
    
    def test_validar_eliminacion(self):
        response = client.get(
            reverse('ver_materia', kwargs={'pk': self.materia.pk})
        )
        
        materia_eliminada = json.loads(response.content)
        print('Materia eliminada', response.content)
        self.assertEqual(response.data, materia_eliminada)
        # self.assertEqual(response.data, serializer.data)

    # ! Get de que no existe, permisos de REST