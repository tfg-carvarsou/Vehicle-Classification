import sys, os, io
from .forms import ImageUploadForm
from .models import VDImage
from .serializers import VDImageSerializer
from torchvision import transforms
from PIL import Image
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
class VDImageViewSet(viewsets.ModelViewSet):
    queryset = VDImage.objects.all()
    serializer_class = VDImageSerializer

    @extend_schema(request=VDImageSerializer, responses=VDImageSerializer)
    def create(self, request, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            transformed_image = self.transform_image(image)
            vd_image = VDImage(image=image)
            vd_image.image.save(f"{image.name.split('.')[0]}_transformed.jpg", transformed_image, save=True)

            serializer = VDImageSerializer(vd_image)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def transform_image(self, image_file):
        image = Image.open(image_file)
        transform = transforms.Compose([
            transforms.Resize((720, 1280))
        ])
        transformed_image = transform(image)
        image_io = io.BytesIO()
        transformed_image.save(image_io, format='JPEG')
        image_io.seek(0)
        return image_io