import os
from django.contrib import admin
from .models import VDImage, VCImage
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from drf_spectacular.utils import extend_schema, OpenApiResponse

admin.site.register(VDImage)
admin.site.register(VCImage)

class AdminImageDeleteAllView(viewsets.GenericViewSet):
    serializer_class = None
    
    @extend_schema(
        exclude=True,
        summary='Delete all images in database',
        responses={
            204: OpenApiResponse(response=None, 
                                 description='All images have been deleted successfully'),
            400: OpenApiResponse(response=None,
                                 description='There has been an incident when deleting the images. Please try again'),
            403: OpenApiResponse(response=None,
                                 description='You are not authorized to perform this action')
        },
    )
    @action(detail=False, methods=['delete'], permission_classes=[IsAdminUser])
    def clean(self, request, *args, **kwargs):
        try:
            for instance in VCImage.objects.all():
                image_path = instance.image.path
                if os.path.exists(image_path):
                    instance.delete()
                    os.remove(image_path)
            
            for instance in VDImage.objects.all():
                image_path = instance.image.path
                if os.path.exists(image_path):
                    instance.delete()
                    os.remove(image_path)
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
class AdminVDImageDeleteAllView(viewsets.GenericViewSet):
    queryset = VDImage.objects.all()
    serializer_class = None
    
    @extend_schema(
        exclude=True,
        summary='Delete all detection images',
        responses={
            204: OpenApiResponse(response=None, 
                                 description='All images have been deleted successfully'),
            400: OpenApiResponse(response=None,
                                 description='There has been an incident when deleting the images. Please try again'),
            403: OpenApiResponse(response=None,
                                 description='You are not authorized to perform this action')
        },
    )
    @action(detail=False, methods=['delete'], permission_classes=[IsAdminUser])
    def clean(self, request, *args, **kwargs):
        try:
            for instance in self.queryset:
                image_path = instance.image.path
                if os.path.exists(image_path):
                    instance.delete()
                    os.remove(image_path)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        
class AdminVCImageDeleteAllView(viewsets.GenericViewSet):
    queryset = VCImage.objects.all()
    serializer_class = None
    
    @extend_schema(
        exclude=True,
        summary='Delete all classification images',
        responses={
            204: OpenApiResponse(response=None, 
                                 description='All images have been deleted successfully'),
            400: OpenApiResponse(response=None,
                                 description='There has been an incident when deleting the images. Please try again'),
            403: OpenApiResponse(response=None,
                                 description='You are not authorized to perform this action')
        },
    )
    @action(detail=False, methods=['delete'], permission_classes=[IsAdminUser])
    def clean(self, request, *args, **kwargs):
        try:
            for instance in self.queryset:
                image_path = instance.image.path
                if os.path.exists(image_path):
                    instance.delete()
                    os.remove(image_path)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)