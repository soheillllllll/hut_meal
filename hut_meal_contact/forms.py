from django import forms
from django.core import validators

from hut_meal_contact.models import Contact


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(
        label='نام کامل',
        widget=forms.TextInput(attrs={'class': 'input-text', "placeholder": "enter your fullname", "type":"text", 'maxlength': '20'}))

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'input-text', "placeholder": "enter your email"}))

    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input-text validate-email", "placeholder": "enter your phone", "type": "text"}),
        validators=[
            validators.MaxLengthValidator(limit_value=11, message="نام کاربری نباید بیش از 11 کاراکتر باشد ")])

    message = forms.CharField(
        label='پیام شما',
        widget=forms.Textarea(attrs={'class': 'required-entry input-text', "cols":"5", "rows":"3", "title":"Comment", "name":"comment"}))

    class Meta:
        model = Contact
        fields = ('name', 'email','phone', 'message')
