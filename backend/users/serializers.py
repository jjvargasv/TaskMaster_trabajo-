from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

# Obtiene el modelo de usuario actual
User = get_user_model()

# Serializer para registrar nuevos usuarios
class RegisterSerializer(serializers.ModelSerializer):
    # Campo para la contraseña, solo se escribe y es requerido
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # Campo para confirmar la contraseña, solo se escribe y es requerido
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Las contraseñas no coinciden."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_picture')
