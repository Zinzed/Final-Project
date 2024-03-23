from django.contrib import admin
from . import models

# Register your models here.
from .models import template
admin.site.register(template)
admin.site.register(models.filterTag, admin.ModelAdmin)
