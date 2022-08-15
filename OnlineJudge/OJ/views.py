from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Problem, UserSubmission, TestCase
from django.views import generic
from django.urls import reverse
from django import forms
from .codeSubmissionForm import CodeSubmission
# from .forms import NameForm

# Create your views here.
''' Will have a view for 
    1. signup/login screen,
    2. problems list,
    3, problem details,
    4. submission of code,
    5. Judge verdict
'''

# Using generic views:

# class Login(generic.ListView):
#     # return HttpResponse("You are at the Login/signup page.")
#     model = Problem
#     template_name = 'OJ/login.html'
#     context_object_name = 'login'



# class ProblemsList(generic.ListView):
#     ProblemList = Problem.objects.order_by('problemDifficulty')
#     # template = loader.get_template('OJ/index.html')
#     # context = {
#     #     ProblemList
#     # }
#     # output = ', '.join([q.problem.ProblemName for q in ProblemList])
    
#     # return render(request, 'OJ/problemList.html', {'ProblemList': ProblemList})

#     template_name = 'OJ/problemList.html'
#     context_object_name = 'ProblemList'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Problem.objects.order_by('problemDifficulty')



# class ProblemDetails(generic.DetailView):
    
#     # def get_queryset(self):
#     #     problem_id = int(self.kwargs['id'])
#     #     # queryset = Problems.objects.filter(id=problem_id)
#     #     return problem_id

#     # try:
#     #     problem = Problems.objects.get(pk=problem_id)
#     # except Problems.DoesNotExist:
#     #     raise Http404("Problem does not exist")
#     # # return render(request, 'OJ/problemDetails.html', {'problem': problem})
#     # return HttpResponse("You are at the details page of problem %s" % problem_id)

#     model = Problem
#     context_object_name = 'problem' # This means you can change the object name (the current instance (problem_id)) to some other name. The orignal is object.
#     template_name = 'OJ/problemDetails.html'


# class JudgeVerdict(generic.DetailView):
#     # return HttpResponse("You are at the Judge verdict page for problem %s" % problem_id)
#     model = Problem
#     context_object_name = 'Verdict'
#     template_name = 'OJ/judgeVerdict.html'


    
# class CodeSubmission(generic.DetailView):
#     # return HttpResponse("You are at the code submission page of problem %s" % problem_id)
    
#     model = Problem
#     context_object_name = 'problem'
#     template_name = 'OJ/codeSubmission.html'

    
# class CodeSubmission(forms.Form):
#     # return HttpResponse("You are at the code submission page of problem %s" % problem_id)
    
#     model = Problem
#     context_object_name = 'problem'
#     template_name = 'OJ/codeSubmission.html'
#     compiler = forms.Select()
#     userCode  = forms.CharField(label="Enter the code here", max_length = 10000)
    

# from OJ.codeSubmissionForm import CodeSubmission
    # if request.method == "POST":
    #     form = CodeSubmission(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect('problems/<int:id>/code/verdict/')
    #     else:
    #         form = CodeSubmission()

    #     return render(request, 'codeSubmission.html', {'form': form})
    

    # form = CodeSubmission()
    # return render(request, "OJ/codeSubmission.html", {'form' : form})




def Login(request):
    return render(request, "OJ/login.html")


def problemsList(request):
    try:
        # try_problem = Problem.objects.get(pk=1)
        problem_list = Problem.objects.order_by('problemDifficulty')
    except Problem.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'OJ/problemList.html', {'problem_list' : problem_list})


def problemDetails(request, id):
    problem = get_object_or_404(Problem, pk=id)
    return render(request, "OJ/problemDetails.html", {'problem' : problem})


def judgeVerdict(request, id):
    return render(request, "OJ/judgeVerdict.html")


def codeSubmission(request, id):
    return render(request, 'OJ/codeSubmission.html')