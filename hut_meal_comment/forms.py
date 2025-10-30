

from django import forms
from django.core import validators
from .models import Comment, CommentProduct, CommentBlog


class CommentForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"id":"name" ,"type":"text", "placeholder":"Name"}),)

    email = forms.EmailField(
        widget=forms.TextInput(attrs={"id":"email","type":"email", "placeholder":"Email"}),
        validators=[validators.EmailValidator("ایمیل نامعتبر است !")]
    ),

    body = forms.CharField(
        widget=forms.Textarea(attrs={"name":"comment" , "placeholder":"Message..."}))


class CommentProductForm(CommentForm):

    class Meta:
        model = CommentProduct
        fields = ('name', 'email', 'body')

class CommentBlogForm(CommentForm):

    class Meta:
        model = CommentBlog
        fields = ('name', 'email', 'body')