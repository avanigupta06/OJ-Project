from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.core.paginator import Paginator
from compiler.forms import CodeSubmissionForm
from compiler.models import CodeSubmission
from home.models import Problem, HiddenTestCase, StarterCode
from compiler.utils import get_code_review 
from django.conf import settings
from pathlib import Path
from django.contrib import messages
from subprocess import TimeoutExpired
import uuid
import os
import subprocess

@never_cache
@login_required
def run_code_view(request, problem_id):
    
    problem = get_object_or_404(Problem, id=problem_id)

    # Get all starter codes once
    starter_codes = StarterCode.objects.all()
    starter_code_dict = {sc.language: sc.code for sc in starter_codes}

    if request.method == "POST":
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            action = request.POST.get("action")
            code = form.cleaned_data["code"]
            language = form.cleaned_data["language"]
            input_data = form.cleaned_data["input_data"]

            if action == "run":

                # Check if code is empty
                if not code.strip():
                    messages.error(request, "No code is given.")
                    return render(request, "problem_detail.html", {
                    "req_problem": problem,
                    "form": form,
                    "starter_codes": starter_code_dict
                })

                # Just run code (do not save)
                output, _ = run_code(language, code, input_data)
                form = CodeSubmissionForm(initial={
                    "code": code,
                    "language": language,
                    "input_data": input_data
                })
                return render(request, "problem_detail.html", {
                    "req_problem": problem,
                    "form": form,
                    "output": output,
                    "starter_codes": starter_code_dict
                })

            elif action == "clear":
            # Clear the form by creating a fresh instance
                form = CodeSubmissionForm()
                return render(request, "problem_detail.html", {
                    "req_problem": problem,
                    "form": form,
                    "output": "",
                    "starter_codes": starter_code_dict
                })
            
            elif action == "submit":
                # save form
                submission = form.save(commit=False)
                submission.user = request.user
                submission.problem = problem
                submission.input_data = input_data
                submission.expected_output = problem.output_testcase

                hidden_testcases = HiddenTestCase.objects.filter(problem=problem)

                verdict = "Accepted"

                for test in hidden_testcases:
                    test_output, status = run_code(language, code, test.input_data)
                    test_output = test_output.strip()
                    expected_output = test.expected_output.strip()

                    if status == "TLE":
                        verdict = "TLE"
                        break
                    elif status == "CE":
                        verdict = "Compile Error"
                        break
                    elif test_output != expected_output:
                        verdict = "Rejected"
                        break


                submission.output_data = verdict

                submission.save()

                return redirect("run_result", submission_id=submission.id)

            elif action == "ai_review":
                review = get_code_review(code, problem.description, language)
                return render(request, "problem_detail.html", {
                    "req_problem": problem,
                    "form": form,
                    "ai_feedback": review,  # pass review to template
                    "starter_codes": starter_code_dict
                })


    else:
        form = CodeSubmissionForm()

    return render(request, "problem_detail.html", {
        "req_problem": problem,
        "form": form,
        "starter_codes": starter_code_dict
    })


