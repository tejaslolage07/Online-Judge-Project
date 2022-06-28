from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
''' Will have a view for 
    1. signup/login screen,
    2. problems list,
    3, problem details,
    4. submission of code,
    5. Judge verdict
'''

def login_signup(request):
    return HttpResponse("You are at the Login/signup page.")

def ProblemsList(request):
    return HttpResponse("You are at the Problems list page.")

def ProblemDetails(request, problem_id):
    return HttpResponse("You are at the details page of problem %s" % problem_id)
    
def CodeSubmission(request, problem_id):
    return HttpResponse("You are at the code submission page of problem %s" % problem_id)

def JudgeVerdict(request, problem_id):
    return HttpResponse("You are at the Judge verdict page for problem %s" % problem_id)

    