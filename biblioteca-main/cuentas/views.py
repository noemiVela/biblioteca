from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from cuentas.serializers import UsuarioRegistroSerializer

@api_view(['POST'])
def registro_view(request):
    serializer = UsuarioRegistroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Usuario creado con éxito.",
            "usuario": serializer.data
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
