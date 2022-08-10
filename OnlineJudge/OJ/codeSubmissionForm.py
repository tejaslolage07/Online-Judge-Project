from django.shortcuts import render
from django.http import HttpResponse, Http404
# from models.py import Problem, Solution, TestCase
from django.views import generic
from django.urls import reverse
from django import forms

class CodeSubmission(forms.Form):
    # return HttpResponse("You are at the code submission page of problem %s" % problem_id)
    
    # model = Problem
    context_object_name = 'problem'
    # template_name = 'OJ/codeSubmission.html'
    compiler = forms.Select()
    userCode  = forms.CharField(label="Enter the code here", max_length = 10000)