from django.urls import path
from .views import Saludos

urlpatterns = [
    
    path("hola/", Saludos.as_view(), name="saludar")
    
]