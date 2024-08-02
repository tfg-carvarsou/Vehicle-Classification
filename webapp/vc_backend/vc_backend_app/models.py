import secrets, string
from django.db import models


class VDImage(models.Model):
    code = models.CharField(max_length=12, unique=True, blank=True)
    image = models.ImageField(upload_to='detect_vehicles/yolov5s/')

    def __str__(self):
        return self.image.name
    
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
