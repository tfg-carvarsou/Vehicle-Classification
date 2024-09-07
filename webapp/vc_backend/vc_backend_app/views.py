import sys, os, io, numpy as np
sys.path.append(os.getcwd())
from .forms import VDImageUploadForm, VCImageUploadForm
from .models import VDImage, VCImage
from .serializers import VDImageSerializer, VDImagePostSerializer, VCImageSerializer, VCImagePostSerializer
from .enums import VDLabel
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse
from core.detect_vehicles.yolov5.model import load_trained_yolov5s_model
from core.detect_vehicles.yolov5.detect import detect_yv5_image
from core.detect_vehicles.yolov8.model import load_trained_yolov8s_model
from core.detect_vehicles.yolov8.detect import detect_yv8_image
from core.classify_vehicles.efficientnet_b1.model import load_trained_effnetb1_model
from core.classify_vehicles.efficientnet_b1.classify import classify_effnetb1_image
from core.classify_vehicles.yolov8.model import load_trained_yolov8scls_model
from core.classify_vehicles.yolov8.classify import classify_yv8_image

detect_yolov5s_model = load_trained_yolov5s_model()
detect_yolov8s_model = load_trained_yolov8s_model()
classify_effnetb1_model = load_trained_effnetb1_model()
classify_yolov8s_model = load_trained_yolov8scls_model()

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
    
    @extend_schema(
        summary='Upload an image to detect vehicles',
        request={
            'multipart/form-data': VDImagePostSerializer,
        },
        responses={
            201: OpenApiResponse(response=VDImageSerializer, 
                                 description='The image has been uploaded successfully'),
            400: OpenApiResponse(response=None,
                                 description='There has been an incident when uploading the image. Please try again')
        },
    )
    def create(self, request, *args, **kwargs):
        
        form = VDImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.cleaned_data['model']
            image = form.cleaned_data['image']
            predicted_image, inf_time, arr_labels = self.predict_image(image, model)
            
            vd_image = VDImage(image=image)
            vd_image.model = model
            vd_image.inf_time = inf_time
            vd_image.label_count_dict = self.build_label_count_dict(arr_labels)
            image_to_save = f"{image.name.split('.')[0]}.jpg"
            vd_image.image.save(image_to_save, predicted_image, save=True)

            serializer = VDImageSerializer(vd_image)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def predict_image(self, image_file, model):
        try:
            if model == 'YOLOv5s':
                predicted_image, end, arr_labels = detect_yv5_image(detect_yolov5s_model, image_file)
            elif model == 'YOLOv8s':
                predicted_image, end, arr_labels = detect_yv8_image(detect_yolov8s_model, image_file)
            image_io = io.BytesIO()
            predicted_image.save(image_io, format='JPEG')
            image_io.seek(0)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        return image_io, end, arr_labels
    
    def build_label_count_dict(self, arr_labels):
        # Associates the index of the label (0) with the label value (0;big bus)
        index_label_dict = {
            int(label.value.split(';')[0]):label.value 
            for label in VDLabel
        }
        # Returns a dict where key is the label value (0;big bus) and value is the count
        return {
            index_label_dict[int(index)]:int(count)
            for index, count in zip(*np.unique(arr_labels, return_counts=True))
            if index in index_label_dict
        }

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
                                 description='There has been an incident when retrieving the image. Please try again'),
            404: OpenApiResponse(response=None,
                                 description='The image does not exist')
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
                                 description='There has been an incident when deleting the image. Please try again'),
            404: OpenApiResponse(response=None,
                                 description='The image does not exist')
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
        
class VCImageListCreateView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = VCImage.objects.all()
    serializer_class = VCImageSerializer
    @extend_schema(
        summary='List all images',
        responses={
            200: OpenApiResponse(response=VCImageSerializer(many=True), 
                                 description='The images has been listed successfully'),
            400: OpenApiResponse(response=None,
                                 description='There has been an incident when listing the images. Please try again')
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        summary='Upload an image to classify vehicles',
        request={
            'multipart/form-data': VCImagePostSerializer,
        },
        responses={
            201: OpenApiResponse(response=VCImageSerializer, 
                                 description='The image has been uploaded successfully'),
            400: OpenApiResponse(response=None,
                                 description='There has been an incident when uploading the image. Please try again')
        },
    )
    def create(self, request, *args, **kwargs):
        form = VCImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.cleaned_data['model']
            image = form.cleaned_data['image']
            predicted_image, inf_time, pred_class = self.predict_image(image, model)

            vc_image = VCImage(image=image)
            vc_image.model = model
            vc_image.inf_time = inf_time
            vc_image.pred_class = pred_class
            image_to_save = f"{image.name.split('.')[0]}.jpg"
            vc_image.image.save(image_to_save, predicted_image, save=True)

            serializer = VCImageSerializer(vc_image)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def predict_image(self, image_file, model):
        try:
            if model == 'EfficientNetB1':
                predicted_image, end, pred_class = classify_effnetb1_image(classify_effnetb1_model, image_file)
            elif model == 'YOLOv8s-cls':
                predicted_image, end, pred_class = classify_yv8_image(classify_yolov8s_model, image_file)
            image_io = io.BytesIO()
            predicted_image.save(image_io, format='JPEG')
            image_io.seek(0)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        return image_io, end, pred_class

class VCImageRetrieveDeleteView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = VCImage.objects.all()
    serializer_class = VCImageSerializer
    lookup_field = 'code'
    
    @extend_schema(
        summary='Retrieve an image by its code',
        responses={
            200: OpenApiResponse(response=VCImageSerializer, 
                                 description='The image has been retrieved successfully'),
            400: OpenApiResponse(response=None,
                                 description='There has been an incident when retrieving the image. Please try again'),
            404: OpenApiResponse(response=None,
                                 description='The image does not exist')
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
                                 description='There has been an incident when deleting the image. Please try again'),
            404: OpenApiResponse(response=None,
                                 description='The image does not exist')
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