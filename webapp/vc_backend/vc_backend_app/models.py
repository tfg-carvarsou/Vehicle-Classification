import secrets, string
from django.db import models
from .enums import VDModel, VCModel

def get_image_upload_path(instance, filename):
    """Function to determine the upload path for the image"""
    return f'detect_vehicles/{instance.model}/{filename}'

class VDImage(models.Model):
    code = models.CharField(max_length=12, unique=True)
    image = models.ImageField(upload_to=get_image_upload_path)
    model = models.TextField(choices=[(model.value, model.name) for model in VDModel],
                             default=VDModel.YOLOV5S.value)
    inf_time = models.FloatField(default=0.)
    label_count_dict = models.JSONField(default=dict)

    def __str__(self):
        return "Filename: {} | Model: {} | Inference time: {}".format(
            self.image.name, self.model, self.inf_time
        )
    
    @staticmethod
    def generate_secure_code(length=12):
        """Generates a secure random alphanumeric code"""
        charset = string.ascii_letters + string.digits
        return ''.join(secrets.choice(charset) for _ in range(length))
    
    def save(self, *args, **kwargs):
        """Override the save method to assign a unique code before saving"""
        if not self.code:
            self.code = self.generate_secure_code()
        super().save(*args, **kwargs)
