from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import password_validation
from django.core import exceptions


class user_form(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password','confirm_password']

    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        errors=dict()
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            errors['username']="username already exists"
            raise forms.ValidationError(errors)
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            errors['email']="email already exists"
            raise forms.ValidationError(errors)
        if password1 and password1 != password2:
            errors['password']="passwords don't match"
            raise forms.ValidationError(errors)
        try:
            password_validation.validate_password(password=password1,user=User)
        except exceptions.ValidationError as e:
            errors['password']=list(e.messages)
        if errors:
            raise forms.ValidationError(errors)
        return self.cleaned_data
