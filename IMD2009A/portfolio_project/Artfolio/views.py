import logging

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import template
from .forms import templateForm
# Create your views here.


def main(request):
    return HttpResponse("<h1>Welcome to Artfolio!</h1>")


def selectTemplate(request):
    myTemplate = template.objects.first()
    if myTemplate is None:
        return render(request, 'selectTemplate.html')
    else:
        url = reverse('editTemplate', kwargs={"templateId": myTemplate.id})
        return redirect(url)


def newTemplate(request):
    form = templateForm()
    print('1')
    if request.method == "POST":
        form = templateForm(request.POST)
        print("2")
        if form.is_valid():
            print('3')
            form.save()
            return redirect('selectTemplate')
    return render(request, 'newTemplate.html', {'templateForm': form})


def editTemplate(request, templateId):
    myTemplate = template.objects.get(pk=templateId)
    form = templateForm(instance=myTemplate)
    print('1')
    if request.method == "POST":
        form = templateForm(request.POST, instance=myTemplate)
        print("2")
        if form.is_valid():
            print('3')
            form.save()
            return redirect('selectTemplate')
    return render(request, 'editTemplate.html', {'templateForm': form})


def saveTemplate(request):
    if request.method == "POST":
        form = templateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request, 'editTemplate.html', {'templateForm': form})

