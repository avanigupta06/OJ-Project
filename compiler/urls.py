from django.urls import path
from compiler.views import run_code_view, run_result, submission_list_view

urlpatterns = [
    path("run/<int:problem_id>/", run_code_view, name="run_code"),
    path("run/result/<int:submission_id>/", run_result, name="run_result"),
     path('submissions/', submission_list_view, name='submission_list'),
]
