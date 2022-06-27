from django.db import models
from django.utils import timezone

# Create your models here.
class Problems(models.Model):
    problemStatement = models.CharField(max_length=500)
    ProblemName = models.CharField(max_length=50)
    UserCode = models.CharField(max_length=10000)
    ProblemDifficulty = models.CharField(max_length=500)
class Solutions(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=300)
    submitted_at = models.DateTimeField("time of submission")
class Test_cases(models.Model):
    Input = models.CharField(max_length=300)
    Output = models.CharField(max_length=300)
    problem = models.ForeignKey(Problems, models.CASCADE)