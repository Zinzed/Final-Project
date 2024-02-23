from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import template1
from .forms import template1Form
# Create your views here.


def main(request):
    return HttpResponse("<h1>Welcome to Artfolio!</h1>")


def selectTemplate(request):
    template = template1.objects.first()
    if template is None:
        return render(request, 'selectTemplate.html')
    else:
        return redirect('editTemplate1')


def editTemplate1(request):
    template = template1.objects.first()
    form = template1Form(instance=template)
    if request.method == "POST":
        form = template1Form(request.POST, instance=template)
        if form.is_valid():
            form.save()
            return redirect("selectTemplate")
    return render(request, "editTemplate1.html", {"template1Form": form})


def saveTemplate(request):
    if request.method == "POST":
        form = template1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request, "editTemplate1.html", {"template1Form": form})

