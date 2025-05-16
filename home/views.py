from django.shortcuts import render, get_object_or_404, redirect
from home.models import Problem
from .forms import ProblemForm
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def problem_list(request):
    problems = Problem.objects.all()
    template = loader.get_template("problem_list.html")
    context = {
        'problems':problems,
    }
    return HttpResponse(template.render(context, request))

def problem_detail(request, id):
    req_problem = Problem.objects.get(id=id)
    template = loader.get_template("problem_detail.html")
    context = {
        "req_problem":req_problem,
    }
    return HttpResponse(template.render(context, request))

def add_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/problems/') 
    else:
        form = ProblemForm()
    
    return render(request, 'add_problem.html', {'form': form})


