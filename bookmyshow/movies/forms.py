from django import forms
from .models import Movie, Category

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['category', 'title', 'description', 'duration', 'poster', 'price']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
