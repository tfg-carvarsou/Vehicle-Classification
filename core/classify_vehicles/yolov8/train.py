
from core.classify_vehicles.yolov8.datasets import download_dataset, crop_dataset, get_ds_path
from core.classify_vehicles.yolov8.model import load_model
from core.classify_vehicles.yolov8.utils import get_train_results

IMG_SIZE = 224
BATCH_SIZE = 16
NUM_WORKERS = 4
EPOCHS = 5
OPTIMIZER = 'SGD' # stochastic gradient descent
CONF_THRESHOLD = 0.25

def train_model(model, img_size, batch, num_workers, epochs, optimizer, ds_path):
    model.train(data=f"{ds_path}/car_data/car_data", imgsz=img_size, batch=batch, 
                workers=num_workers, epochs=epochs, optimizer=optimizer)

def debug_mode():
    download = True
    load = True
    train = True
    evaluate = True
    return download, load, train, evaluate

def main():
    download, load, train, evaluate = debug_mode()

    ds_path = get_ds_path()
    train_results_source = './runs/classify/train2/*'
    train_results_dest = './models/classify_vehicles/yolov8/exp/'

    # 1. Download stanford dataset
    if download:
        print("\n📥 Downloading dataset...")
        download_dataset('./scripts/yolov8_stanford_dataset.sh')
        crop_dataset()

    # 2. Load pre-trained YoloV8 model 
    if load:
        print("\n🔍 Loading YoloV8 model...")
        model = load_model()

    # 4. Train model with training file
    if train:
        print("\n🚀 Training model...")
        train_model(model, IMG_SIZE, BATCH_SIZE, NUM_WORKERS, EPOCHS, OPTIMIZER, ds_path)
        print("Training completed")

    # 5. Evaluate new model performance
    if evaluate:
        print("\n📊 Evaluating model performance...")
        get_train_results(train_results_source, train_results_dest)
        

if __name__ == '__main__':
    main()