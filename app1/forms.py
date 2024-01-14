from django import forms
from .models import Users

class RegistrationForms(forms.ModelForm):
    class Meta:
        model= Users
        fields=['first_name','last_name','email','password']


    def __init__(self, *args, **kwargs):
        super(RegistrationForms, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'



class LoginForms(forms.ModelForm):
    class Meta:
        model= Users
        fields=['email','password']


    def __init__(self, *args, **kwargs):
        super(LoginForms, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


