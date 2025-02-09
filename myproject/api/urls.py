# api/urls.py
from django.urls import path
from . import views  # Asegúrate de importar correctamente las vistas

urlpatterns = [
    path('', views.home),  # Vista para la página de bienvenida
    path('formulario/', views.show_form),
    path('post/', views.postData),   # URL para mostrar el formulario HTML
    path('get/', views.getData),  # URL para obtener los datos en formato JSON
    path('post/', views.postData),  # URL para enviar los datos del formulario
]
