from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Problem, UserSubmission, TestCase, UserData
from django.views import generic
from django.urls import reverse
from django import forms
from .forms import CodeSubmission, RegistrationForm, RegistrationForm2
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

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


def Login(request):
    context = {}
    return render(request, "OJ/loginTemplate.html", context)


def problemsList(request):
    try:
        # try_problem = Problem.objects.get(pk=1)
        problem_list = Problem.objects.order_by('problemDifficulty')
    except Problem.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'OJ/problemList.html', {'problem_list': problem_list})


def problemDetails(request, id):
    problem = get_object_or_404(Problem, pk=id)
    return render(request, "OJ/problemDetails.html", {'problem': problem})


def codeSubmission(request, id):
    form = CodeSubmission()
    if request.method == 'POST':
        form = CodeSubmission(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    # return HttpResponse("The form is valid. Thanks.")
    return render(request, 'OJ/codeSubmission.html', context)


def judgeVerdict(request, id):
    return render(request, "OJ/judgeVerdict.html")
