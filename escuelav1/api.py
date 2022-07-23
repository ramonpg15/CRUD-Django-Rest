from rest_framework import generics
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer
from .models import Materias
from .serializer import MateriasSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Si ha usuario y contraseña
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.Now perform Login to get your token",
        })
        

class actualizar_materia(generics.RetrieveUpdateAPIView):
    queryset = Materias.objects.all()
    serializer_class = MateriasSerializer