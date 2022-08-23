from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class UserCreateForm(forms.ModelForm):

    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'style': 'width: 500px;', 'class':'form-control'}), required=True)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, required=True)
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'style': 'width: 500px;', 'class':'form-control'}), required=True)
    first_name = forms.CharField(label='Primeiro Nome', widget=forms.TextInput(attrs={'style': 'width: 500px;', 'class':'form-control'}), required=True)
    last_name =  forms.CharField(label='Segundo Nome', widget=forms.TextInput(attrs={'style': 'width: 500px;', 'class':'form-control'}), required=True)


    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')