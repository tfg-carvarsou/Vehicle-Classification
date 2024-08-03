import sys, os, io
sys.path.append(os.getcwd())
from .forms import ImageUploadForm
from .models import VDImage
from .serializers import VDImageSerializer
from torchvision import transforms
from PIL import Image
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from core.detect_vehicles.yolov5.model import load_trained_yolov5s_model

# detect_yolov5s_model = load_trained_yolov5s_model()

class VDImageListCreateView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = VDImage.objects.all()
    serializer_class = VDImageSerializer

    @extend_schema(
        summary='List all images',
        responses={
            200: OpenApiResponse(response=VDImageSerializer(many=True), 
                                 description='The images has been listed successfully'),
            400: OpenApiResponse(response=None,
                                 description='There has been an incident when listing the images. Please try again')
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    #TODO: Change application/json to multipart/form-data in create method
    @extend_schema(
        summary='Upload an image to detect vehicles',
        request={
            'multipart/form-data': VDImageSerializer,
        },
        responses={
            201: OpenApiResponse(response=VDImageSerializer, 
                                 description='The image has been uploaded successfully'),
            400: OpenApiResponse(response=None,
                                 description='There has been an incident when uploading the image. Please try again')
        },
    )
    def create(self, request, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            transformed_image = self.transform_image(image)
            predicted_image = transformed_image
            
            vd_image = VDImage(image=image)
            image_to_save = f"{image.name.split('.')[0]}.jpg"
            vd_image.image.save(image_to_save, predicted_image, save=True)

            serializer = VDImageSerializer(vd_image)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
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

class VDImageRetrieveDeleteView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = VDImage.objects.all()
    serializer_class = VDImageSerializer
    lookup_field = 'code'
    
    @extend_schema(
        summary='Retrieve an image by its code',
        responses={
            200: OpenApiResponse(response=VDImageSerializer, 
                                 description='The image has been retrieved successfully'),
            400: OpenApiResponse(response=None,
                                 description='There has been an incident when retrieving the image. Please try again')
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(
        summary='Delete an image by its code',
        responses={
            204: OpenApiResponse(response=None, 
                                 description='The image has been deleted successfully'),
            400: OpenApiResponse(response=None,
                                 description='There has been an incident when deleting the image. Please try again')
        },
    )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        image_path = instance.image.path
        try:
            if os.path.exists(image_path):
                instance.delete()
                os.remove(image_path)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
       