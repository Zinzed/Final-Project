from django.db import models

# Create your models here.


class project(models.Model):
    title = models.CharField(max_length=100, default="Hello World")
    finalImg = models.ImageField
    finalImgCap = models.CharField(max_length=100)
    explanation = models.CharField(max_length=1000)


class template1(models.Model):
    project1 = project

