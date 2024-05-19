import os
import torch
import subprocess
from datasets import download_dataset, get_ds_path, configure_yaml
from model import get_model_path, load_model
from yv5_detect import detect_vehicles
from yv5_utils import get_train_results, get_detect_results

IMG_SIZE = 256
BATCH_SIZE = 8
NUM_WORKERS = 4
EPOCHS = 5
DEVICE = (0 if torch.cuda.is_available() else 'cpu')
OPTIMIZER = 'SGD' # stochastic gradient descent
CONF_THRESHOLD = 0.25

def train_model(model_path, img_size, batch, num_workers, epochs, optimizer, ds_path, weights):
    """
    python /home/carvarsou/.cache/torch/hub/ultralytics_yolov5_master/train.py 
    --img 256 
    --batch 16 
    --epochs 5 
    --workers 4
    --optimizer SGD
    --data ./datasets/vehicles/yolov5/data.yaml
    --weights yolov5s.pt
    """
    subprocess.run([
        "python",
        f"{model_path}/train.py",
        "--img", str(img_size),
        "--batch", str(batch),
        "--workers", str(num_workers),
        "--epochs", str(epochs),
        "--optimizer", optimizer,
        "--data", f"{ds_path}/data.yaml",
        "--weights", weights
    ])

def debug_mode():
    download = True
    load = True
    configure = True
    train = True
    evaluate = True
    detect = True
    return download, load, configure, train, evaluate, detect

def main():
    download, load, configure, train, evaluate, detect = debug_mode()

    ds_path = get_ds_path()
    model_path = get_model_path()
    train_results_source = os.path.join(model_path, 'runs/train/exp')
    train_results_dest = './models/detect_vehicles/yolov5'
    yolov5_weights = os.path.join(train_results_dest, 'exp/weights/best.pt')
    detect_img_source = os.path.join(model_path, 'runs/detect')
    detect_img_dest = './images/detect_vehicles/yolov5'
    list_images = [os.path.join(detect_img_dest, f) 
                   for f in os.listdir(detect_img_dest) if f.endswith('.jpg')]

    # 1. Download roboflow-vehicles dataset
    if download:
        print("\n📥 Downloading dataset...")
        download_dataset('./scripts/yolov5_vehicles_dataset.sh')

    # 2. Load pre-trained YoloV5 model 
    if load:
        print("\n🔍 Loading YoloV5 model...")
        load_model()
        print("Model loaded from: ", model_path)

    # 3. Configure training file (data.yaml)
    if configure:
        print("\n🤖 Configuring training file...")
        configure_yaml(ds_path)
        print("Training file configured")

    # 4. Train model with training file
    if train:
        print("\n🚀 Training model...")
        train_model(model_path, IMG_SIZE, BATCH_SIZE, NUM_WORKERS, 
                    EPOCHS, OPTIMIZER, ds_path, 'yolov5s.pt')
        print("Training completed")

    # 5. Evaluate new model performance
    if evaluate:
        print("\n📊 Evaluating model...")
        get_train_results(train_results_source, train_results_dest)

    # 6. Detect vehicles in new image
    if detect:
        print("\n🚗 Detecting vehicles...")
        detect_vehicles(model_path, yolov5_weights, IMG_SIZE, CONF_THRESHOLD, 
                        ds_path, list_images)
        get_detect_results(detect_img_source, detect_img_dest, list_images)

if __name__ == "__main__":
    main()


