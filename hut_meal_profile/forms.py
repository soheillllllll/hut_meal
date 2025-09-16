from django import forms
from django.contrib.auth import get_user_model
from django.core import validators


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(attrs={"type":"text", "placeholder":"enter your username"})
    )
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={"type":"text", "placeholder":"enter your password"})
    )




User = get_user_model()
class UserAccountForm(forms.Form):
    first_name = forms.CharField(
        widget= forms.TextInput(attrs={"type":"text", "placeholder":"Enter your name."})
    )
    last_name = forms.CharField(
        widget= forms.TextInput(attrs={"type":"text", "placeholder":"Enter your last name."})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"type":"text", "placeholder": "enter your username"}),
        validators=[
            validators.MaxLengthValidator(limit_value=20, message="نام کاربری نباید بیش از 20 کاراکتر باشد ")
        ])
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"type":"email", "placeholder": "enter your email"}),
        validators=[
            validators.EmailValidator("ایمیل نامعتبر است !")
        ])

    phone = forms.CharField(

        widget=forms.TextInput(attrs={"type":"text", "placeholder": "enter your phone"}),
        validators=[
            validators.MaxLengthValidator(limit_value=11, message="نام کاربری نباید بیش از 11 کاراکتر باشد ")
        ])

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"type":"text", "placeholder": "enter your password"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"type":"text", "placeholder": "re enter your password"}))
    address = forms.CharField(
        widget=forms.TextInput(attrs={"class":"full-form", 'placeholder': 'enter your address'})
    )
    company = forms.CharField(
        widget=forms.TextInput(attrs={"type":"text", 'placeholder': 'enter your Company'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("Email must contain a gmail address")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Passwords must match")
        return data