from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('<int:guild_id>/', views.view_guild),
    path('<int:guild_id>/questions/', views.add_question),
    path('<int:guild_id>/questions/<int:question_id>/', views.edit_question),
    path('<int:guild_id>/questions/<int:question_id>/delete/', views.delete_question),
    path('<int:guild_id>/channels/', views.add_channel),
    path('<int:guild_id>/channels/<int:channel_id>/', views.edit_channel),
    path('<int:guild_id>/channels/<int:channel_id>/delete/', views.delete_channel),
]
