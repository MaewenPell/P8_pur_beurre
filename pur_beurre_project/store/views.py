from django.shortcuts import render, redirect
from store.models import Aliment
from django.db.models import Q
from difflib import SequenceMatcher
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate
from store.forms.forms import SignUpForm
import numpy as np


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


def result(request):
    query = request.GET.get('search_alim')
    best_match = {
                  'name': 'name',
                  'similarity': 0
                 }
    if Aliment.objects.filter(name__icontains=query).exists():
        query_alim = Aliment.objects.filter(name__icontains=query)
        for alim in query_alim:
            similarity = SequenceMatcher(None, alim.name, best_match['name']).ratio()
            if similarity > best_match['similarity']:
                best_match['similarity'] = similarity
                best_match['name'] = alim.name

        alim = Aliment.objects.get(name=best_match['name'])

        db_query = Q(nutriscore__lte=alim.nutriscore)
        db_query.add(Q(category=alim.category), Q.AND)

        better_alim = Aliment.objects.filter(db_query).order_by("nutriscore")[0:6]

        context = {
                    'alim': better_alim,
                    'query_alim': alim
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
