from django.urls import path, include
from .views import main
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('selectTemplate', views.selectTemplate, name='selectTemplate'),
    path('newTemplate', views.newTemplate, name='newTemplate'),
    path('editTemplate/<int:templateId>', views.editTemplate, name='editTemplate'),
    path('explore', views.explore, name='explore'),
]