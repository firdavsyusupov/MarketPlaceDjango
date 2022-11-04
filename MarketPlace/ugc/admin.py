from django.contrib import admin
from .models import *
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'task')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'task')


admin.site.register(Task, TaskAdmin)
