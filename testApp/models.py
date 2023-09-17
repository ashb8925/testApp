from django.db import models

# Create your models here.

class MCQs(models.Model):
    ques = models.CharField(max_length=255)
    opt1 = models.CharField(max_length=100)
    opt2 = models.CharField(max_length=100)
    opt3 = models.CharField(max_length=100)
    opt4 = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)
