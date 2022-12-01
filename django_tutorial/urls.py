"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from community.views import index
from .views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('community/', include('community.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', index, name='index'),
    # 인증 관련 path 모두 포함시키기
    path('accounts/', include('django.contrib.auth.urls')),
    # login 인증 path
    path('account/register/', UserCreateView.as_view(), name='register'),
    path('account/register/done/', UserCreateDoneTV.as_view(), name="register_done"),
]
