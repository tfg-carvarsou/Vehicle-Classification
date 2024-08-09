from django import forms

class VDImageUploadForm(forms.Form):
    model = forms.ChoiceField(choices=[('YOLOv5s', 'YOLOV5S'), ('YOLOv8s', 'YOLOV8S')])
    image = forms.ImageField()

class VCImageUploadForm(forms.Form):
    model = forms.ChoiceField(choices=[('EfficientNetB1', 'EFFNETB1'), ('X', 'X')])
    image = forms.ImageField()