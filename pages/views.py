from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render( request , 'pages/index.html' )

def shop(request):
    return render( request , 'pages/shop.html' )

def blog(request):
    return render( request , 'pages/blog.html' )

def about_us(request):
    return render( request , 'pages/about us.html')

def contact(request):
    return render(request , 'pages/contact.html' )