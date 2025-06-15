# urls.py
from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('accounts/login/', lambda request: redirect('/auth/login/')),  # redirect fallback
    path('', views.dashboard, name='dashboard'),
    path('auth/login/', views.login_user, name='login'),
    path('auth/register/', views.register_user, name='register'),
    path('auth/logout/', views.logout_user, name='logout'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
]
