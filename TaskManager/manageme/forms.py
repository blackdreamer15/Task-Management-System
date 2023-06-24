from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task, Category, Tag

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Please provide a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)