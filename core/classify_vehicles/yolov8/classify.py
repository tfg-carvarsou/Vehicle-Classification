from torchvision import transforms
from PIL import Image

def get_transforms(width, height):
    return transforms.Compose([
        transforms.Resize((height, width))
    ])

def classify_yv8_image(model, image_file):
    width = 1280; height = 720
    image = Image.open(image_file)
    transformed_image = get_transforms(width, height)(image)
    predicted_image = model(transformed_image)
    for r in predicted_image:
        predicted_image = r.plot()
        pred_class_idx = r.probs.top1
        end = r.speed['inference']
        pred_class = model.names[int(pred_class_idx)]
    return Image.fromarray(predicted_image[..., ::-1]), round(end, 1), pred_class