import time, cv2, numpy as np
from torchvision import transforms
from torch.nn import functional as F
from torch import topk
from PIL import Image
from .model import get_classes, DEVICE

def generate_cams(feature_conv, weight_softmax, class_idx, width=224, height=224):
    # generate the class activation maps upsample to 224x224
    size_upsample = (width, height)
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

def load_cv2_image(image_file, width, height):
    image_file.seek(0)
    image_bytes = image_file.read()
    image_array = np.frombuffer(image_bytes, np.uint8)
    image_cv2 = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return cv2.resize(image_cv2, (width, height))

def get_cam_image(cams, width, height, image_file, pred_class):
    image_cv2 = load_cv2_image(image_file, width, height)
    for _, cam in enumerate(cams):
        heatmap = cv2.applyColorMap(cv2.resize(cam,(width, height)), cv2.COLORMAP_JET)
        result = heatmap * 0.3 + image_cv2 * 0.5
        cv2.putText(img=result, 
            text=pred_class, 
            org=(20, 80), 
            fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
            fontScale=1.5, 
            color=(0, 0, 0), 
            thickness=3, 
            lineType=cv2.LINE_AA)
    return result

features_blobs = []
def hook_feature(module, input, output):
    features_blobs.append(output.data.cpu().numpy())

def get_transforms(width=224, height=224):
    return transforms.Compose([
        transforms.Resize((height, width)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

def classify_image(model, image_file):
    width = 1280; height = 720
    model._modules.get('features').register_forward_hook(hook_feature)
    params = list(model.parameters())
    image = Image.open(image_file)
    image_tensor = get_transforms()(image).unsqueeze(0)
    classes = get_classes()
    # forward pass through model
    start = time.process_time()
    outputs = model(image_tensor.to(DEVICE))
    # get softmax probabilities
    probs = F.softmax(input=outputs, dim=1).data.squeeze()
    # get class indices of top k probabilities
    class_idx = topk(probs, 1)[1].int()
    pred_class = classes[int(class_idx)].strip()
    weight_softmax = np.squeeze(params[-2].data.numpy())
    cams = generate_cams(features_blobs[0], weight_softmax, class_idx)
    predicted_image = get_cam_image(cams, width, height, image_file, pred_class)
    end = time.process_time() - start
    return predicted_image, round(end, 4), pred_class