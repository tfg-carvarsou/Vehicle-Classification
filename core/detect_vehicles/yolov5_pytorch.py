import torch
import os
import subprocess
import matplotlib.pyplot as plt
import numpy as np

def load_model():
    torch.hub.load('ultralytics/yolov5', 'yolov5s', force_reload=True)

def get_model_path():
    pwd = os.getcwd()
    myuser = os.path.dirname(pwd)
    return os.path.join(myuser, '.cache/torch/hub/ultralytics_yolov5_master/')

def train(model_path, img_size, batch, epochs, data_path):
    '''
    python /home/carvarsou/.cache/torch/hub/ultralytics_yolov5_master/train.py 
    --img 640 
    --batch 16 
    --epochs 5 
    --data ./datasets/vehicles/yolov5_pytorch/data.yaml
    '''
    subprocess.run([
        "python",
        f"{model_path}train.py",
        "--img", f"{img_size}",
        "--batch", f"{batch}",
        "--epochs", f"{epochs}",
        "--data", f"{data_path}data.yaml"
    ])

def detect_vehicles(model_path, weights, img_size, conf, img):
    '''
    python /home/carvarsou/.cache/torch/hub/ultralytics_yolov5_master/detect.py 
    --weights /home/carvarsou/.cache/torch/hub/ultralytics_yolov5_master/runs/train/exp3/weights/best.pt 
    --img 640 
    --conf 0.3 
    --source /home/carvarsou/Vehicle-Classification/datasets/vehicles/yolov5_pytorch/test/images/adit_mp4-5_jpg.rf.bd945716e20cb3f850e2ad36df03d6e3.jpg
    '''
    subprocess.run([
        "python",
        f"{model_path}detect.py",
        "--weights", f"{weights}",
        "--img", f"{img_size}",
        "--conf", f"{conf}",
        "--source", f"{img}"
    ])

def main():
    # 1. Download roboflow-vehicles dataset
    # download_dataset()

    # 2. Load pre-trained YoloV5 model 
    load_model()
    model_path = get_model_path()
    print(model_path)

    # 3. Configure training file (data.yaml)
    # configure_yaml()

    # 4. Train model with training file
    # train(model_path)

    # 5. Evaluate new model performance
    # evaluate()

    # 6. Detect vehicles in new image
    # detect_vehicles()

if __name__ == "__main__":
    main()


