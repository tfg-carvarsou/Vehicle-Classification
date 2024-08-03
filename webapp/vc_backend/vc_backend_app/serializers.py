from rest_framework import serializers
from .models import VDImage

class VDImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VDImage
        fields = ['model', 'image']
        extra_kwargs = {
            'model': {'help_text': 'The ML model for detecting vehicles'},
            'image': {'help_text': 'The image file to be uploaded'}
        }