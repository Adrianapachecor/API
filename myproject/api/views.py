from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import FormResponse
from .serializers import FormResponseSerializer

def show_form(request):
    return render(request, 'formulario.html') 

@api_view(['GET'])
def home(request):
    return Response({"message": "Bienvenido a la API. Usa '/get/' para obtener datos y '/post/' para enviar datos."})

@api_view(['GET'])
def getData(request):
    # Obtener todas las respuestas del formulario
    form_responses = FormResponse.objects.all()
    # Serializar los datos
    serializer = FormResponseSerializer(form_responses, many=True)
    return Response(serializer.data)  # Retornar los datos en formato JSON

@api_view(['POST'])
def postData(request):
    # Crear una nueva entrada en FormResponse utilizando los datos del formulario
    serializer = FormResponseSerializer(data=request.data)
    
    if serializer.is_valid():  # Validar los datos recibidos
        serializer.save()  # Guardar los datos en la base de datos
        return Response(serializer.data, status=201)  # Retornar los datos guardados
    
    return Response(serializer.errors, status=400)  # Si los datos no son válidos, retornar los errores
