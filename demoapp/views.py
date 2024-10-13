from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request,'index.html')

def administration(request):
    return render(request,'administration.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def mass(request):
    return render(request,'masses.html')

def event(request):
    return render(request,'events.html')

def gallery(request):
    return render(request,'gallery.html')

def administration(request):
    return render(request,'administration.html')
