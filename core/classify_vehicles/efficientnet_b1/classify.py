import torch
import os
import argparse
import numpy as np
import cv2
import glob as glob
from torchvision import transforms
from torch.nn import functional as F
from torch import topk
from model import load_model

DEVICE = ('cuda' if torch.cuda.is_available() else 'cpu')
IMAGES_PATH = './images/classify_vehicles/efficientnet_b1/'

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='path to input image', 
                    default=os.path.join(IMAGES_PATH, 'prueba.jpg'))
args = vars(parser.parse_args())

def get_trained_weights_path():
    pwd = os.getcwd()
    return os.path.join(pwd, 'models/classify_vehicles/efficientnet_b1/model.pth')

def get_classes():
    with open('./datasets/stanford/names.csv', 'r') as names:
        car_list = names.readlines()
    return car_list

def load_trained_model():
    weights_path = get_trained_weights_path()
    num_classes = len(get_classes())
    model = load_model(
            pretrained=True,
            fine_tune=True, 
            num_classes=num_classes
        ).to(DEVICE)
    model = model.eval()
    model.load_state_dict(torch.load(weights_path)['model_state_dict'])
    return model

def load_image(image_path):
    image = cv2.imread(image_path)
    orig_image = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return orig_image, image

def return_cam(feature_conv, weight_softmax, class_idx):
    # generate the class activation maps upsample to 224x224
    size_upsample = (224, 224)
    bz, nc, h, w = feature_conv.shape
    output_cam = []
    for idx in class_idx:
        cam = weight_softmax[idx].dot(feature_conv.reshape((nc, h*w)))
        cam = cam.reshape(h, w)
        cam = cam - np.min(cam)
        cam_img = cam / np.max(cam)
        cam_img = np.uint8(255 * cam_img)
        output_cam.append(cv2.resize(cam_img, size_upsample))
    return output_cam

def show_cam(cams, width, height, orig_image, class_idx, all_classes, save_name):
    for i, cam in enumerate(cams):
        heatmap = cv2.applyColorMap(cv2.resize(cam,(width, height)), cv2.COLORMAP_JET)
        result = heatmap * 0.3 + orig_image * 0.5
        # put class label text on the result
        cv2.putText(result, all_classes[class_idx[i]], (20, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
        cv2.imshow('CAM', result/255.)
        cv2.waitKey(0)
        cv2.imwrite(os.path.join(IMAGES_PATH, f"results/CAM_{save_name}"), result)

features_blobs = []
def hook_feature(module, input, output):
    features_blobs.append(output.data.cpu().numpy())
    print("AAAA: ", features_blobs)

def get_transforms():
    return transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

def main():
    #TODO Inference on vehicle image using EfficientNetB1
    model = load_trained_model()
    model._modules.get('features').register_forward_hook(hook_feature)
    print("Feature blobs ", features_blobs) #todel
    params = list(model.parameters())
    weight_softmax = np.squeeze(params[-2].data.numpy())

    image_path = os.path.join(IMAGES_PATH, 'prueba.jpg')
    print(image_path)
    orig_image, image = load_image(image_path)
    height, width, _ = orig_image.shape
    # get transforms
    transforms = get_transforms()
    image_tensor = transforms(image)
    image_tensor = image_tensor.unsqueeze(0)
    # forward pass through model
    outputs = model(image_tensor.to(DEVICE))
    # get softmax probabilities
    probs = F.softmax(outputs).data.squeeze()
    # get class indices of top k probabilities
    class_idx = topk(probs, 1)[1].int()
    classes = get_classes()

    cams = return_cam(features_blobs[0], weight_softmax, class_idx)
    show_cam(cams, height, width, orig_image, class_idx, classes, 'prueba.jpg')

if __name__ == '__main__':
    main()