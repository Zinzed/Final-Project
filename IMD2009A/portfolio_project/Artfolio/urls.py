from django.urls import path, include
from .views import main
from . import views

urlpatterns = [
    path('', views.LandingPage, name='LandingPage'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('main', views.main, name='main'),
    path('selectTemplate', views.selectTemplate, name='selectTemplate'),
    path('newTemplate', views.newTemplate, name='newTemplate'),
    path('editTemplate/<int:templateId>', views.editTemplate, name='editTemplate'),
    path('explore', views.explore, name='explore'),
    path('exploreFiltered/<int:filterTagId>', views.exploreFiltered, name='exploreFiltered'),

]
