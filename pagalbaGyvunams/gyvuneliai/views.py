from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'gyvuneliai/home.html')


def posts(request):
    return render(request, 'gyvuneliai/posts.html')


def post(request):
    return render(request, 'gyvuneliai/post.html')
