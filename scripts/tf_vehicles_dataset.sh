#!/bin/bash

# Get the absolute path of the directory where this script resides
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

# Define the target directory
TARGET_DIR="$SCRIPT_DIR/../datasets/vehicles/tensorflow"

# Check if the directory exists, if not, create it
if [ -d "$TARGET_DIR" ]; then
    # Strip the prefix from the absolute path to get the relative path
    RELATIVE_PATH="${TARGET_DIR#$SCRIPT_DIR/}"
    echo "Directory $RELATIVE_PATH already exists. Aborting script."
    exit 1
else
    mkdir -p "$TARGET_DIR" || { echo "Failed to create directory $TARGET_DIR"; exit 1; }

# Navigate to the datasets/vehicles folder
cd "$TARGET_DIR" || { echo "Failed to navigate to directory $TARGET_DIR"; exit 1; }

# Tensorflow Vehicles Dataset
curl -L "https://universe.roboflow.com/ds/gV0Icgz9uI?key=VonD89jLsK" > tf_vd.zip

# Unzip the dataset
unzip tf_vd.zip

# Remove the downloaded zip file
rm tf_vd.zip
