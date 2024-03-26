import tensorflow as tf
import pandas as pd
import os
import matplotlib.pyplot as plt
import cv2
import requests
from index_vehicles import RoboflowVehiclesIndex, Elasticsearch
tf.compat.v1.enable_eager_execution()
INDEX_NAME = RoboflowVehiclesIndex.INDEX_NAME
INDEX_SETTINGS = RoboflowVehiclesIndex.INDEX_SETTINGS

"""Example on detection: /home/carvarsou/Vehicle-Classification/datasets/vehicles/a/train/
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

# --- Other functions ---
def count_index_docs(index_name: str):
    response = requests.get("http://localhost:9200/"+index_name+"/_stats/docs")
    data = response.json()
    count = data['indices'][index_name]['primaries']['docs']['count']
    print("Total number of docs: " + str(count))

# TODO - Iterate through all vehicles in img_dict and display all bounding boxes
def display_image(es: Elasticsearch, index_name: str, data_dir: str, filename: str):
    # Get image dict from index
    param = os.path.join(data_dir, filename)
    query = es.search(index=index_name, body={"query": {"match": {"filename": param}}})
    img_dict = query['hits']['hits'][0]['_source']
    bbox_coords = img_dict['vehicles'][0][1:]

    # Display image with bounding box
    img = cv2.imread(img_dict['filename'])
    img_bbox = cv2.rectangle(img, (bbox_coords[0], bbox_coords[1]), (bbox_coords[2], bbox_coords[3]), (0, 255, 0), 2)
    img_rgb = cv2.cvtColor(img_bbox, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.show()


# --- Main ---
def main():
    es =  Elasticsearch("http://localhost:9200")
    data_dir = 'datasets/vehicles/a/train'
    csv_file = '_annotations.csv'
    RoboflowVehiclesIndex.reset_index(es, INDEX_NAME, INDEX_SETTINGS)
    read_images(es, INDEX_NAME, data_dir, csv_file)

    filename = 'adit_mp4-1843_jpg.rf.00408082bf814686c49908deb2728057.jpg'
    display_image(es, INDEX_NAME, data_dir, filename)

if __name__ == "__main__":
    main()

