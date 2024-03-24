import tensorflow as tf
import pandas as pd
import os
import matplotlib.pyplot as plt
import cv2
tf.compat.v1.enable_eager_execution()

"""Example on detection: /home/carvarsou/Vehicle-Classification/datasets/vehicles/a/train/
filename,width,height,class,xmin,ymin,xmax,ymax
adit_mp4-2_jpg.rf.fdf2998eb42800e8136ec33eb5724f59.jpg,640,480,bus-l-,322,151,362,193
adit_mp4-2_jpg.rf.fdf2998eb42800e8136ec33eb5724f59.jpg,640,480,car,294,167,312,182
...
"""

# --- Read functions ---
def read_csv(data_dir: str, csv_file: str):
    return pd.read_csv(os.path.join(data_dir, csv_file))

# TODO - Read all vehicles in the image
def read_image(data_dir: str, csv_file: str):
    df = read_csv(data_dir, csv_file)
    return {
        'filename': os.path.join(data_dir, df['filename'][0]), 
        'size': (df['width'][0], df['height'][0]),
        'vehicles': [(df['class'][0], df['xmin'][0], df['ymin'][0], df['xmax'][0], df['ymax'][0])]
    }

def display_image(img_dict: dict):
    img = cv2.imread(img_dict['filename'])
    bbox_coords = img_dict['vehicles'][0][1:]
    img_bbox = cv2.rectangle(img, (bbox_coords[0], bbox_coords[1]), (bbox_coords[2], bbox_coords[3]), (0, 255, 0), 2)
    
    img_rgb = cv2.cvtColor(img_bbox, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.show()

# --- Main ---
def main():
    data_dir = 'datasets/vehicles/a/train'
    csv_file = '_annotations.csv'
    img_dict = read_image(data_dir, csv_file)
    display_image(img_dict)

if __name__ == "__main__":
    main()

