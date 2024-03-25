import tensorflow as tf
import pandas as pd
import os
import matplotlib.pyplot as plt
import cv2
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
load_dotenv()
tf.compat.v1.enable_eager_execution()

"""Example on detection: /home/carvarsou/Vehicle-Classification/datasets/vehicles/a/train/
filename,width,height,class,xmin,ymin,xmax,ymax
adit_mp4-2_jpg.rf.fdf2998eb42800e8136ec33eb5724f59.jpg,640,480,bus-l-,322,151,362,193
adit_mp4-2_jpg.rf.fdf2998eb42800e8136ec33eb5724f59.jpg,640,480,car,294,167,312,182
...

Train: 2634
Test: 458
Valid: 966
"""

ELASTIC_USER = os.getenv("ELASTIC_USER")
ELASTIC_PASS = os.getenv("ELASTIC_PASS")
INDEX_NAME = 'roboflow-vehicles'
INDEX_SETTINGS = {
    "mappings": {
        "properties": {
            "filename": {
                "type": "text"
            },
            "size": {
                "type": "text"
            },
            "vehicles": {
                "type": "text"
            }
        }
    }
}

# --- Read functions ---
def read_csv(data_dir: str, csv_file: str):
    return pd.read_csv(os.path.join(data_dir, csv_file))

def collect_filenames(data_dir: str, csv_file: str):
    df = read_csv(data_dir, csv_file)
    filenames = set()
    for i in range(len(df)):
        filename = os.path.join(data_dir, df['filename'][i])
        filenames.add(filename)
    return filenames

def read_images(es: Elasticsearch, data_dir: str, csv_file: str):
    df = read_csv(data_dir, csv_file)
    ld = [] # List of images
    d = {} # Image dictionary
    prev_filename = None

    for i in range(len(df)):
        filename = os.path.join(data_dir, df['filename'][i]) # Current filename
        if filename != prev_filename: # New filename in d
            if d:
                ld.append(d)
                index_image(es, INDEX_NAME, d)
            d = {
                'filename': filename,
                'size': (df['width'][i], df['height'][i]),
                'vehicles': []
            }
        d['vehicles'].append((df['class'][i], df['xmin'][i], df['ymin'][i], df['xmax'][i], df['ymax'][i]))
        prev_filename = filename

    ld.append(es)
    # Index d in Elasticsearch
    index_image(es, INDEX_NAME, d)

    return ld

def index_image(es: Elasticsearch, index_name: str, image_dict: dict):

    # Index the image dictionary
    res = es.index(index=index_name, id=image_dict['filename'], document=image_dict)

    # Print the response
    print(res)

def reset_index(es: Elasticsearch, index_name: str) -> None:
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)

    es.indices.create(index=index_name, body=INDEX_SETTINGS)

def display_image(img_dict: dict):
    img = cv2.imread(img_dict[0]['filename'])
    bbox_coords = img_dict[0]['vehicles'][0][1:]
    img_bbox = cv2.rectangle(img, (bbox_coords[0], bbox_coords[1]), (bbox_coords[2], bbox_coords[3]), (0, 255, 0), 2)
    
    img_rgb = cv2.cvtColor(img_bbox, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.show()

def write_to_text_file(processed_data, output_file):
    with open(output_file, 'w') as file:
        c = 0
        for d in processed_data:
            file.write(f"Filename: {d['filename']}\n")
            file.write(f"Size: {d['size']}\n")
            file.write("Vehicles:\n")
            for vehicle in d['vehicles']:
                file.write(f"\t{vehicle}\n")
            file.write("\n")
            c+=1
        print("Count when writing: " + str(c))


# --- Main ---
def main():
    data_dir = 'datasets/vehicles/a/train'
    csv_file = '_annotations.csv'
    es =  Elasticsearch(
        hosts=["http://localhost:9200"],
        basic_auth=(ELASTIC_USER, ELASTIC_PASS),
    )
    reset_index(es, INDEX_NAME)
    img_dict = read_images(es, data_dir, csv_file)
    print("Size of img_dict: " + str(len(img_dict)))
    # output_file = 'dict.txt'
    # write_to_text_file(img_dict, output_file)

    display_image(img_dict)

if __name__ == "__main__":
    main()

