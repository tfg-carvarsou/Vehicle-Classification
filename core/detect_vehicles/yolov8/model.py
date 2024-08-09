import os, pwd
from ultralytics import YOLO

def get_username():
    return pwd.getpwuid(os.getuid())[0]

def load_model():
    return YOLO('yolov8s.pt')

def print_model_info(model):
    print('-------------------------\nYOLOv8 🚀 2024-8-9')
    model.info()

def load_trained_yolov8s_model():
    model = YOLO('/data/Vehicle-Classification/models/detect_vehicles/yolov8/exp/weights/best.pt')
    print_model_info(model)
    return model