from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import template1
# Create your views here.


def main(request):
    return HttpResponse("<h1>Welcome to Artfolio!</h1>")


def selectTemplate(request):
    return render(request, 'selectTemplate.html')


def editTemplate1(request):
    template = template1()
    template.save()
    return render(request, 'editTemplate1.html', {'template1': template})
