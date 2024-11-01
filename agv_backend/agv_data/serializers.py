from rest_framework import serializers
from .models import AGVData

class AGVDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AGVData
        fields = '__all__'