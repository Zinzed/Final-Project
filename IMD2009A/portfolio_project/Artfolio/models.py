from django.db import models

# Create your models here.


class template1(models.Model):
    project1Title = models.CharField(max_length=100, default="Hello World")
    project1FinalImg = models.ImageField
    project1FinalImgCap = models.CharField(max_length=100)
    project1Explanation = models.CharField(max_length=1000)
