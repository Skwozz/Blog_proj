from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = get_user_model()  # Используем кастомную модель пользователя, если она есть
#         fields = ['username', 'email', 'password1', 'password2']
#
# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField(label="Username")
#     password = forms.CharField(widget=forms.PasswordInput)