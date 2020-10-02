from django import forms
from .models import *


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['employee_name', 'Image']
