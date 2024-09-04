from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'login__input',
            'placeholder': '아이디를 입력해주세요',
            'id': 'username',
            'aria-invalid': 'false',
            'aria-describedby': 'usernameError',
        }),
        label='아이디'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'login__input',
            'placeholder': '이메일을 입력해주세요',
            'id': 'email',
            'aria-invalid': 'false',
            'aria-describedby': 'emailError',
        }),
        label='이메일'
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'login__input',
            'placeholder': '비밀번호를 입력해주세요',
            'id': 'password1',
            'aria-invalid': 'false',
            'aria-describedby': 'password1Error',
        }),
        label='비밀번호'
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'login__input',
            'placeholder': '비밀번호를 다시 입력해주세요',
            'id': 'password2',
            'aria-invalid': 'false',
            'aria-describedby': 'password2Error',
        }),
        label='비밀번호 확인'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'login__input',
            'placeholder': '아이디를 입력해주세요',
            'id': 'username',
            'aria-invalid': 'false',
            'aria-describedby': 'usernameError',
        }),
        label='아이디'
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'login__input',
            'placeholder': '비밀번호를 입력해주세요',
            'id': 'password',
            'aria-invalid': 'false',
            'aria-describedby': 'passwordError',
        }),
        label='비밀번호'
    )

    class Meta:
        model = User
        fields = ('username', 'password')

from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')