from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

import store.services.db_lookup as db_lookup
from store.forms.forms import SignUpForm


def index(request):
    return render(request, 'store/index.html')


def detail(request, alim_id):
    return render(request, 'store/detail.html', db_lookup.get_alim(alim_id))


def add_alim(request):
    message = db_lookup.add_aliment_in_favorite(request)

    if message == "success":
        messages.success(request, 'Aliment ajouté aux favoris')
    elif message == "present":
        messages.error(request, 'Aliment déjà présent dans vos favoris')
    else:
        messages.error(request, "Cet aliment n'est pas présent dans notre base de donnée")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_alim(request):
    status = db_lookup.remove_alim_from_favorite(request)
    if status == "success":
        messages.success(request, 'Aliment retiré des favoris')
    else:
        messages.error(request, "Cet aliment n'est pas présent dans notre base de donnée")
    return redirect('my_aliments')


def result(request):
    context = db_lookup.get_results_from_research(request)
    if context == "unkown":
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'store/result.html', context)


def user(request):
    if request.user.is_authenticated:
        return render(request, 'store/user.html')
    else:
        return redirect("accounts/login")


def my_aliments(request):
    if request.user.is_authenticated:
        context = db_lookup.get_user_favorite_alims(request)
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
