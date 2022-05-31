from rest_framework import serializers
from .models import ConjuntoModel

class ConjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConjuntoModel
        fields = '__all__'