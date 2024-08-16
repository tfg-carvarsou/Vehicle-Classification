from ultralytics import YOLO

def load_model():
    return YOLO('yolov8s-cls.pt')

def print_model_info(model):
    print('-------------------------\nYOLOv8s-cls 🚀 2024-8-11')
    model.info()

def load_trained_yolov8scls_model():
    model = YOLO('/data/Vehicle-Classification/models/classify_vehicles/yolov8/exp/weights/best.pt')
    print_model_info(model)
    return model