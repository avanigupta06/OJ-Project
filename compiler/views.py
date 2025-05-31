from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from compiler.forms import CodeSubmissionForm
from compiler.models import CodeSubmission
from home.models import Problem, HiddenTestCase
# from compiler.utils import get_code_review 
from django.conf import settings
from pathlib import Path
import uuid
import os
import subprocess

@login_required
def run_code_view(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)

    if request.method == "POST":
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            action = request.POST.get("action")
            code = form.cleaned_data["code"]
            language = form.cleaned_data["language"]
            input_data = form.cleaned_data["input_data"]

            if action == "run":
                # Just run code (do not save)
                output = run_code(language, code, input_data)
                return render(request, "problem_detail.html", {
                    "req_problem": problem,
                    "form": form,
                    "output": output
                })

            elif action == "submit":
                # save form
                submission = form.save(commit=False)
                submission.user = request.user
                submission.problem = problem
                submission.input_data = input_data
                submission.expected_output = problem.output_testcase

                hidden_testcases = HiddenTestCase.objects.filter(problem=problem)
                all_passed = True

                for test in hidden_testcases:
                    test_output = run_code(
                        language,
                        code,
                        test.input_data
                    ).strip()
                    expected_output = test.expected_output.strip()

                    if test_output != expected_output:
                        all_passed = False
                        break

                submission.output_data = "Accepted" if all_passed else "Rejected"

                # ai review
                # review = get_code_review(language, problem.description)
                # submission.ai_feedback = review


                submission.save()

                return redirect("run_result", submission_id=submission.id)

    else:
        form = CodeSubmissionForm()

    return render(request, "problem_detail.html", {
        "req_problem": problem,
        "form": form
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

    if language == "cpp":
        executable_path = codes_dir / unique
        compile_result = subprocess.run(
                ["g++", str(code_file_path), "-o", str(executable_path)],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
        if compile_result.returncode == 0:
            with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
                subprocess.run(
                    [str(executable_path)],
                    stdin=input_file,
                    stdout=output_file,
                    stderr=subprocess.STDOUT,
                    timeout=5
                )
        else:
            # Capture compile errors
            return compile_result.stderr.decode('utf-8')

    elif language == "python":
        python_cmd = "python" if os.name == "nt" else "python3"
        with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
            subprocess.run(
                [python_cmd, str(code_file_path)],
                stdin=input_file,
                stdout=output_file,
                stderr=subprocess.STDOUT,
                timeout=5
        )

    with open(output_file_path, "r") as output_file:
        output_data = output_file.read()

    return output_data


def run_result(request, submission_id):
    submission = get_object_or_404(CodeSubmission, id=submission_id)
    return render(request, "run_result.html", {"submission": submission})


from django.core.paginator import Paginator

@login_required
def submission_list_view(request):
    submissions = CodeSubmission.objects.all().order_by('-timestamp')
    paginator = Paginator(submissions, 10)  # 10 submissions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "submission_list.html", {"page_obj": page_obj})

@login_required
def submission_history_view(request):
    submissions = CodeSubmission.objects.filter(user=request.user).select_related('problem').order_by('-timestamp')
    return render(request, 'submission_history.html', {
        "submissions": submissions
    })