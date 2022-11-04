from django.shortcuts import render
from .models import Task
# Create your views here.


def index(request):
    return render(request, 'ugc/index.html')


def about(request):
    return render(request, 'ugc/test/about.html')
