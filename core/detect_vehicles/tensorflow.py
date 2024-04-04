# import tensorflow as tf
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import requests
from ..indexes.index_vehicles import RoboflowVehiclesIndex, Elasticsearch
# tf.compat.v1.enable_eager_execution()

INDEX_NAME = RoboflowVehiclesIndex.INDEX_NAME
INDEX_SETTINGS = RoboflowVehiclesIndex.INDEX_SETTINGS

"""Example on detection: /home/carvarsou/Vehicle-Classification/datasets/vehicles/tensorflow/train/
filename,width,height,class,xmin,ymin,xmax,ymax
adit_mp4-2_jpg.rf.fdf2998eb42800e8136ec33eb5724f59.jpg,640,480,bus-l-,322,151,362,193
adit_mp4-2_jpg.rf.fdf2998eb42800e8136ec33eb5724f59.jpg,640,480,car,294,167,312,182
...

Train: 2634
Test: 458
Valid: 966
"""

# --- Read functions ---
def read_csv(data_dir: str, csv_file: str):
    return pd.read_csv(os.path.join(data_dir, csv_file))

def read_images(es: Elasticsearch, index_name: str, data_dir: str, csv_file: str):
    df = read_csv(data_dir, csv_file)
    d = {} # Image dictionary
    prev_filename = None

    for i in range(len(df)):
        filename = os.path.join(data_dir, df['filename'][i]) # Current filename
        if filename != prev_filename: # New filename in d
            if d:
                RoboflowVehiclesIndex.index_image(es, index_name, d)
            d = {
                'filename': filename,
                'size': (df['width'][i], df['height'][i]),
                'vehicles': []
            }
        d['vehicles'].append((df['class'][i], df['xmin'][i], df['ymin'][i], df['xmax'][i], df['ymax'][i]))
        prev_filename = filename

    RoboflowVehiclesIndex.index_image(es, index_name, d)

# --- Display functions ---
def count_index_docs(index_name: str):
    response = requests.get("http://localhost:9200/"+index_name+"/_stats/docs")
    data = response.json()
    count = data['indices'][index_name]['primaries']['docs']['count']
    print("Total number of docs: " + str(count))

def dict_classes_colors():
    return {
        'big bus': (0, 0, 255),     # Blue
        'big truck': (255, 255, 0), # Yellow
        'bus-l-': (0, 255, 0),      # Green
        'bus-s-': (255, 165, 0),    # Orange
        'car': (173, 216, 230),     # Light Blue
        'mid truck': (144, 238, 144), # Light Green
        'small bus': (72, 191, 145), # Ocean Green
        'small truck': (0, 0, 139), # Dark Blue
        'truck-l-': (255, 0, 0),    # Red
        'truck-m-': (169, 169, 169),# Gray
        'truck-s-': (128, 0, 128),  # Purple
        'truck-xl-': (255, 127, 127) # Pink
    }

def display_image(es: Elasticsearch, index_name: str, data_dir: str, filename: str):
    # Get image dict from index
    param = os.path.join(data_dir, filename)
    query = es.search(index=index_name, body={"query": {"match": {"filename": param}}})
    img_dict = query['hits']['hits'][0]['_source']

    list_bbox_coords = []
    for v in img_dict['vehicles']:
        list_bbox_coords.append(v[1:])

    # Display image with bounding box
    img = plt.imread(img_dict['filename'])
    _, ax = plt.subplots()
    
    classes_colors = dict_classes_colors()
    for class_index, b in enumerate(list_bbox_coords):
        class_name = img_dict['vehicles'][class_index][0]  # Get the label and color for the vehicle
        color = tuple(rgb/255 for rgb in classes_colors.get(class_name, (0, 0, 0)))
        img_bbox = patches.Rectangle((b[0], b[1]), b[2] - b[0], b[3] - b[1], linewidth=2, edgecolor=color, facecolor='none')
        ax.add_patch(img_bbox)
        ax.text(b[0], b[1]-10, class_name, fontsize=12, color=color)

    ax.imshow(img)
    plt.show()

# --- Model ---
# Faster R-CNN   

# --- Main ---
def main():
    es =  Elasticsearch("http://localhost:9200")
    data_dir = 'datasets/vehicles/tensorflow/train'
    csv_file = '_annotations.csv'
    RoboflowVehiclesIndex.reset_index(es, INDEX_NAME, INDEX_SETTINGS)
    read_images(es, INDEX_NAME, data_dir, csv_file)

    filename = 'pagi_16112021_mp4-581_jpg.rf.00c56fa5c3ce82f9d92e6e5ff9367430.jpg'
    display_image(es, INDEX_NAME, data_dir, filename)

if __name__ == "__main__":
    main()

