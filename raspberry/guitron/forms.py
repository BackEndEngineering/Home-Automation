from django import forms
from .models import Gadget

class GadgetForm(forms.ModelForm):
    class Meta:
        model = Gadget
        fields = ['gadget_id', 'ip_address']
