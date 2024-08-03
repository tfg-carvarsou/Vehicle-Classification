from django import forms

class VDImageUploadForm(forms.Form):
    model = forms.ChoiceField(choices=[('YOLOv5s', 'R-CNN')])
    image = forms.ImageField()