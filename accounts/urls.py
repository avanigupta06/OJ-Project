# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('auth/login/', views.login_user, name='login'),
    path('auth/register/', views.register_user, name='register'),
    path('auth/logout/', views.logout_user, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
