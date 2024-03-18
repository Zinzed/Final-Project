from django.urls import path, include
from .views import main
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('selectTemplate', views.selectTemplate, name='selectTemplate'),
    path('newTemplate', views.newTemplate, name='newTemplate'),
    path('editTemplate/<int:templateId>', views.editTemplate, name='editTemplate'),

]