from django.urls import path 
from . import views

urlpatterns = [
    path( '' , views.index, name='index'),
    path('shop/' , views.shop, name='shop'),
    path('blog/' , views.blog, name='blog'),
    path('about us/', views.about_us, name='about us'),
    path('contact/', views.contact , name='contact'),
]