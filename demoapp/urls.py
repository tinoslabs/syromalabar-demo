from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administration',views.administration, name='administration'),
    path('contact',views.contact, name='contact'),
    path('mass',views.mass, name='mass'),
    path('blog',views.blog, name='blog'),
    path('event',views.event, name='event'),
    path('gallery',views.gallery, name='gallery'),
    
    # Add more patterns here
]
