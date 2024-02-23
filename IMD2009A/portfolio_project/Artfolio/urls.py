from django.urls import path, include
from .views import main
from . import views

urlpatterns = [
    path('', main),
    path('selectTemplate', views.selectTemplate, name='selectTemplate'),
    path('editTemplate1', views.editTemplate1, name='editTemplate1'),
    path('saveTemplate', views.saveTemplate, name='saveTemplate'),
]