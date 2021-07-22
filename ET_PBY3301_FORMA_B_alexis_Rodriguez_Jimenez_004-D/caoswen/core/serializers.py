from rest_framework import serializers
from .models import datos

class datosSerializer(serializers.ModelSerializer):
    class Meta:
        model = datos
        fields = ['rut', 'nombre', 'telefono', 'direccion', 'email', 'pais', 'contrasena']