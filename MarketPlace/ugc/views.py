from django.shortcuts import render
from .models import Task
# Create your views here.


def index(request):
    return render(request, 'ugc/index.html')


def about(request):
    return render(request, 'ugc/about.html')


def shop(request):
    return render(request, 'ugc/shop.html')


def shop_details(request):
    return render(request, 'ugc/shop-details.html')


def shopping_cart(request):
    return render(request, 'ugc/shopping-cart.html')


def checkout(request):
    return render(request, 'ugc/checkout.html')


def blog(request):
    return render(request, 'ugc/blog.html')


def blog_details(request):
    return render(request, 'ugc/blog-details.html')


def contact(request):
    return render(request, 'ugc/contact.html')


def signin(request):
    return render(request, 'ugc/signin.html')


