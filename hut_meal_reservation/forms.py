from django import forms
from django.contrib.auth import get_user_model
from django.core import validators


class ReservationForm(forms.Form):
    name = forms.CharField(
        widget= forms.TextInput(attrs={"type":"text", "placeholder":"enter your name"})
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={"type":"email", "placeholder": "enter your email"}),
        validators=[
            validators.EmailValidator("ایمیل نامعتبر است !")
        ])

    table = forms.CharField(
        widget=forms.RadioSelect(attrs={'onchange': 'this.form.submit();', "name": "table"})
    )
