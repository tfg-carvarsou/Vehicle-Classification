from rest_framework import serializers
from .models import VDImage

class VDImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VDImage
        fields = ['id', 'image']