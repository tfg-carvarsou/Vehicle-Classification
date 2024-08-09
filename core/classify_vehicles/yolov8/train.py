
from datasets import download_dataset, crop_dataset, get_ds_path
from model import load_model

IMG_SIZE = 224
BATCH_SIZE = 16
NUM_WORKERS = 4
EPOCHS = 5
OPTIMIZER = 'SGD' # stochastic gradient descent
CONF_THRESHOLD = 0.25

def train_model(model, img_size, batch, num_workers, epochs, optimizer, ds_path):
    model.train(data=f"{ds_path}", imgsz=img_size, batch=batch, 
                workers=num_workers, epochs=epochs, optimizer=optimizer)

def debug_mode():
    download = False
    load = True
    configure = True
    train = True
    evaluate = True
    return download, load, configure, train, evaluate

def main():
    download, load, configure, train, evaluate = debug_mode()

    ds_path = get_ds_path()

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
    #TODO: Configure YAML file for training
    if train:
        print("\n🚀 Training model...")
        train_model(model, IMG_SIZE, BATCH_SIZE, NUM_WORKERS, EPOCHS, OPTIMIZER, ds_path)
        print("Training completed")

if __name__ == '__main__':
    main()