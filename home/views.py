from django.shortcuts import render, redirect
from home.models import Problem
from compiler.forms import CodeSubmissionForm
from compiler.models import CodeSubmission
from .forms import ProblemForm
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def problem_list(request):
    problems = Problem.objects.all()
    solved_ids = set()
    if request.user.is_authenticated:
        solved_ids = set(
            CodeSubmission.objects.filter(user=request.user, output_data='Accepted').values_list('problem_id', flat=True)
        )
    total = problems.count()
    solved_count = len(solved_ids)
    template = loader.get_template("problem_list.html")
    context = {
        'problems':problems,
        "solved_ids": solved_ids,
        "solved_count": solved_count,
        "total": total,
    }
    return HttpResponse(template.render(context, request))

def problem_detail(request, id):
    req_problem = Problem.objects.get(id=id)
    form = CodeSubmissionForm()
    template = loader.get_template("problem_detail.html")
    context = {
        "req_problem":req_problem,
        "form": form,
    }
    return HttpResponse(template.render(context, request))

def add_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/problems/') 
    else:
        form = ProblemForm()
    
    return render(request, 'add_problem.html', {'form': form})


