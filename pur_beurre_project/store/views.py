from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'store/index.html')


def detail(request):
    return render(request, 'store/detail.html')


def result(request):
    return render(request, 'store/result.html')


def user(request):
    return render(request, 'store/user.html')


def my_aliments(request):
    return render(request, 'store/my_aliments.html')


def legal(request):
    return render(request, 'store/legal.html')


def contact(request):
    return render(request, 'store/contact.html')
