from django.db import models
from django import forms
from .models import UploadImage
from django.forms import ModelForm

class UserImageForm(forms.ModelForm):
    class Meta:
        # To specify the model to be used to create form
        model = UploadImage
        # It includes all the fiels of model
        fields = '__all__'