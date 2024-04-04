import torch
import yaml
import os
import matplotlib.pyplot as plt
import numpy as np

def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    return model

def define_parameters():
    with open('datasets/vehicles/yolov5_pytorch/data.yaml', 'r') as r:
        data = yaml.safe_load(r)
        num_classes = data['nc']
        names = data['names']
    return num_classes, names

def detect_objects(model, img_path, save_dir):
    results = model(img_path)
    results.print()
    plt.imshow(np.squeeze(results.render()), extent=[0, 640, 480, 0])
    plt.axis('off')
    
    filename = os.path.basename(img_path)
    save_path = os.path.join(save_dir, filename)
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)

def main():
    model = load_model()
    base_dir = 'datasets/vehicles/yolov5_pytorch'
    train_dir = os.path.join(base_dir, 'train')
    img_dir = os.path.join(train_dir, 'images')

    filename = 'pagi_16112021_mp4-581_jpg.rf.00c56fa5c3ce82f9d92e6e5ff9367430.jpg'
    img_path = os.path.join(img_dir, filename)

    save_dir = os.path.join('core', 'imgs')
    detect_objects(model, img_path, save_dir)

if __name__ == "__main__":
    main()

