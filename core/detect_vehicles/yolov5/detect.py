import time
from torchvision import transforms
from PIL import Image

def get_transforms(width, height):
    return transforms.Compose([
        transforms.Resize((height, width))
    ])

def detect_image(model, image_file):
    width = 1280; height = 720
    image = Image.open(image_file)
    transformed_image = get_transforms(width, height)(image)
    start = time.process_time()
    predicted_image = model(transformed_image)
    end = time.process_time() - start
    return predicted_image, round(end, 4)

