from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # 로그인 처리
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/마켓_로그인.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # 가입 후 로그인 처리
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/마켓_회원가입.html', {'form': form})
