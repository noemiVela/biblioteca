from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Genero, Autor, Libro, Calificacion

Usuario = get_user_model()

class GeneroSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Genero.
    """
    class Meta:
        model = Genero
        fields = ['id', 'nombre']

class AutorSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Autor.
    """
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'nacionalidad']

class LibroSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Libro.
    """
    class Meta:
        model = Libro
        fields = [
            'id',
            'titulo',
            'autor',
            'genero',
            'fecha_publicacion',
            'isbn',
            'url',
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'url': {'required': False}
        }

class CalificacionSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Calificacion.
    Asigna automáticamente el usuario logueado.
    """
    class Meta:
        model = Calificacion
        fields = ['id', 'libro', 'calificacion']

    def create(self, validated_data):
        # Asignar automáticamente el usuario autenticado
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)
