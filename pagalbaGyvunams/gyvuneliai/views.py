from django.shortcuts import render
from .models import Animal, Tag
from django.db import connection

# Create your views here.


def home(request):

    # animals = Animal.objects.all()
    animals = Animal.objects.filter(active=True)[:4]

    print(animals)
    print(connection.queries)

    context = {'animals' : animals}
    return render(request, 'gyvuneliai/home.html', context)

# testing RAW queries
# Django ORM - Performing raw SQL queries
# https://docs.djangoproject.com/en/4.1/topics/db/queries/
# def home(request):

#     sql = "SELECT * FROM gyvuneliai_Animal WHERE age = 2 ORDER BY RAND()"
#     # sql = "SELECT * FROM gyvuneliai_Animal WHERE age = 2 ORDER BY RAND() LIMIT 3"
#     # sql = "SELECT * FROM gyvuneliai_Animal WHERE age = 2"
#     animals = Animal.objects.raw(sql)[:4]

#     print(animals)
#     print(connection.queries)

#     context = {'animals' : animals}
#     return render(request, 'gyvuneliai/home.html', context)


def sunys(request):
    sunys = Animal.objects.filter(tags__name="Suo")

    print(sunys)                # little help to make sure the querry is correct

    context = {'sunys' : sunys}  # how you define it here, will later be used in template
    return render(request, 'gyvuneliai/sunys.html', context)


def suo(request, pk):
    suo = Animal.objects.get(id=pk)

    context = {'suo' : suo}
    return render(request, 'gyvuneliai/suo.html', context)


def kates(request):
    kates = Animal.objects.filter(tags__name="Kate")

    print(kates)                # little help to make sure the querry is correct

    context = {'kates' : kates}  # how you define it here, will later be used in template
    return render(request, 'gyvuneliai/kates.html', context)


def kate(request, pk):
    kate = Animal.objects.get(id=pk)

    context = {'kate' : kate}
    return render(request, 'gyvuneliai/kate.html', context)


def kontaktai(request):
    return render(request, 'gyvuneliai/kontaktai.html')


def apie(request):
    return render(request, 'gyvuneliai/apie_mus.html')


def savanoryste(request):
    return render(request, 'gyvuneliai/savanoryste.html')


def statistika(request):
    return render(request, 'gyvuneliai/statistika.html')


def parama(request):
    return render(request, 'gyvuneliai/parama.html')
