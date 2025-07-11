from django.contrib.auth import get_user_model
from rest_framework import serializers

# Usamos get_user_model para mayor flexibilidad
Usuario = get_user_model()

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """
        Crea un nuevo usuario con los datos validados.
        """
        user = Usuario.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )
        return user
