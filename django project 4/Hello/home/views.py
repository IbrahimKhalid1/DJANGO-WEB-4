# from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is my Home")

def about(request):
    return render(request,'about.html')

def shop(request):
    return render(request,'shop.html')

def blog(request):
    return render(request, 'blog.html')
