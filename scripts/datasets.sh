#!/bin/bash

# Get the absolute path of the directory where this script resides
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

# Define the target directory
TARGET_DIR="$SCRIPT_DIR/../datasets/vehicles"

# Check if the directory exists, if not, create it
if [ ! -d "$TARGET_DIR" ]; then
    mkdir -p "$TARGET_DIR" || { echo "Failed to create directory $TARGET_DIR"; exit 1; }
fi

# Navigate to the datasets/vehicles folder
cd "$TARGET_DIR" || { echo "Failed to navigate to directory $TARGET_DIR"; exit 1; }

# Download the vehicles dataset
curl -L "https://universe.roboflow.com/ds/yMpTPUk83y?key=IdCQYHz9sx" > roboflow.zip

# Unzip the dataset
unzip roboflow.zip

# Remove the downloaded zip file
rm roboflow.zip
