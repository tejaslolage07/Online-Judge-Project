from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Problems, Solutions, Test_cases
from django.views import generic
from django.urls import reverse

# Create your views here.
''' Will have a view for 
    1. signup/login screen,
    2. problems list,
    3, problem details,
    4. submission of code,
    5. Judge verdict
'''

# Using generic views:

class login_signup(generic.DetailView):
    # return HttpResponse("You are at the Login/signup page.")
    template_name = 'OJ/login.html'
    context_object_name = 'login'


class ProblemsList(generic.ListView):
    ProblemList = Problems.objects.order_by('problemDifficulty')
    # template = loader.get_template('OJ/index.html')
    # context = {
    #     ProblemList
    # }
    # output = ', '.join([q.problem.ProblemName for q in ProblemList])
    
    # return render(request, 'OJ/problemList.html', {'ProblemList': ProblemList})

    template_name = 'OJ/problemList.html'
    context_object_name = 'ProblemList'

    def get_queryset(self):
        """Return the last five published questions."""
        return Problems.objects.order_by('problemDifficulty')

class ProblemDetails(generic.DetailView):
    
    # def get_queryset(self):
    #     problem_id = int(self.kwargs['id'])
    #     # queryset = Problems.objects.filter(id=problem_id)
    #     return problem_id

    # try:
    #     problem = Problems.objects.get(pk=problem_id)
    # except Problems.DoesNotExist:
    #     raise Http404("Problem does not exist")
    # # return render(request, 'OJ/problemDetails.html', {'problem': problem})
    # return HttpResponse("You are at the details page of problem %s" % problem_id)

    model = Problems
    context_object_name = 'problem' # This means you can change the object name (the current instance (problem_id)) to some other name. The orignal is object.
    template_name = 'OJ/problemDetails.html'


    
class CodeSubmission(generic.DetailView):
    # return HttpResponse("You are at the code submission page of problem %s" % problem_id)
    model = Problems
    context_object_name = 'problem'
    template_name = 'OJ/codeSubmission.html'

    

class JudgeVerdict(generic.DetailView):
    # return HttpResponse("You are at the Judge verdict page for problem %s" % problem_id)
    model = Solutions
    context_object_name = 'problem'
    template_name = 'OJ/judgeVerdict.html'
    