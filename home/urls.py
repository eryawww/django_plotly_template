from django.urls import path
from . import views
from home.dash_apps import example

urlpatterns = [
    path('', views.home, name='home')
]

