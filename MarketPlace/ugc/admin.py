from django.contrib import admin
from .models import *
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'task')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'task')


class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'content')
    search_fields = ('id', 'title', 'name')


class BannerSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_title', 'second_title', 'third_title')
    search_fields = ('id', 'first_title', 'second_title', 'third_title')


class LatestBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    search_fields = ('id', 'title', 'date')


class EmailForMailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('id', 'email')


admin.site.register(Task, TaskAdmin)
admin.site.register(HeroSection, HeroSectionAdmin)
admin.site.register(BannerSection, BannerSectionAdmin)
admin.site.register(LatestBlog, LatestBlogAdmin)
admin.site.register(EmailForMailing, EmailForMailingAdmin)
