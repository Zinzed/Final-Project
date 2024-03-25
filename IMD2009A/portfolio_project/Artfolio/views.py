import logging

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import template, filterTag
from .forms import templateForm, userForm, loginForm
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def main(request):
    myTemplate = template.objects.first()
    if myTemplate is None:
        return render(request, 'firstMain.html')
    else:
        return render(request, 'main.html', {'myTemplate': myTemplate})


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
        form = templateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'main.html', {'templateForm': form, 'imgObj': form.instance})
        else:
            form = templateForm()
    return render(request, 'newTemplate.html', {'templateForm': form})

def editTemplate(request, templateId):
    myTemplate = template.objects.get(pk=templateId)
    form = templateForm(instance=myTemplate)

    if request.method == "POST":
        form = templateForm(request.POST, request.FILES, instance=myTemplate)

        if form.is_valid():
            form.save()
            return redirect('main')

    return render(request, 'editTemplate.html', {'templateForm': form})


def register(request):

    form = userForm()
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect("login")

    context = {'registerForm': form}

    return render(request, 'register.html', context=context)
  
  
def login(request):

    form = loginForm()
    if request.method == "POST":
        form = loginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)
                myTemplate = template.objects.filter(user=user)
                if myTemplate is None:
                    return render(request, 'firstMain.html')
                else:
                    return render(request, 'main.html', {'myTemplate': myTemplate})

    context = {'loginForm':form}

    return render(request, 'login.html', context)
  

def LandingPage(request):
    return render(request, 'LandingPage.html')


def explore(request):
    filterTags = filterTag.objects.all
    portfolios = template.objects.all
    return render(request, 'explore.html', {'portfolios': portfolios, 'filterTags': filterTags})


def exploreFiltered(request, filterTagId):
    filterTags = filterTag.objects.all
    portfolios = template.objects.filter(filterTags=filterTagId)
    return render(request, 'explore.html', {'portfolios': portfolios, 'filterTags': filterTags, 'filterTagId': filterTagId})
