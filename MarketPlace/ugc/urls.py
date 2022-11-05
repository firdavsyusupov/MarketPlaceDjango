from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('shop', views.shop, name='shop'),
    path('shop-details', views.shop_details, name='shop-details'),
    path('shopping-cart', views.shopping_cart, name='shopping-cart'),
    path('checkout', views.checkout, name='checkout'),
    path('blog', views.blog, name='blog'),
    path('blog-details', views.blog_details, name='blog-details'),
    path('contact', views.contact, name='contact'),
    path('signin', views.signin, name='signin'),
]
