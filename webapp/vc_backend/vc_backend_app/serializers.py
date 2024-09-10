from rest_framework import serializers
from .models import VDImage, VCImage

class VDImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VDImage
        fields = ['code', 'model', 'image', 'inf_time', 'label_count_dict']
        extra_kwargs = {
            'code': {'help_text': 'The unique code for the image'},
            'model': {'help_text': 'The ML model for detecting vehicles'},
            'image': {'help_text': 'The uploaded image'},
            'inf_time': {'help_text': 'The inference time for the model'},
            'label_count_dict': {'help_text': 'The dictionary containing the count of each label'}
        }

class VDImagePostSerializer(serializers.ModelSerializer):
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
        fields = ['code', 'model', 'image', 'inf_time', 'pred_class']
        extra_kwargs = {
            'code': {'help_text': 'The unique code for the image'},
            'model': {'help_text': 'The ML model for classifying vehicles'},
            'image': {'help_text': 'The uploaded image'},
            'inf_time': {'help_text': 'The inference time for the model'},
            'pred_class': {'help_text': 'The predicted class for the image'}
        }
class VCImagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VCImage
        fields = ['model', 'image']
        extra_kwargs = {
            'model': {'help_text': 'The ML model for classifying vehicles'},
            'image': {'help_text': 'The image file to be uploaded'}
        }