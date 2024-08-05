import os, pwd
import torch

def get_username():
    return pwd.getpwuid(os.getuid())[0]

def get_model_path():
    myuser = get_username()
    return os.path.join('/home/', myuser, '.cache/torch/hub/ultralytics_yolov5_master')

def load_model():
    torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True, force_reload=False)

def load_trained_yolov5s_model():
    myuser = get_username()
    model_repo = os.path.join('/home/', myuser, '.cache/torch/hub/ultralytics_yolov5_master')
    weights = '/data/Vehicle-Classification/models/detect_vehicles/yolov5/exp/weights/best.pt'
    return torch.hub.load(model_repo, 'custom', path=weights, source='local')