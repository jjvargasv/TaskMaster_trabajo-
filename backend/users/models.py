from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de usuario personalizado para extender el modelo por defecto de Django.
# Este modelo permite agregar campos adicionales al usuario sin modificar el modelo base de Django.
class CustomUser(AbstractUser):
    # Campo opcional para foto de perfil (puede ser null)
    # Este campo permite que los usuarios suban una foto de perfil, que se almacenará en el directorio 'profile_pics/'.
    # El parámetro 'null=True' indica que este campo puede ser null, y 'blank=True' indica que puede estar vacío.
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # Método que devuelve una representación en cadena del objeto.
    # En este caso, devuelve el nombre de usuario.
    def __str__(self):
        return self.username
