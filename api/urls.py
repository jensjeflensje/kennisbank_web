from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('channels/', views.get_used_channels),
    path('answer/', views.get_answer),
]
