import torch
import os
import subprocess
import yaml

def download_dataset(script):
    subprocess.run(["chmod", "+x", script])
    subprocess.run([script])

def load_model():
    torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True, force_reload=False)

def get_model_path():
    pwd = os.getcwd()
    myuser = os.path.dirname(pwd)
    return os.path.join(myuser, '.cache/torch/hub/ultralytics_yolov5_master')

def configure_yaml(dataset_path):
    dataset_path = dataset_path[2:]
    pwd = os.getcwd()
    yaml_file = os.path.join(dataset_path, 'data.yaml')

    with open(yaml_file, 'r') as y:
        yaml_data = yaml.safe_load(y)

    yaml_data.update({
        'train': os.path.join(pwd, dataset_path, 'train/images'),
        'val': os.path.join(pwd, dataset_path, 'valid/images'),
        'test': os.path.join(pwd, dataset_path, 'test/images')
    })

    with open(yaml_file, 'w') as y:
        yaml.safe_dump(yaml_data, y)

def train(model_path, img_size, batch, epochs, dataset_path, weights):
    '''
    python /home/carvarsou/.cache/torch/hub/ultralytics_yolov5_master/train.py 
    --img 640 
    --batch 16 
    --epochs 5 
    --data ./datasets/vehicles/yolov5_pytorch/data.yaml
    --weights yolov5s.pt
    '''
    subprocess.run([
        "python",
        f"{model_path}/train.py",
        "--img", str(img_size),
        "--batch", str(batch),
        "--epochs", str(epochs),
        "--data", f"{dataset_path}/data.yaml",
        "--weights", weights
    ])

def get_results(source, dest):
    """
    Recursively copy the contents of a directory from source to destination using subprocess.
    
    Parameters:
        source (str): The path of the source directory to copy.
        dest (str): The path of the destination directory.
    """
    os.makedirs(dest, exist_ok=True)
    subprocess.run(["cp", "-r", source, dest])

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
        f"{model_path}/detect.py",
        "--weights", weights,
        "--img", img_size,
        "--conf", conf,
        "--source", img
    ])

def main():
    # 1. Download roboflow-vehicles dataset
    print("\n📥 Downloading dataset...")
    download_dataset('./scripts/yolov5_vehicles_dataset.sh')

    # 2. Load pre-trained YoloV5 model 
    print("\n🔍 Loading YoloV5 model...")
    load_model()
    model_path = get_model_path()
    print("Model loaded from: ", model_path)

    # 3. Configure training file (data.yaml)
    print("\n🤖 Configuring training file...")
    dataset_path = './datasets/vehicles/yolov5_pytorch'
    configure_yaml(dataset_path)
    print("Training file configured.")

    # 4. Train model with training file
    print("\n🚀 Training model...")
    train(model_path, 320, 10, 5, dataset_path, 'yolov5s.pt')
    print("Training completed.")

    # 5. Evaluate new model performance
    print("\n📊 Evaluating model...")
    model_source = os.path.join(model_path, 'runs/train/exp')
    model_dest = './models/detect_vehicles/yolov5_pytorch'
    get_results(model_source, model_dest)
    # evaluate()

    # 6. Detect vehicles in new image
    print("\n🚗 Detecting vehicles...")
    # detect_vehicles()

if __name__ == "__main__":
    main()


