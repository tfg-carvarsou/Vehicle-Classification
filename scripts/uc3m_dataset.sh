#!/bin/bash

# Get the absolute path of the directory where this script resides
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

# Define the target directory
TARGET_DIR="$SCRIPT_DIR/../datasets/uc3m"

# Check if the directory exists, if not, create it
if [ -d "$TARGET_DIR" ]; then
    # Strip the prefix from the absolute path to get the relative path
    RELATIVE_PATH="${TARGET_DIR#$SCRIPT_DIR/}"
    echo "Directory $RELATIVE_PATH already exists. Aborting script."
    exit 1
else
    mkdir -p "$TARGET_DIR" || { echo "Failed to create directory $TARGET_DIR"; exit 1; }
fi
# Navigate to the datasets/uc3m folder
cd "$TARGET_DIR" || { echo "Failed to navigate to directory $TARGET_DIR"; exit 1; }

# UC3M-LP Dataset
gdown https://drive.google.com/uc?id=1UMY-WCRl0tIL_EVMugMH5F7Btl5UE4Wu

# Unzip the dataset
unzip UC3M-LP.zip

# Remove the downloaded zip file
rm UC3M-LP.zip