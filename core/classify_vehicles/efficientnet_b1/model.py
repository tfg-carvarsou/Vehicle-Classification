import os
import torch
import torch.nn as nn
from torchvision import models

DEVICE = ('cuda' if torch.cuda.is_available() else 'cpu')

def get_model_path():
    pwd = os.getcwd()
    myuser = os.path.dirname(pwd)
    return os.path.join(myuser, '.cache/torch/hub/checkpoints')

def load_model(fine_tune=True, num_classes=10):
    model = models.efficientnet_b1(weights=models.EfficientNet_B1_Weights.DEFAULT)
    if fine_tune:
        for params in model.parameters():
            params.requires_grad = True
    elif not fine_tune:
        for params in model.parameters():
            params.requires_grad = False
    # Change the final classification head
    model.classifier[1] = nn.Linear(in_features=1280, out_features=num_classes)
    return model

def print_model_info(parameters, layers):
    print('-------------------------\nEfficientNetB1 🚀 2024-8-4')
    print(f'Model summary: {layers} layers, {parameters} parameters\n')

def get_trained_weights_path():
    pwd = os.getcwd()
    return os.path.join(pwd, 'models/classify_vehicles/efficientnet_b1/model.pth')

def get_classes():
    with open('./core/classify_vehicles/efficientnet_b1/names/names.csv', 'r') as names:
        car_list = names.readlines()
    return car_list

def get_total_layers(model):
    total_layers = 0
    for child in nn.Module.children(model):
        if list(child.children()):  # If the child module has children, it's a container
            total_layers += get_total_layers(child)
        else:
            total_layers += 1  # Each non-container module counts as a layer
    return total_layers

def get_total_parameters(model):
    return sum(x.numel() for x in model.parameters())

def load_trained_effnetb1_model():
    weights_path = get_trained_weights_path()
    num_classes = len(get_classes())
    model = load_model(
            fine_tune=False, 
            num_classes=num_classes
        ).to(DEVICE)
    parameters = get_total_parameters(model)
    layers = get_total_layers(model)
    print_model_info(parameters, layers)
    model = model.eval()
    model.load_state_dict(torch.load(weights_path)['model_state_dict'])
    return model