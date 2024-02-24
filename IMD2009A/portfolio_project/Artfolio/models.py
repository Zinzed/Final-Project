from django.db import models

# Create your models here.


# class project(models.Model):
#     title = models.CharField(max_length=100, default="Hello World")
#     finalImg = models.ImageField
#     finalImgCap = models.CharField(max_length=100)
#     explanation = models.CharField(max_length=1000)


class template(models.Model):
    project1Title = models.CharField(max_length=100, default="Title1")
    project2Title = models.CharField(max_length=100, default="Title2")


