"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
""" Platzigram URLs module"""
from django.urls import path
from platzigram import views

urlpatterns = [
    path('hello-world/', views.hello_world),
    path('sorted/', views.sort_integers),           #http://localhost:8000/sorted/?numbers=2,44,51,23,5,52
    path('hi/<str:name>/<int:age>/', views.say_hi) # http://localhost:8000/hi/Jose/10/
]
