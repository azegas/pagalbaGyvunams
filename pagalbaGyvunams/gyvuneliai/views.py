from django.shortcuts import render
from .models import Animal

# Create your views here.


def home(request):

    # animals = Animal.objects.all()
    animals = Animal.objects.filter(active=True)

    context = {'animals' : animals}
    return render(request, 'gyvuneliai/home.html', context)


def sunys(request):
    return render(request, 'gyvuneliai/sunys.html')


def suo(request, pk):
    suo = Animal.objects.get(id=pk)

    context = {'suo' : suo}
    return render(request, 'gyvuneliai/suo.html', context)


def kates(request):
    return render(request, 'gyvuneliai/kates.html')


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
