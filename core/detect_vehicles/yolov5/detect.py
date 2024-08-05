import time
from torchvision import transforms
from PIL import Image

def get_transforms(width, height):
    return transforms.Compose([
        transforms.Resize((width, height))
    ])

def detect_image(model, image_file):
    width = 720; height = 1280
    image = Image.open(image_file)
    transformed_image = get_transforms(width, height)(image)
    start = time.process_time()
    predicted_image = model(transformed_image)
    end = time.process_time() - start
    return predicted_image, round(end, 4)

