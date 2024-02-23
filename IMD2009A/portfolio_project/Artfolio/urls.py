from django.urls import path, include
from .views import main
from . import views

urlpatterns = [
    path('', main),
    path('selectTemplate', views.selectTemplate, name='selectTemplate'),
    path('editTemplate', views.editTemplate, name='editTemplate'),
    path('saveTemplate', views.saveTemplate, name='saveTemplate'),
]