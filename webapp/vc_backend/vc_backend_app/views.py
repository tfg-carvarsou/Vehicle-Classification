import sys, os, io, base64
sys.path.append(os.getcwd())
from django.shortcuts import render
from .forms import ImageUploadForm
from .models import VDImage
from .serializers import VDImageSerializer
from torchvision import transforms
from core.detect_vehicles.yolov5.model import load_trained_yolov5s_model
from PIL import Image
from rest_framework import viewsets

detect_yolov5s_model = None 
# detect_yolov5s_model = load_trained_yolov5s_model()

# img = Image.open('./images/classify_vehicles/efficientnet_b1/Aston Martin V8 Vantage Convertible 2012.jpg')
# img = transforms.Resize((720, 1280))(img)
# img = detect_yolov5s_model(img)
# img.show()

def transform_image(image):
    tf = transforms.Compose([
        transforms.Resize((720, 1280))
    ])
    return tf(image)

def get_prediction(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    image = transform_image(image)
    return detect_yolov5s_model(image)
class VDImageViewSet(viewsets.ModelViewSet):
    queryset = VDImage.objects.all()
    serializer_class = VDImageSerializer

def detector(request):
    image_uri = None
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_bytes = image.file.read()
            encoded_img = base64.b64encode(image_bytes).decode('ascii')
            image_uri = f'data:image/jpeg;base64,{encoded_img}'
            try:
                res = get_prediction(image_bytes)
            except RuntimeError as e:
                print(e)
        else:
            form = ImageUploadForm()
                
    context = {
        'form': form,
        'image_uri': image_uri,
        'image': res
    }
    return render(request, 'vc_backend_app/detector.html', context)