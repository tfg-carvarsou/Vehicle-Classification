from rest_framework import serializers
from .models import VDImage, VCImage

class VDImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VDImage
        fields = ['model', 'image']
        extra_kwargs = {
            'model': {'help_text': 'The ML model for detecting vehicles'},
            'image': {'help_text': 'The image file to be uploaded'}
        }

class VCImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VCImage
        fields = ['model', 'image']
        extra_kwargs = {
            'model': {'help_text': 'The ML model for classifying vehicles'},
            'image': {'help_text': 'The image file to be uploaded'}
        }