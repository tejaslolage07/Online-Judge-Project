from django import forms
from django.forms import ModelForm
from .models import Problem, UserSubmission, TestCase, UserData
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime

# class CodeSubmission(forms.Form):
#     # return HttpResponse("You are at the code submission page of problem %s" % problem_id)

#     # model = Problem
#     # context_object_name = 'problem'
#     # template_name = 'OJ/codeSubmission.html'
#     compiler = forms.Select()
#     userCode  = forms.CharField(label="Enter the code here", max_length = 10000)


class CodeSubmission(ModelForm):
    # userCode = forms.Textarea()
    # compiler = forms.TextInput()
    # # submitted_at = forms.DateTimeInput()
    # problem = forms.TextInput()

    # def save(self, commit=True):
    #     send = super(CodeSubmission, self).save(commit=False)
    #     send.submitted_at = datetime.now()
    #     if commit:
    #         send.save()
    #     return send
    class Meta:
        model = UserSubmission
        # submitted_at = datetime.now()
        fields = ['compiler', 'userCode', 'problem']
        widgets = {
            'userCode': forms.Textarea(attrs={'rows': '22', 'cols': '120', 'data-val': 'true', 'data-val-required': 'Please enter your code here'})
        }


class RegistrationForm(ModelForm):
    # username = forms.TextInput()
    # password = forms.TextInput()

    class Meta:
        model = UserData
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'data-val': 'true', 'data-val-required': 'Please enter your user name'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'data-val': 'true', 'data-val-required': 'Please enter your password'}),
        }


class RegistrationForm2(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
