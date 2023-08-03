from django import forms
from . models import CheckModel

class CheckForm(forms.ModelForm):
    
    class Meta:
        model = CheckModel
        fields = '__all__'