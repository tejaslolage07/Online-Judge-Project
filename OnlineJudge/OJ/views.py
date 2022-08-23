from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Problem, UserSubmission, TestCase, UserData
from django.views import generic
from django.urls import reverse
from django import forms
from .forms import CodeSubmission, RegistrationForm, RegistrationForm2
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# import sys
# sys.path.insert(
#     0, '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/coderunner')
from .database_fetch import problem_number, compiler, user_code, input_test_cases, output_test_cases
from .write import writeCpp
from .runCpp import main

# from .textout import writeCpp

# from .forms import NameForm

# Create your views here.
''' Will have a view for 
    1. signup/login screen,
    2. problems list,
    3, problem details,
    4. submission of code,
    5. Judge verdict
'''


def Registration(request):
    if request.user.is_authenticated:
        return redirect('Problems')
    else:
        form = RegistrationForm2()
        if request.method == 'POST':
            form = RegistrationForm2(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)
                return redirect("Login")
        context = {'form': form}
        return render(request, 'OJ/registrationTemplate.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Problems')
    else:
        context = {}
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Problems')
            else:
                messages.info(
                    request, "The username-password combination does not exist")
                return redirect("Login")
        context = {}
        return render(request, "OJ/loginTemplate.html", context)


@login_required(login_url='Login')
def logoutUser(request):
    logout(request)
    return redirect('Login')


@login_required(login_url='Login')
def problemsList(request):
    try:
        problem_list = Problem.objects.order_by('problemDifficulty')
    except Problem.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'OJ/problemList.html', {'problem_list': problem_list})


@login_required(login_url='Login')
def problemDetails(request, id):
    problem = get_object_or_404(Problem, pk=id)
    return render(request, "OJ/problemDetails.html", {'problem': problem})


@login_required(login_url='Login')
def codeSubmission(request, id):
    problemOBJ = Problem.objects.get(id=id)
    form = CodeSubmission()
    if request.method == 'POST':
        form = CodeSubmission(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.compiler == 'Select':
                messages.info(request, "Please select a compiler")
                return redirect('Code', id)
            else:
                instance.problem = problemOBJ
                instance.submitted_at = datetime.now()
                instance.user = request.user
                instance.save()
                return redirect("Verdict", id)
    context = {'form': form}
    return render(request, 'OJ/codeSubmission.html', context)


@login_required(login_url='Login')
def judgeVerdict(request, id):
    writeCpp(request.user.id)
    # writeCpp(54)
    your_fate = main(1)
    if your_fate == 1:
        return render(request, "OJ/judgeVerdictAccepted.html")
    elif your_fate == 0:
        return render(request, "OJ/judgeVerdictWrongAns.html")
    elif your_fate == -1:
        return render(request, "OJ/judgeVerdictCompilationError.html")
