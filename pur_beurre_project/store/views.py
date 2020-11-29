from django.shortcuts import render, redirect, HttpResponse
from store.models import Aliment
from django.contrib.auth import login, authenticate
from store.forms.forms import SignUpForm
from store.services.db_lookup import find_best_match, find_better_alims
import numpy as np
from django.contrib.auth.models import User


def index(request):
    return render(request, 'store/index.html')


def detail(request, alim_id):
    alim = Aliment.objects.get(pk=alim_id)

    context = {'alim': alim,
               'nutrim': {
                   'fat': np.round(float(alim.fat), 2),
                   'salt': np.round(float(alim.salt), 2),
                   'sugar': np.round(float(alim.sugar), 2),
                   'energy': np.round(float(alim.energy), 2)
                },
               }

    return render(request, 'store/detail.html', context)


def add_alim(request):
    context = request.POST.get('add_alim')
    context = context.split("#")
    alim_id = context[0]
    user_email = context[1]
    alim = Aliment.objects.get(pk=alim_id)
    current_user = User.objects.get(email=user_email)

    current_user.my_aliments.add(alim)

    return HttpResponse(200)


def result(request):
    query = request.GET.get('search_alim')

    best_match = find_best_match(query)
    better_alims = find_better_alims(Aliment.objects.get(name=best_match['name']))

    context = {
                'alim': better_alims,
                'query_alim': best_match['product']
                }

    return render(request, 'store/result.html', context)


def user(request):
    return render(request, 'store/user.html')


def my_aliments(request):
    return render(request, 'store/my_aliments.html')


def legal(request):
    return render(request, 'store/legal.html')


def contact(request):
    return render(request, 'store/contact.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
    else:
        form = SignUpForm()

    context = {
        "form": form,
    }
    return render(request, 'registration/register.html', context=context)
