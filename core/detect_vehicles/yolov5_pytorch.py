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
    --img 320 
    --batch 10 
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

def get_train_results(source, dest):
    os.makedirs(dest, exist_ok=True)
    subprocess.run(["cp", "-r", source, dest])

def detect_vehicles(model_path, weights, img_size, conf, img):
    '''
    python /home/carvarsou/.cache/torch/hub/ultralytics_yolov5_master/detect.py 
    --weights /home/carvarsou/Vehicle-Classification/models/detect_vehicles/yolov5_pytorch/exp/weights/best.pt 
    --img 640 
    --conf 0.3 
    --source /home/carvarsou/Vehicle-Classification/models/detect_vehicles/yolov5_pytorch/test_images/prueba.jpg
    '''
    subprocess.run([
        "python",
        f"{model_path}/detect.py",
        "--weights", weights,
        "--img", str(img_size),
        "--conf", str(conf),
        "--source", img
    ])
    
def get_detect_results(source, dest):
    os.makedirs(dest, exist_ok=True)
    subprocess.run(["cp", "-r", source, dest])

def debug_mode():
    download = False
    load = False
    configure = False
    train = False
    evaluate = True
    detect = True
    return download, load, configure, train, evaluate, detect

def main():
    download, load, configure, train, evaluate, detect = debug_mode()
    model_path = get_model_path()
    dataset_path = './datasets/vehicles/yolov5_pytorch'
    train_results_source = os.path.join(model_path, 'runs/train/exp')
    train_results_dest = './models/detect_vehicles/yolov5_pytorch'
    weights = os.path.join(train_results_dest, 'exp/weights/best.pt')
    detect_img_source = os.path.join(model_path, 'runs/detect/exp')
    detect_img_dest = './images/detect_vehicles/yolov5_pytorch'
    img = os.path.join(detect_img_dest, 'prueba.jpg')

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
        configure_yaml(dataset_path)
        print("Training file configured.")

    # 4. Train model with training file
    if train:
        print("\n🚀 Training model...")
        train(model_path, 320, 10, 5, dataset_path, 'yolov5s.pt')
        print("Training completed.")

    # 5. Evaluate new model performance
    if evaluate:
        print("\n📊 Evaluating model...")
        get_train_results(train_results_source, train_results_dest)
        #TODO evaluate()

    # 6. Detect vehicles in new image
    if detect:
        print("\n🚗 Detecting vehicles...")
        detect_vehicles(model_path, weights, 320, 0.5, img)
        # TODO show image instead of saving it
        get_detect_results(detect_img_source, os.path.join(detect_img_dest, 'results'))

if __name__ == "__main__":
    main()


