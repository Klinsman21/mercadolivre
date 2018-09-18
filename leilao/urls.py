"""ML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from leilao import views

app_name = 'leilao'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('create/', views.CreateProduct.as_view(), name='create'),
    path('search/', views.Search.as_view(), name='search'),
    path('throw/', views.Throw.as_view(), name='throw'),
    path('my-throw/', views.MeusLances.as_view(), name='my-throw'),
    path('my-product/', views.MyProduct.as_view(), name='my'),
    path('update/<pk>/', views.ProductUp.as_view(), name='update'),
]
