from ultralytics import YOLO

def load_model():
    return YOLO('yolov8s.pt')

def print_model_info(model):
    print('-------------------------\nYOLOv8s 🚀 2024-8-9')
    model.info()

def load_trained_yolov8s_model():
    model = YOLO('/data/Vehicle-Classification/models/detect_vehicles/yolov8/exp/weights/best.pt')
    print_model_info(model)
    return model