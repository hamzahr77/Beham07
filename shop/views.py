from django.shortcuts import render
from django.http import HttpResponse
from .models import Allproduct
# Create your views here.

def shop(request):
    context = {
        'shop':Allproduct.objects.all()
    }
    return render(request , 'shop/shop.html', context )