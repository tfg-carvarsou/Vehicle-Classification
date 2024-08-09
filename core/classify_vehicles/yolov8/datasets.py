import os
import csv
import subprocess

BASE_DIR = './datasets/stanford/yolov8/'
TRAIN_DIR = os.path.join(BASE_DIR, 'car_data/car_data/train/')
TEST_DIR = os.path.join(BASE_DIR, 'car_data/car_data/test/')
NAMES_CSV = os.path.join(BASE_DIR, 'names.csv')
ANNO_TRAIN = os.path.join(BASE_DIR, 'anno_train.csv')
ANNO_TEST = os.path.join(BASE_DIR, 'anno_test.csv')

# We are using a subset of the dataset for this project.
# The Stanford Cars dataset subset contains 3933 images of 49 classes of cars,
# where 1977 images are used for training and 1956 images are used for testing.
# Classes are typically at the level of Make, Model, Year, e.g. 2012 Tesla Model S or 2012 BMW M3 coupe.

def get_ds_path():
    return BASE_DIR

def download_dataset(script):
    subprocess.run(["chmod", "+x", script])
    subprocess.run([script])

def crop_dataset():
    """
    Function to crop the datasets.
    Reduces the training and test datasets size.
    """
    # Crop names.csv
    with open(NAMES_CSV, 'r') as names:
        car_list = names.readlines()
    unique_cars = {}
    for car in car_list:
        new_car = car.split(' ')[0]
        if new_car not in unique_cars:
            unique_cars[new_car] = car.strip()
    unique_cars["Ram"] = "Ram C-V Cargo Van Minivan 2012"
    unique_car_list = list(unique_cars.values())
    with open(NAMES_CSV, 'w') as names:
        for car in unique_car_list:
            names.write(car)
            names.write('\n')
    
    # Crop train and test folders
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

    # Crop anno_train.csv and anno_test.csv
    with open(ANNO_TRAIN, 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)
    filtered_lines = [line for line in lines if line[0] in train_unique_images_set]
    with open(ANNO_TRAIN, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(filtered_lines)
    with open(ANNO_TEST, 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)
    filtered_lines = [line for line in lines if line[0] in test_unique_images_set]
    with open(ANNO_TEST, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(filtered_lines)