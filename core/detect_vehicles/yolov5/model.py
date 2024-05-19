import os
import torch

def get_model_path():
    pwd = os.getcwd()
    myuser = os.path.dirname(pwd)
    return os.path.join(myuser, '.cache/torch/hub/ultralytics_yolov5_master')

def load_model():
    torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True, force_reload=False)