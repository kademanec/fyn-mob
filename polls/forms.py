
from django import forms
from django.forms import ModelForm
from .models import PricingConfig

class PricingConfigForm(ModelForm):
    class Meta:
        model = PricingConfig
        
        fields = ('distanceBasePrice', 'distanceAdditionalPrice', 'timeMultiplierFactor','distance')

        widgets = {
            'distanceBasePrice': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Distance Base Price'}),
            'distanceAdditionalPrice': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Distance Additional Price'}),
            'timeMultiplierFactor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Time multiplier factor'}),
            'distance':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Distance'})
        }