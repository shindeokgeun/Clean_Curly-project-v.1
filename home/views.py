
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from users.forms import CustomUserCreationForm, CustomAuthenticationForm  # forms 모듈 import

def index(request):
    return render(request, 'home/market.html')



