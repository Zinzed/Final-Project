from django.urls import path, include
from .views import main
from . import views

urlpatterns = [
    path('', main),
    path('selectTemplate', views.selectTemplate, name='selectTemplate'),
    path('newTemplate', views.newTemplate, name='newTemplate'),
    path('editTemplate/<int:templateId>', views.editTemplate, name='editTemplate'),
    path('saveTemplate', views.saveTemplate, name='saveTemplate'),
]