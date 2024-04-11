import subprocess
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
tf.config.set_visible_devices([], 'GPU')
tf.compat.v1.enable_eager_execution()

import matplotlib.pyplot as plt
from keras.applications import EfficientNetB1
# from keras.preprocessing.image import ImageDataGenerator
from keras.utils import image_dataset_from_directory
from keras import Sequential
from keras.layers import RandomFlip, RandomRotation
from keras.layers.experimental.preprocessing import Rescaling, Resizing
from keras.preprocessing.image import load_img
AUTOTUNE = tf.data.AUTOTUNE

# The Cars dataset contains 16,185 images of 196 classes of cars. 
# The data is split into 8,144 training images and 8,041 testing images, 
# where each class has been split roughly in a 50-50 split. 
# Classes are typically at the level of Make, Model, Year, e.g. 2012 Tesla Model S or 2012 BMW M3 coupe.

def download_dataset(script):
    subprocess.run(["chmod", "+x", script])
    subprocess.run([script])

def preprocess_dataset(train_dir):
    # Load datasets
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        train_dir,
        label_mode='categorical',
        batch_size=32,
        image_size=(224, 224),  # Adjusted image size for simplicity
        shuffle=True
    )

    # Resize and rescale datasets
    resize_and_rescale = Sequential([Resizing(224, 224), Rescaling(1./255)])
    train_ds = train_ds.map(lambda x, y: (resize_and_rescale(x), y), num_parallel_calls=AUTOTUNE)
    return train_ds.prefetch(buffer_size=AUTOTUNE)

def print_image(image_path):
    image = load_img(image_path)
    plt.imshow(image)
    plt.show()

def plot_images(dataset, num_images=5):
    plt.figure(figsize=(10, 10))
    for images, labels in dataset.take(1):  # Take one batch
        for i in range(num_images):
            ax = plt.subplot(5, 5, i + 1)
            image = images[i].numpy().astype("uint8")
            label = labels[i].numpy()
            if image.max() == 0:
                print(f"Image {i+1}: All pixels are black. Label: {label}")
            else:
                plt.imshow(image)
                plt.title(label)
                plt.axis("off")
    plt.show()

def debug_mode():
    download = True
    preprocess = True
    load = False
    train = False
    evaluate = False
    classify = False
    return download, preprocess, load, train, evaluate, classify

def main():
    download, preprocess, load, train, evaluate, classify = debug_mode()
    train_dir = './datasets/stanford/car_data/car_data/train'
    test_dir = './datasets/stanford/car_data/car_data/test'

    # 1. Download stanford dataset
    if download:
        print("\n📥 Downloading dataset...")
        download_dataset('./scripts/stanford_dataset.sh')
    
    # 2. Preprocess data
    if preprocess:
        print("\n⏳ Preprocessing data...")
        # print_image('./datasets/stanford/car_data/car_data/train/Acura Integra Type R 2001/00198.jpg')
        train_ds = preprocess_dataset(train_dir)
        plot_images(train_ds, 2)
        print("Data preprocessed successfully.")

if __name__ == "__main__":
    main()