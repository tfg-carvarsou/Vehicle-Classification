from rest_framework import serializers
from .models import VDImage

class VDImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VDImage
        fields = ['image']
        extra_kwargs = {
            'image': {'help_text': 'The image file'}
        }