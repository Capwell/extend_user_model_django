from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('create_user/', views.create_user, name='create_user'),
]
