from django.urls import path, include
from .models import Cliente
from rest_framework import serializers



# Serializers define the API representation.
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'endereço', 'idade']