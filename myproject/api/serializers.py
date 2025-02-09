# api/serializers.py
from rest_framework import serializers
from .models import FormResponse

class FormResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormResponse
        fields = ['name', 'last_name', 'age', 'email', 'sex', 'country', 'occupation', 'date_submitted']
