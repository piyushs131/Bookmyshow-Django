from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username or Email', max_length=254)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if '@' in username:
            # If the username looks like an email, we can handle it here
            cleaned_data['username'] = CustomUser.objects.filter(email=username).first().username
        return cleaned_data 