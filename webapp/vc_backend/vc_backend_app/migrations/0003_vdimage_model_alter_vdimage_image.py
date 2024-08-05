# Generated by Django 4.2 on 2024-08-03 10:02

from django.db import migrations, models
import vc_backend_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('vc_backend_app', '0002_vdimage_code_alter_vdimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vdimage',
            name='model',
            field=models.TextField(choices=[('YOLOV5S', 'YOLOv5s'), ('RCNN', 'R-CNN')], default='YOLOv5s'),
        ),
        migrations.AlterField(
            model_name='vdimage',
            name='image',
            field=models.ImageField(upload_to=vc_backend_app.models.get_image_upload_path),
        ),
    ]
