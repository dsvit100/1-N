from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # auth_login
            # 입력한 정보(form.get_user)가 db에 있는지 확인해주고 일치하다면 세션 발급까지 진행하는 함수
            return redirect('articles:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')