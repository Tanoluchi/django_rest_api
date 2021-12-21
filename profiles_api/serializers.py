from rest_framework import fields, serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """ Serializa un campo para probar nuestro APIView """
    name = serializers.CharField(max_length=10)
    

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializa objeto de perfil de usuario """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                # La clave solo se muestra cuando se crea el usuario
                'write_only': True,
                # Se estiliza el campo, asi solo se muestra los asteriscos
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ Crear y retornar nuevo usuario """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """ Actualiza los datos del usuario """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


