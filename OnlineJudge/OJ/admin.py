from django.contrib import admin
from .models import Problem, UserSubmission, TestCase

admin.site.register(Problem)
admin.site.register(UserSubmission)
admin.site.register(TestCase)
