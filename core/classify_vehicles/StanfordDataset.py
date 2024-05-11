import os
import subprocess
import pandas as pd
from torch.utils.data import Dataset
from PIL import Image

class StanfordDataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
        self.data = pd.read_csv(csv_file, header=None)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_name = self.data.iloc[idx, 0]
        img_path = subprocess.check_output(['find', self.root_dir, '-name', img_name]).decode().strip()
        image = Image.open(img_path)
        bbox = self.data.iloc[idx, 1:5].values.astype(float)
        class_label = self.data.iloc[idx, 5]
        metadata = self.get_metadata(img_path.split('/')[-2].split(' '))

        if self.transform:
            image = self.transform(image)

        return image, bbox, class_label, metadata

    # Get vehicle metadata and check if the make is compound
    def get_metadata(self, parts):
        is_make_compound = ' '.join(parts[:2]) in ['Aston Martin', 'Land Rover']
        metadata = {
            'make': ' '.join(parts[:2]) if is_make_compound else parts[0],
            'model': ' '.join(parts[2:-1]) if is_make_compound else ' '.join(parts[1:-1]),
            'year': parts[-1]
        }
        return metadata
               