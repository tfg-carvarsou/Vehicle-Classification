# Vehicle-Classification

*Vehicle and license classification project (2024)*

## Introduction

In this project, the aim is to develop machine learning models for the **classification of vehicles and license plates**. The project focuses on utilizing computer vision techniques to automatically identify and classify vehicles based on their make, model, and license plate information.

## Project Components
1. **Data Collection**: Gather a diverse dataset of vehicle images and corresponding license plate annotations.
2. **Data Preprocessing**: Clean and preprocess the dataset to prepare it for training the classification models.
3. **Model Training**: Train machine learning and deep learning models using state-of-the-art techniques and frameworks such as TensorFlow and OpenCV.
4. **Evaluation**: Evaluate the trained models on test datasets to measure their accuracy, precision, and recall.
5. **Deployment**: Integrate the trained models into an application for real-time vehicle and license plate classification.


## Installation

### Prerequisites

1. **Prior to installing WSL in Windows**
- Search in Windows: Control Panel > Programs > Activate or deactive Windows features.
- Enable "Virtual Machine Platform", "Windows Hypervisor Platform" and "Windows Subsytem for Linux".
- Restart your PC after making those changes.

2. **Steps to install WSL in Windows**
- Go to Microsoft Store and install "Windows Subsystem for Linux".
- Open Windows Powershell as Administrator and check if WSL is installed:

    ```bash
    wsl --status
    ```
- Go back to Microsoft Store and install "Debian" or "Ubuntu".
- Open the chosen OS terminal and create a UNIX user and password. Then install git:

    ```bash
    sudo apt update && sudo apt install git
    ```

- Open VS Code and select the blue button in the bottom left corner to create a Remote Connection with WSL option.

### Steps to Install the Environment

1. **Clone the repository:**

- Open a new terminal in VS Code and execute:

    ```bash
    git clone https://github.com/carvarsou/Vehicle-Classification
    ```

2. **Install Miniconda:**

- Execute these commands to install Miniconda:

    ```bash
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
    bash Miniconda3-latest-Linux-x86_64.sh
    ```
- Check if Miniconda is added to the PATH:

    ```bash
    nano ~/.bashrc
    export PATH="$HOME/miniconda3/bin:$PATH"
    ```

- Reload the Shell Configuration:

    ```bash
    source ~/.bashrc
    ```

- Verify installation:

    ```bash
    conda --version
    ```

3. **Create a Conda Environment:**

- Make sure you have Python 3.7 installed:

    ```bash
    conda create --name directml python=3.7
    ```
  Otherwise, downgrade it as so:
    ```bash
    conda create --name directml python=<your_version>
    conda activate directml
    conda install python=3.7
    ```

4. **Activate the Environment:**

    ```bash
    conda init
    conda activate directml
    ```

    To deactivate:

    ```bash
    conda deactivate directml
    ```

5. **Install the requirements:**

- Make sure Conda Environment is now activated. Then install TensorFlow and other packages:

    ```bash
    pip install -r requirements.txt
    ```

- Install and enable Docker Desktop for WSL following these instructions:

    https://docs.docker.com/desktop/wsl/

- Create a container for Elasticsearch services:

    ```bash
    docker pull docker.elastic.co/elasticsearch/elasticsearch:8.12.1
    docker-compose up
    ```

## Usage

**TODO**

1. **Download the datasets:**

    ```bash
    chmod +x ./scripts/datasets.sh
    ./scripts/datasets.sh
    ```

2. **Train the model:**

    ```bash
    python main.py
    ```

## License

This project is released under the Apache 2.0 License. For more information, check: https://www.apache.org/licenses/LICENSE-2.0.

## Contributors

Carlos Varela Soult (carvarsou).

## Acknowledgements

**TODO**

Roboflow 100:
https://universe.roboflow.com/roboflow-100

