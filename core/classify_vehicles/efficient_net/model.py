import os
import torch.nn as nn
from torchvision import models

def get_model_path():
    pwd = os.getcwd()
    myuser = os.path.dirname(pwd)
    return os.path.join(myuser, '.cache/torch/hub/checkpoints')

def load_model(pretrained=True, fine_tune=True, num_classes=10):
    if pretrained:
        print('[INFO]: Loading pre-trained weights')
    else:
        print('[INFO]: Not loading pre-trained weights')
    model = models.efficientnet_b1(weights=models.EfficientNet_B1_Weights.DEFAULT)
    
    if fine_tune:
        print('[INFO]: Fine-tuning all layers...')
        for params in model.parameters():
            params.requires_grad = True
    elif not fine_tune:
        print('[INFO]: Freezing hidden layers...')
        for params in model.parameters():
            params.requires_grad = False
    # Change the final classification head
    model.classifier[1] = nn.Linear(in_features=1280, out_features=num_classes)
    return model