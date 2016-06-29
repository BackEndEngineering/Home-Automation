from django import forms
from .models import Gadget, Action
from django.contrib.auth.models import User

class GadgetForm(forms.ModelForm):
    class Meta:
        model = Gadget
        fields = ['gadget_id', 'ip_address']

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['component', 'value','completed']

class CreateUserForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        widgets = {
            'password': forms.TextInput(attrs={'type': 'password'}),
        }
