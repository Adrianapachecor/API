# api/admin.py
from django.contrib import admin
from .models import FormResponse

admin.site.register(FormResponse)  # Esto permitirá ver las respuestas desde el panel de administración
