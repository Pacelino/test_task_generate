"""
URL configuration for test_task_random_generate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from app import admin
from app.views import *
urlpatterns = [
       # path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/login/')),
    path('code-auth/', generate_code_auth, name='generate_code_auth'),
    path('generate-code/', generate_code, name='generate_code'),
    path('register/', register_view, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='generator/login.html'), name='login'),
]
