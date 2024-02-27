import logging

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import template
from .forms import templateForm
# Create your views here.


def main(request):
    myTemplate = template.objects.first()
    if myTemplate is None:
        return render(request, 'firstMain.html')
    else:
        return render(request, 'main.html')


def selectTemplate(request):
    myTemplate = template.objects.first()
    if myTemplate is None:
        return render(request, 'selectTemplate.html')
    else:
        url = reverse('editTemplate', kwargs={"templateId": myTemplate.id})
        return redirect(url)


def newTemplate(request):
    form = templateForm()
    if request.method == "POST":
        form = templateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, 'newTemplate.html', {'templateForm': form})


def editTemplate(request, templateId):
    myTemplate = template.objects.get(pk=templateId)
    form = templateForm(instance=myTemplate)
    if request.method == "POST":
        form = templateForm(request.POST, instance=myTemplate)
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, 'editTemplate.html', {'templateForm': form})


