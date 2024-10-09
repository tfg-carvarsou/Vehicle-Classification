import torch
from core.detect_vehicles.yolov8.datasets import download_dataset, get_ds_path, configure_yaml
from core.detect_vehicles.yolov8.model import load_model
from core.detect_vehicles.yolov8.utils import get_train_results

IMG_SIZE = 256
BATCH_SIZE = 8
NUM_WORKERS = 4
EPOCHS = 5
DEVICE = (0 if torch.cuda.is_available() else 'cpu')
OPTIMIZER = 'SGD' # stochastic gradient descent
CONF_THRESHOLD = 0.25

def train_model(model, img_size, batch, num_workers, epochs, optimizer, ds_path):
    model.train(data=f"{ds_path}/data.yaml", imgsz=img_size, batch=batch, 
                workers=num_workers, epochs=epochs, optimizer=optimizer)

def debug_mode():
    download = True
    load = True
    configure = True
    train = True
    evaluate = True
    return download, load, configure, train, evaluate

def main():
    download, load, configure, train, evaluate = debug_mode()

    ds_path = get_ds_path()
    train_results_source = './runs/detect/train/*'
    train_results_dest = './models/detect_vehicles/yolov8/exp/'

    # 1. Download roboflow-vehicles dataset
    if download:
        print("\n📥 Downloading dataset...")
        download_dataset('./scripts/yolov8_vehicles_dataset.sh')

    # 2. Load pre-trained YoloV8 model 
    if load:
        print("\n🔍 Loading YoloV5 model...")
        model = load_model()
        
    # 3. Configure training file (data.yaml)
    if configure:
        print("\n🤖 Configuring training file...")
        configure_yaml(ds_path)
        print("Training file configured")

    # 4. Train model with training file
    if train:
        print("\n🚀 Training model...")
        train_model(model, IMG_SIZE, BATCH_SIZE, NUM_WORKERS, EPOCHS, OPTIMIZER, ds_path)
        print("Training completed")

    # 5. Evaluate new model performance
    if evaluate:
        print("\n📊 Evaluating model...")
        get_train_results(train_results_source, train_results_dest)

if __name__ == "__main__":
    main()


