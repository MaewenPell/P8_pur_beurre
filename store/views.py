from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
import store.services.db_lookup as db_lookup
from store.forms.forms import SignUpForm
from store.models import User


def index(request):
    return render(request, 'store/index.html')


def detail(request, alim_id):
    return render(request, 'store/detail.html', db_lookup.get_alim(alim_id))


def add_alim(request):
    if request.user.is_authenticated:
        alim_id = request.POST.get('add_alim')
        current_user = User.objects.get(email=request.user.email)
        message = db_lookup.add_aliment_in_favorite(alim_id, current_user)
    else:
        return redirect("accounts/login")

    if message == "success":
        messages.success(request, 'Aliment ajouté aux favoris')
    elif message == "present":
        messages.error(request, 'Aliment déjà présent dans vos favoris')
    else:
        messages.error(
            request, "Cet aliment n'est pas présent dans notre base de donnée")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_alim(request):
    if request.user.is_authenticated:
        alim_id = request.POST.get('remove_alim')
        user = User.objects.get(email=request.user.email)
        status = db_lookup.remove_alim_from_favorite(alim_id, user)
        if status == "success":
            messages.success(request, 'Aliment retiré des favoris')
        else:
            messages.error(
                request,
                "Cet aliment n'est pas présent dans notre base de donnée")
        return redirect('my_aliments')
    else:
        return redirect("accounts/login")


def notation(request):
    alim_information = request.POST['notation_drop'].split("|")
    try:
        alim_notation = int(alim_information[0])
        alim_name = alim_information[1].strip()
        db_lookup.manage_user_notation(alim_name, alim_notation)
        messages.success(request, "Note ajoutée")
    except ValueError:
        messages.error(request, "Veuillez choisir une note")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def result(request):
    context, error = db_lookup.get_results_from_research(request)
    if error:
        messages.error(request,
                       "Cet aliment n'est pas présent dans notre base de donnée \
            affichons le nôtre à la place !")
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