def run_code(language, code, input_data):
    project_path = Path(settings.BASE_DIR)
    directories = ["codes", "inputs", "outputs"]

    for directory in directories:
        dir_path = project_path / directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)

    codes_dir = project_path / "codes"
    inputs_dir = project_path / "inputs"
    outputs_dir = project_path / "outputs"

    unique = str(uuid.uuid4())

    ext_map = {
        "python": "py",
        "cpp": "cpp",
        "c" : "c",
    }
    file_ext = ext_map.get(language, "txt")

    code_file_path = codes_dir / f"{unique}.{file_ext}"
    input_file_path = inputs_dir / f"{unique}.txt"
    output_file_path = outputs_dir / f"{unique}.txt"

    with open(code_file_path, "w") as code_file:
        code_file.write(code)

    with open(input_file_path, "w") as input_file:
        input_file.write(input_data or "")

    # Create empty output file
    with open(output_file_path, "w") as output_file:
        pass

    try:
        if language == "cpp":
            executable_path = codes_dir / unique
            compile_result = subprocess.run(
                ["g++", str(code_file_path), "-o", str(executable_path)],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            if compile_result.returncode == 0:
                try:
                    with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
                        result = subprocess.run(
                        [str(executable_path)],
                        stdin=input_file,
                        stdout=output_file,
                        stderr=subprocess.PIPE,
                        timeout=5
                        )
                        if result.returncode != 0:
                            error_msg = result.stderr.decode('utf-8')
                            if not error_msg:
                                error_msg = "Runtime Error: Program exited with non-zero status."
                            return error_msg, "RE"
                except TimeoutExpired:
                 return "Time Limit Exceeded", "TLE"

            else:
            # Capture compile errors
             return compile_result.stderr.decode('utf-8'), "CE"

        
        elif language == "c":
            executable_path = codes_dir / unique
            compile_result = subprocess.run(
                ["gcc", str(code_file_path), "-o", str(executable_path)],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            if compile_result.returncode == 0:
                try:
                    with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
                        result = subprocess.run(
                        [str(executable_path)],
                        stdin=input_file,
                        stdout=output_file,
                        stderr=subprocess.PIPE,
                        timeout=5
                        )
                        if result.returncode != 0:
                            error_msg = result.stderr.decode('utf-8')
                            if not error_msg:
                                error_msg = "Runtime Error: Program exited with non-zero status."
                            return error_msg, "RE"
                except TimeoutExpired:
                    return "Time Limit Exceeded", "TLE"

            else:
            # Capture compile errors
                return compile_result.stderr.decode('utf-8'), "CE"


        elif language == "python":
            python_cmd = "python" if os.name == "nt" else "python3"
            try:
                with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
                    result = subprocess.run(
                    [python_cmd, str(code_file_path)],
                    stdin=input_file,
                    stdout=output_file,
                    stderr=subprocess.PIPE,
                    timeout=5
                    )
                    if result.returncode != 0:
                        error_msg = result.stderr.decode('utf-8')
                        if not error_msg:
                            error_msg = "Runtime Error: Program exited with non-zero status."
                        return error_msg, "RE"
            except TimeoutExpired:
                return "Time Limit Exceeded", "TLE"


        with open(output_file_path, "r") as output_file:
            output_data = output_file.read()

        return output_data, "OK"
    # remove files
    finally:
        if code_file_path.exists():
            os.remove(code_file_path)
        if input_file_path.exists():
            os.remove(input_file_path)
        if output_file_path.exists():
            os.remove(output_file_path)
        if language in ["c", "cpp"] and executable_path.exists():
            os.remove(executable_path)



@never_cache
@login_required
def run_result(request, submission_id):
    submission = get_object_or_404(CodeSubmission, id=submission_id)
    return render(request, "run_result.html", {"submission": submission})

@never_cache
@login_required
def submission_list_view(request):

    # Restrict access to only 'setter' and 'admin'
    if request.user.userextension.user_type not in ['setter', 'admin']:
        return HttpResponse("You are not authorized to access this page.", status=403)

    
    submissions = CodeSubmission.objects.all().order_by('-timestamp')
    paginator = Paginator(submissions, 10)  # 10 submissions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "submission_list.html", {"page_obj": page_obj})

@never_cache
@login_required
def back_to_problem_view(request, problem_id, submission_id):
    problem = get_object_or_404(Problem, id=problem_id)
    submission = get_object_or_404(CodeSubmission, id=submission_id, user=request.user)

    # Pre-fill the form
    form = CodeSubmissionForm(initial={
        "code": submission.code,
        "language": submission.language,
    })
    # Add this part to get all starter codes
    starter_codes = StarterCode.objects.all()
    starter_code_dict = {sc.language: sc.code for sc in starter_codes}

    return render(request, "problem_detail.html", {
        "req_problem": problem,
        "starter_codes": starter_code_dict,
        "form": form # This shows last result
    })