from django.shortcuts import render, redirect
from django.http import HttpResponse
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
        return redirect('editTemplate')


def editTemplate(request):
    myTemplate = template.objects.first()
    form = templateForm(instance=myTemplate)
    if request.method == "POST":
        form = templateForm(request.POST, instance=myTemplate)
        if form.is_valid():
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

