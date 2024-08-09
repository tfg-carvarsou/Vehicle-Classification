import time
from torchvision import transforms
from PIL import Image

def get_transforms(width, height):
    return transforms.Compose([
        transforms.Resize((height, width))
    ])

def detect_yv5_image(model, image_file):
    width = 1280; height = 720
    image = Image.open(image_file)
    transformed_image = get_transforms(width, height)(image)
    start = time.process_time()
    predicted_image = model(transformed_image)
    end = time.process_time() - start
    arr_labels = predicted_image.xyxyn[0][:, -1].numpy()
    return Image.fromarray(predicted_image.render()[0].astype('uint8')), round(end, 4), arr_labels

