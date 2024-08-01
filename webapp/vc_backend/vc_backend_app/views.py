import sys, os
sys.path.append(os.getcwd())
from django.conf import settings
from core.detect_vehicles.yolov5.model import load_trained_yolov5s_model
from core.detect_vehicles.yolov5.yv5_detect import detect_vehicles
from PIL import Image

detect_yolov5s_model = load_trained_yolov5s_model()

test_img = Image.open('./images/detect_vehicles/yolov5/camiones.jpg')
res = detect_yolov5s_model(test_img)
res.show()