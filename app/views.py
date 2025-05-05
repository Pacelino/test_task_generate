from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import random


@login_required
def generate_code_auth(request):
    code = random.randint(1000, 9999)
    logout(request)
    return render(request, 'generator/code_auth.html', {'code': code})