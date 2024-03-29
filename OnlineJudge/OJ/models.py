from django.db import models
from django.utils import timezone
from django.conf import settings
# from datetime import datetime


class Problem(models.Model):
    problemStatement = models.CharField(max_length=20000)
    problemName = models.CharField(max_length=500)
    problemDifficulty = models.CharField(max_length=100)


compiler_choices = (
    ('Select', 'Select your desired compiler'),
    ('GNU G++ 17', 'C++'),
    ('Java', 'Java'),
    ('Python 3', 'Python'),
)

class UserData(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    userEmail = models.EmailField(max_length=100)


class UserSubmission(models.Model):
    userCode = models.CharField(max_length=100000)
    compiler = models.CharField(
        max_length=50, choices=compiler_choices, default='Select')
    # verdict = models.CharField(max_length=300)
    submitted_at = models.DateTimeField("time of submission")
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     now = timezone.now()
    #     self.submitted_at = now
    #     super(UserSubmission, self).save(*args, **kwargs)


class TestCase(models.Model):
    Input = models.CharField(max_length=1000, blank=True)
    Output = models.CharField(max_length=1000, blank=True)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)