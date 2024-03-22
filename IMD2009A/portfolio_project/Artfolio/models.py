from django.db import models
from PIL import Image

# Create your models here.


# class project(models.Model):
#     title = models.CharField(max_length=100, default="Hello World")
#     finalImg = models.ImageField
#     finalImgCap = models.CharField(max_length=100)
#     explanation = models.CharField(max_length=1000)

class filterTag(models.Model):
    filterTag = models.CharField(max_length=100)

#     graphicDesign
#     gameDesign
#     fashion
#     traditionalArt
#     interiorDesign
#     industrialDesign
#     architecture


class template(models.Model):
    filterTag = models.ManyToManyField(filterTag, default='none')

    project1Title = models.CharField(max_length=100, default="Project 1 Title")
    p1FinalImg = models.ImageField(upload_to='projectImages')
    p1FinalCap = models.CharField(max_length=50, default="final product caption")
    p1ProgressImg1 = models.ImageField(upload_to='projectImages')
    p1ProgressImg2 = models.ImageField(upload_to='projectImages')
    p1ProgressImg3 = models.ImageField(upload_to='projectImages')
    p1ProgressCap1 = models.CharField(max_length=50, default="progress image 1 caption")
    p1ProgressCap2 = models.CharField(max_length=50, default="progress image 2 caption")
    p1ProgressCap3 = models.CharField(max_length=50, default="progress image 3 caption")
    p1Explanation = models.CharField(max_length=300, default="short explanation of your design process")

    project2Title = models.CharField(max_length=100, default="Project 2 Title")
    p2FinalImg = models.ImageField(upload_to='projectImages')
    p2FinalCap = models.CharField(max_length=50, default="final product caption")
    p2ProgressImg1 = models.ImageField(upload_to='projectImages')
    p2ProgressImg2 = models.ImageField(upload_to='projectImages')
    p2ProgressImg3 = models.ImageField(upload_to='projectImages')
    p2ProgressCap1 = models.CharField(max_length=50, default="progress image 1 caption")
    p2ProgressCap2 = models.CharField(max_length=50, default="progress image 2 caption")
    p2ProgressCap3 = models.CharField(max_length=50, default="progress image 3 caption")
    p2Explanation = models.CharField(max_length=300, default="short explanation of your design process")

    project3Title = models.CharField(max_length=100, default="Project 3 Title")
    p3FinalImg = models.ImageField(upload_to='projectImages')
    p3FinalCap = models.CharField(max_length=50, default="final product caption")
    p3ProgressImg1 = models.ImageField(upload_to='projectImages')
    p3ProgressImg2 = models.ImageField(upload_to='projectImages')
    p3ProgressImg3 = models.ImageField(upload_to='projectImages')
    p3ProgressCap1 = models.CharField(max_length=50, default="progress image 1 caption")
    p3ProgressCap2 = models.CharField(max_length=50, default="progress image 2 caption")
    p3ProgressCap3 = models.CharField(max_length=50, default="progress image 3 caption")
    p3Explanation = models.CharField(max_length=300, default="short explanation of your design process")

    project4Title = models.CharField(max_length=100, default="Project 4 Title")
    p4FinalImg = models.ImageField(upload_to='projectImages')
    p4FinalCap = models.CharField(max_length=50, default="final product caption")
    p4ProgressImg1 = models.ImageField(upload_to='projectImages')
    p4ProgressImg2 = models.ImageField(upload_to='projectImages')
    p4ProgressImg3 = models.ImageField(upload_to='projectImages')
    p4ProgressCap1 = models.CharField(max_length=50, default="progress image 1 caption")
    p4ProgressCap2 = models.CharField(max_length=50, default="progress image 2 caption")
    p4ProgressCap3 = models.CharField(max_length=50, default="progress image 3 caption")
    p4Explanation = models.CharField(max_length=300, default="short explanation of your design process")
