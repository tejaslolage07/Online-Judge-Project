from django.db import models
from django.utils import timezone


class Problem(models.Model):
    problemStatement = models.CharField(max_length=500)
    problemName = models.CharField(max_length=50)
    problemDifficulty = models.CharField(max_length=100)


class Solution(models.Model):
    userCode = models.CharField(max_length=10000)
    verdict = models.CharField(max_length=300)
    submitted_at = models.DateTimeField("time of submission")
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)


class TestCase(models.Model):
    Input = models.CharField(max_length=300)
    Output = models.CharField(max_length=300)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
