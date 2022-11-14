from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def index(request):
    hero_posts = HeroSection.objects.all()
    banner_posts = BannerSection.objects.all()
    blog_posts = LatestBlog.objects.order_by('-date')[:3]
    if request.method == 'POST':
        form = AddMailingForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                EmailForMailing.objects.create(**form.cleaned_data)
                # form.save()
                return redirect('home')
            except:
                print('Ошибка')
    else:
        form = AddMailingForm()

    context = {
        'hero': hero_posts,
        'banner': banner_posts,
        'blog': blog_posts,
        'form': form
    }
    return render(request, 'ugc/index.html', context)


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
    blog_posts = LatestBlog.objects.order_by('-date')
    context = {
        'blog': blog_posts
    }
    return render(request, 'ugc/blog.html', context)


def blog_details(request):
    blog_posts = LatestBlog.objects.all()
    context = {
        'blog': blog_posts
    }
    return render(request, 'ugc/blog-details.html', context)


def post(request, pk):
    blog_post = LatestBlog.objects.get(id=pk)
    print(blog_post)
    context = {
        'blog_post': blog_post
    }
    return render(request, 'ugc/blog-details.html', context)


def contact(request):
    return render(request, 'ugc/contact.html')


def signin(request):
    return render(request, 'ugc/signin.html')


def signup(request):
    return render(request, 'ugc/signup.html')

