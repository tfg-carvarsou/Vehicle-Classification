import os
import subprocess
import yaml

DS_DIR = './datasets/vehicles/yolov5'

# The Vehicles Dataset contains 4058 images of 12 classes of vehicles,
# where 2634 images are used for training, 966 images are used for validation 
# and 458 images are used for testing.
# Classes are:
# 'big bus', 'big truck', 'bus-l-', 'bus-s-', 'car', 
# 'mid truck', 'small bus', 'small truck', 'truck-l-', 'truck-m-', 'truck-s-', 'truck-xl-'

def download_dataset(script):
    subprocess.run(["chmod", "+x", script])
    subprocess.run([script])

def get_ds_path():
    return DS_DIR

def configure_yaml(ds_path):
    pwd = os.getcwd()
    yaml_file = os.path.join(ds_path, 'data.yaml')

    with open(yaml_file, 'r') as y:
        yaml_data = yaml.safe_load(y)

    yaml_data.update({
        'train': os.path.join(pwd, ds_path, 'train/images'),
        'val': os.path.join(pwd, ds_path, 'valid/images'),
        'test': os.path.join(pwd, ds_path, 'test/images')
    })

    with open(yaml_file, 'w') as y:
        yaml.safe_dump(yaml_data, y)