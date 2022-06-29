from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Problems, Solutions, Test_cases

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
    ProblemList = Problems.objects.order_by('problemDifficulty')
    # template = loader.get_template('OJ/index.html')
    # context = {
    #     ProblemList
    # }
    # output = ', '.join([q.problem.ProblemName for q in ProblemList])
    return render(request, 'OJ/problemList.html', {'ProblemList': ProblemList})

def ProblemDetails(request, problem_id):
    try:
        problem = Problems.objects.get(pk=problem_id)
    except Problems.DoesNotExist:
        raise Http404("Problem does not exist")
    return render(request, 'OJ/problemDetails.html', {'problem': problem})
    # return HttpResponse("You are at the details page of problem %s" % problem_id)
    
def CodeSubmission(request, problem_id):
    return HttpResponse("You are at the code submission page of problem %s" % problem_id)

def JudgeVerdict(request, problem_id):
    return HttpResponse("You are at the Judge verdict page for problem %s" % problem_id)

    