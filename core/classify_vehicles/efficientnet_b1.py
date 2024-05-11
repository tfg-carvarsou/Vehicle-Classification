import subprocess
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from StanfordDataset import StanfordDataset

from torch.utils.data import DataLoader
from torchvision import transforms
from efficientnet_pytorch import EfficientNet
from PIL import Image

# The Cars dataset contains 16,185 images of 196 classes of cars. 
# The data is split into 8,144 training images and 8,041 testing images, 
# where each class has been split roughly in a 50-50 split. 
# Classes are typically at the level of Make, Model, Year, e.g. 2012 Tesla Model S or 2012 BMW M3 coupe.

def download_dataset(script):
    subprocess.run(["chmod", "+x", script])
    subprocess.run([script])

def preprocess_dataset(csv_file, train_dir):
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    train_ds = StanfordDataset(csv_file=csv_file, root_dir=train_dir, transform=transform)
    train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
    return train_loader

def print_dataset_samples(dataset_loader, num_samples=1):
    for i, (images, _, class_labels, metadata) in enumerate(dataset_loader):
        if i > num_samples-1:
            break
        for j in range(num_samples):
            plt.imshow(images[j].permute(1, 2, 0))
            plt.title(f"Make: {metadata['make'][j]}, Model: {metadata['model'][j]}, Year: {metadata['year'][j]}, Label: {class_labels[j]}")
            plt.show()

def debug_mode():
    download = False
    preprocess = True
    load = False
    train = False
    evaluate = False
    classify = False
    return download, preprocess, load, train, evaluate, classify

def main():
    download, preprocess, load, train, evaluate, classify = debug_mode()
    train_dir = './datasets/stanford/car_data/car_data/train'
    train_csv = './datasets/stanford/anno_train.csv'
    test_dir = './datasets/stanford/car_data/car_data/test'
    test_csv = './datasets/stanford/anno_test.csv'

    if download:
        print("\n📥 Downloading dataset...")
        download_dataset('./scripts/stanford_dataset.sh')
    
    if preprocess:
        print("\n⏳ Preprocessing data...")
        train_loader = preprocess_dataset(train_csv, train_dir)
        print_dataset_samples(train_loader)
        print("Data preprocessed successfully.")

if __name__ == "__main__":
    main()
