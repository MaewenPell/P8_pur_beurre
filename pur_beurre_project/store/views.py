from django.shortcuts import render, redirect, HttpResponse
from store.models import Aliment, Favorite
from django.contrib.auth import login, authenticate
from store.forms.forms import SignUpForm
from store.services.db_lookup import find_best_match, find_better_alims
import numpy as np
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


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
    c = request.POST.get('add_alim').split("#")
    alim_id = c[0]
    user_email = c[1]
    alim = Aliment.objects.get(pk=alim_id)
    current_user = User.objects.get(email=user_email)

    try:
        new_fav = Favorite.objects.create(user=current_user, aliment=alim)
    except IntegrityError:
        pass

    current_user = User.objects.get(email=request.user.email)
    fav_alim_user = Favorite.objects.filter(user=current_user)

    context = {
        "alims" : fav_alim_user
    }
    return render(request, 'store/my_aliments.html', context=context)

def remove_alim(request):
    c = request.POST.get('remove_alim')
    alim_id = c
    alim = Aliment.objects.get(pk=alim_id)
    current_user = User.objects.get(email=request.user.email)
    
    to_del = Favorite.objects.get(user=current_user, aliment=alim)
    to_del.delete()

    current_user = User.objects.get(email=request.user.email)
    fav_alim_user = Favorite.objects.filter(user=current_user)

    context = {
        "alims" : fav_alim_user
    }
    return render(request, 'store/my_aliments.html', context=context)


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
    current_user = User.objects.get(email=request.user.email)
    fav_alim_user = Favorite.objects.filter(user=current_user)

    context = {
        "alims" : fav_alim_user
    }
    return render(request, 'store/my_aliments.html', context)


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
