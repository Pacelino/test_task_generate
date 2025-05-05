from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm
import random


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'generator/register.html', {'form': form})
@login_required
def generate_code_auth(request):
    code = random.randint(1000, 9999)
    logout(request)
    return render(request, 'generator/code_auth.html', {'code': code})


def generate_code(request):
    code = random.randint(1000, 9999)
    logout(request)
    return render(request, 'generator/code_auth.html', {'code': code})