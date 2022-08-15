from django.db import models
from django.utils import timezone


class Problem(models.Model):
    problemStatement = models.CharField(max_length=500)
    problemName = models.CharField(max_length=50)
    problemDifficulty = models.CharField(max_length=100)

compiler_choices = (
    ('Select', 'Select your desired compiler'),
    ('GNU G++ 17', 'C++'),
    ('Java', 'Java'),
    ('Python 3', 'Python'),
)

class UserSubmission(models.Model):
# class Submission(models.Model):
    userID = models.IntegerField()
    userCode = models.CharField(max_length=10000)
    compiler = models.CharField(max_length=20, choices=compiler_choices, default='Select')
    verdict = models.CharField(max_length=300)
    submitted_at = models.DateTimeField("time of submission")
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)


class TestCase(models.Model):
    Input = models.CharField(max_length=300)
    Output = models.CharField(max_length=300)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
