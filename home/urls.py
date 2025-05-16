from django.urls import path
from . import views

urlpatterns = [
    path('problems/', views.problem_list, name='problem_list'),
    path('problems/<int:id>/', views.problem_detail, name='problem_detail'),
    path('problem_add/', views.add_problem, name='add_problem'),
]