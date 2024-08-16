# Vehicle-Classification

*Vehicle and license classification project (2024)*

## Introduction

In this project, the aim is to train machine learning models for **detection and classification of vehicles** and run them in a web application for real-time inference. The project focuses on utilizing computer vision techniques to automatically identify vehicles in a road and classify vehicles based on their make and model.

## Project Components
1. **Data Collection**: Download the [Roboflow-100 Vehicles Collection](https://universe.roboflow.com/roboflow-100/vehicles-q0x2v) for detection tasks and [Stanford Car Dataset](https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder) for classification tasks.
2. **Data Preprocessing**: Clean and preprocess the dataset to prepare it for training the models.
3. **Model Training**: Train computer vision models using state-of-the-art techniques and frameworks such as PyTorch.
4. **Evaluation**: Evaluate the trained models on test datasets to measure their accuracy, precision, and other measures.
5. **Deployment**: Integrate the trained models into an application for real-time vehicle detection and classification.


## Installation in Windows/Linux

### Prerequisites (only in Windows)

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

- Install a new environment:

    ```bash
    conda create --name env python=3.10
    ```
  If you already have an environment to use, downgrade the version as so:
    ```bash
    conda activate <your_env>
    conda install python=3.10
    ```

4. **Activate the Environment:**

    ```bash
    conda init
    conda activate env
    ```

    To deactivate:

    ```bash
    conda deactivate env
    ```

5. **Install the requirements:**

- Make sure Conda Environment is now activated. Then install Torch and other packages:

    ```bash
    pip install -r requirements.txt
    ```

- Install npm and node.js:

    ```bash
    # installs nvm (Node Version Manager)
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
    # download and install Node.js (you may need to restart the terminal)
    cd ~/.nvm && nvm install 22
    ```
## Usage

### Running the webapp API locally
- The app uses Swagger as the API framework.
    ```bash
    cd <path_to>/Vehicle-Classification/webapp/vc_backend
    # Generates .env file for local settings
    echo -e "DJANGO_KEY='$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')'\nDEBUG=True" > .env
    # Runs SQLite server
    ./manage.py makemigrations 
    ./manage.py migrate
    ./manage.py runserver
    ```

### Training the models
- Run the train file of each model in the core folder.
    ```bash
    python -m core.detect_vehicles.yolov5.train
    python -m core.detect_vehicles.yolov8.train
    ...
    ```

## License

This project is released under the Apache 2.0 License. For more information, check: https://www.apache.org/licenses/LICENSE-2.0.

## Contributors

Carlos Varela Soult (carvarsou).

## Acknowledgements

**TODO**

[Roboflow 100 Project.](https://universe.roboflow.com/roboflow-100)

[Stanford Car Dataset by J. Utrera.](https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder)