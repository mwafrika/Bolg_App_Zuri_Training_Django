from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CommentModel


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': '4'}))

    class Meta:
        model = CommentModel
        fields = ('comment',)

    # def __str__(self):
    #     return f"{self.comment} by {self.author}"
# class LoginForm()
