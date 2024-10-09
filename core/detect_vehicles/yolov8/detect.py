import time
from torchvision import transforms
from PIL import Image

def get_transforms(width, height):
    return transforms.Compose([
        transforms.Resize((height, width))
    ])

def detect_yv8_image(model, image_file):
    width = 1280; height = 720
    image = Image.open(image_file)
    transformed_image = get_transforms(width, height)(image)
    predicted_image = model(transformed_image)
    for r in predicted_image:
        predicted_image = r.plot()
        end = r.speed['inference']
        arr_labels = r.boxes.cls.numpy()
    return Image.fromarray(predicted_image[..., ::-1]), round(end, 1), arr_labels