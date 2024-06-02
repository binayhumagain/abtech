from django.contrib import admin

# Register your models here.
from .models import Task, Teams

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'completed']

@admin.register(Teams)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']