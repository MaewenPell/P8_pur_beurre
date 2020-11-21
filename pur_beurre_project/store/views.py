from django.shortcuts import render
from store.models import Aliment


def index(request):
    return render(request, 'store/index.html')


def detail(request, alim_id):
    alim = Aliment.objects.filter(pk=alim_id)

    context = {'alim': alim}

    return render(request, 'store/detail.html', context)


def result(request):
    alim = Aliment.objects.filter(name__icontains='lait').order_by('nutriscore')[0:3]

    context = {'alim': alim}

    return render(request, 'store/result.html', context)


def user(request):
    return render(request, 'store/user.html')


def my_aliments(request):
    return render(request, 'store/my_aliments.html')


def legal(request):
    return render(request, 'store/legal.html')


def contact(request):
    return render(request, 'store/contact.html')
