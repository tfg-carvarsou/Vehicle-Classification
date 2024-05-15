import os
import shutil
import csv
import subprocess
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

TRAIN_DIR = './datasets/stanford/car_data/car_data/train/'
TEST_DIR = './datasets/stanford/car_data/car_data/test/'
IMG_SIZE = 224
BATCH_SIZE = 16
NUM_WORKERS = 4

# We are using a subset of the dataset for this project.
# The Stanford Cars dataset subset contains 3933 images of 49 classes of cars,
# where 1977 images are used for training and 1956 images are used for testing.
# Classes are typically at the level of Make, Model, Year, e.g. 2012 Tesla Model S or 2012 BMW M3 coupe.

def download_dataset(script):
    subprocess.run(["chmod", "+x", script])
    subprocess.run([script])

def crop_dataset():
    """
    Function to crop the datasets.
    Reduces the training and test datasets size.
    """
    # Crop names.csv
    with open('./datasets/stanford/names.csv', 'r') as names:
        car_list = names.readlines()
    unique_cars = {}
    for car in car_list:
        new_car = car.split(' ')[0]
        if new_car not in unique_cars:
            unique_cars[new_car] = car.strip()
    unique_cars["Ram"] = "Ram C-V Cargo Van Minivan 2012"
    unique_car_list = list(unique_cars.values())
    with open('./datasets/stanford/names.csv', 'w') as names:
        for car in unique_car_list:
            names.write(car)
            names.write('\n')
    
    # # Crop train and test folders
    train_cars = set(os.listdir(TRAIN_DIR))
    test_cars = set(os.listdir(TEST_DIR))
    unique_car_set = set(unique_car_list)
    train_cars_to_delete = train_cars - unique_car_set
    test_cars_to_delete = test_cars - unique_car_set
    for car in train_cars_to_delete:
        subprocess.run(["rm", "-rf", f"{TRAIN_DIR}{car}"])
    for car in test_cars_to_delete:
        subprocess.run(["rm", "-rf", f"{TEST_DIR}{car}"])
    train_unique_images_set, test_unique_images_set = set(), set()
    for car in unique_car_set:
        train_found_images = subprocess.run(["find", f"{TRAIN_DIR}{car}", "-type", "f"], stdout=subprocess.PIPE)
        for image_path in train_found_images.stdout.splitlines():
            image_name = os.path.basename(image_path.decode())
            train_unique_images_set.add(image_name)
        test_found_images = subprocess.run(["find", f"{TEST_DIR}{car}", "-type", "f"], stdout=subprocess.PIPE)
        for image_path in test_found_images.stdout.splitlines():
            image_name = os.path.basename(image_path.decode())
            test_unique_images_set.add(image_name)

    # # Crop anno_train.csv and anno_test.csv
    with open('./datasets/stanford/anno_train.csv', 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)
    filtered_lines = [line for line in lines if line[0] in train_unique_images_set]
    with open('./datasets/stanford/anno_train.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(filtered_lines)
    with open('./datasets/stanford/anno_test.csv', 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)
    filtered_lines = [line for line in lines if line[0] in test_unique_images_set]
    with open('./datasets/stanford/anno_test.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(filtered_lines)

def get_train_transforms(img_size):
    return transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomRotation(35),
        transforms.RandomAdjustSharpness(sharpness_factor=2, p=0.5),
        transforms.RandomGrayscale(p=0.5),
        transforms.RandomPerspective(distortion_scale=0.5, p=0.5),
        transforms.RandomPosterize(bits=2, p=0.5),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

def get_test_transforms(img_size):
    return transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

def get_datasets():
    """
    Function to prepare the datasets.
    Returns the training and test datasets along with the class names.
    """
    train_ds = datasets.ImageFolder(
        TRAIN_DIR, 
        transform=(get_train_transforms(IMG_SIZE))
    )
    test_ds = datasets.ImageFolder(
        TEST_DIR, 
        transform=(get_test_transforms(IMG_SIZE))
    )
    return train_ds, test_ds, train_ds.classes

def get_data_loaders(train_ds, test_ds):
    """
    Prepares the training and test data loaders.
    :param train_ds: The training dataset.
    :param test_ds: The test dataset.
    Returns the training and test data loaders.
    """
    train_loader = DataLoader(
        train_ds, batch_size=BATCH_SIZE, shuffle=True, num_workers=NUM_WORKERS
    )
    test_loader = DataLoader(
        test_ds, batch_size=BATCH_SIZE, shuffle=False, num_workers=NUM_WORKERS
    )
    return train_loader, test_loader 