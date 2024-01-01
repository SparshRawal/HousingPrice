from django import forms
from .models import HouseFeatures

class HouseFeaturesForm(forms.ModelForm):
    class Meta:
        model = HouseFeatures
        fields = '__all__'