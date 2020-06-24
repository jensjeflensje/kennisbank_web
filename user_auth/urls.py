from . import views
from django.urls import path, include

urlpatterns = [
    path('login/', views.auth_login),
    path('logout/', views.auth_logout),
    path('callback/', views.callback),
]
