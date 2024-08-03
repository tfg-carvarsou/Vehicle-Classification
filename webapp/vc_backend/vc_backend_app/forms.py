from django import forms

class VDImageUploadForm(forms.Form):
    model = forms.ChoiceField(choices=[('YOLOv5s', 'YOLOV5S'), ('R-CNN', 'RCNN')])
    image = forms.ImageField()