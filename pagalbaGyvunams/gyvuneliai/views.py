from django.shortcuts import render
from .models import Animal

# Create your views here.


def home(request):

    # animals = Animal.objects.all()
    animals = Animal.objects.filter(active=True)

    context = {'animals' : animals}
    return render(request, 'gyvuneliai/home.html', context)


def posts(request):
    return render(request, 'gyvuneliai/posts.html')


def post(request):
    return render(request, 'gyvuneliai/post.html')
