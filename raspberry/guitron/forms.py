from django import forms
from .models import Gadget, Action

class GadgetForm(forms.ModelForm):
    class Meta:
        model = Gadget
        fields = ['gadget_id', 'ip_address']

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['component', 'value','completed']
