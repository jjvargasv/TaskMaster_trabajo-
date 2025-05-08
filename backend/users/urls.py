from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, ProfileView, PasswordResetAPIView, PasswordResetConfirmAPIView, ChangePasswordView
from rest_framework_simplejwt.views import TokenRefreshView

# Endpoints relacionados a usuarios: registro, login, refresco de token, perfil, cambio de contraseña y recuperación de contraseña.
urlpatterns = [
    # Registro de un nuevo usuario.
    path('register/', RegisterView.as_view(), name='register'),
    # Autenticación de un usuario existente.
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    # Refresco del token de autenticación.
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Detalle del perfil del usuario autenticado.
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('password_reset/', PasswordResetAPIView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),
]
