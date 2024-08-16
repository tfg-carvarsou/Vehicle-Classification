#!/bin/bash

# Get the absolute path of the directory where this script resides
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

# Define the target directory
TARGET_DIR="$SCRIPT_DIR/../datasets/stanford/yolov8"

# Check if the directory exists, if not, create it
if [ -d "$TARGET_DIR" ]; then
    # Strip the prefix from the absolute path to get the relative path
    RELATIVE_PATH="${TARGET_DIR#$SCRIPT_DIR/}"
    echo "Directory $RELATIVE_PATH already exists. Aborting script."
    exit 1
else
    mkdir -p "$TARGET_DIR" || { echo "Failed to create directory $TARGET_DIR"; exit 1; }
fi
# Navigate to the datasets/stanford folder
cd "$TARGET_DIR" || { echo "Failed to navigate to directory $TARGET_DIR"; exit 1; }

# Stanford Car Dataset
kaggle datasets download -d jutrera/stanford-car-dataset-by-classes-folder

# Unzip the dataset
unzip stanford-car-dataset-by-classes-folder.zip

# Remove the downloaded zip file
rm stanford-car-dataset-by-classes-folder.zip