import numpy as np
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from store.forms.forms import SignUpForm
from store.models import Aliment, Favorite
from store.services.db_lookup import find_best_match, find_better_alims
from django.contrib import messages

from django.http import HttpResponseRedirect


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
    try:
        alim_id = request.POST.get('add_alim')
        alim = Aliment.objects.get(pk=alim_id)
        current_user = User.objects.get(email=request.user.email)

        if not Favorite.objects.filter(user=current_user, aliment=alim).exists():
            Favorite.objects.create(user=current_user, aliment=alim)
            messages.success(request, 'Aliment ajouté aux favoris')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Aliment déjà présent dans vos favoris')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except AttributeError:
        messages.error(request, "Cet aliment n'est pas présent dans notre base de donnée")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_alim(request):
    try:
        c = request.POST.get('remove_alim')
        alim_id = c
        alim = Aliment.objects.get(pk=alim_id)
        current_user = User.objects.get(email=request.user.email)

        to_del = Favorite.objects.get(user=current_user, aliment=alim)
        to_del.delete()

        current_user = User.objects.get(email=request.user.email)
        Favorite.objects.filter(user=current_user)

        messages.success(request, 'Aliment retiré des favoris')
        return redirect('my_aliments')
    except Aliment.DoesNotExist:
        # If someone want to remove an aliment without the correct
        # methods
        messages.error(request, "Cet aliment n'est pas présent dans notre base de donnée")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def result(request):
    query = request.GET.get('search_alim')
    try:
        best_match = find_best_match(query)
        better_alims = find_better_alims(Aliment.objects.get(name=best_match['name']))
    except Aliment.DoesNotExist:
        print("passed")
        messages.error(request, "Cet aliment n'est pas présent dans notre base de donnée")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
                'alim': better_alims,
                'query_alim': best_match['product'],
            }
    return render(request, 'store/result.html', context)


def user(request):
    if request.user.is_authenticated:
        return render(request, 'store/user.html')
    else:
        return redirect("accounts/login")


def my_aliments(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(email=request.user.email)
        fav_alim_user = Favorite.objects.filter(user=current_user)

        paginator = Paginator(fav_alim_user, 6)

        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)

        context = {
            "alims": fav_alim_user,
            "len": len(fav_alim_user),
            "page_obj": page_object
        }

        return render(request, 'store/my_aliments.html', context)
    else:
        return redirect("accounts/login")


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
