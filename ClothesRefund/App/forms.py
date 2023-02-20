from .models import Clothes
from django import forms

# This is the form for the clothes, it contains the name, the material, the size, the brand and the color of the clothes.

class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['ClothesName']