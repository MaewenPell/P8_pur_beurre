from store.models import Aliment, Favorite, User
from django.db.models import Q
from difflib import SequenceMatcher
from django.core.paginator import Paginator
import numpy as np


def find_best_match(query: str):
    best_match = {
                  'temp_name': 'temp_name',
                  'name': 'name',
                  'similarity': 0
                 }
    if Aliment.objects.filter(name__icontains=query).exists():
        query_alim = Aliment.objects.filter(name__icontains=query)
        for alim in query_alim:
            temp_name = alim.name.replace(' ', '')
            similarity = SequenceMatcher(None, temp_name,
                                         best_match['temp_name']).ratio()
            if similarity > best_match['similarity']:
                best_match['temp_name'] = temp_name
                best_match['similarity'] = similarity
                best_match['name'] = alim.name
                best_match['product'] = alim

    return best_match


def find_better_alims(alim: Aliment, to_sort: str):
    db_query = Q(nutriscore__lt=alim.nutriscore)
    db_query.add(Q(category=alim.category), Q.AND)

    if to_sort != "Checked":
        better_alim = Aliment.objects.filter(
            db_query).order_by("nutriscore")[0:6]
    else:
        better_alim = Aliment.objects.filter(
            db_query).order_by("-average")[0:6]

    return better_alim


def add_aliment_in_favorite(alim_id, current_user):
    try:
        alim = Aliment.objects.get(pk=alim_id)

        if not Favorite.objects.filter(user=current_user,
                                       aliment=alim).exists():
            Favorite.objects.create(user=current_user, aliment=alim)
            return "success"
        else:
            return "present"
    except AttributeError:
        return "unknown"


def get_alim(alim_id: int):
    alim = Aliment.objects.get(pk=alim_id)

    context = {'alim': alim,
               'nutrim': {
                   'fat': np.round(float(alim.fat), 2),
                   'salt': np.round(float(alim.salt), 2),
                   'sugar': np.round(float(alim.sugar), 2),
                   'energy': np.round(float(alim.energy), 2)
                },
               }
    return context


def remove_alim_from_favorite(alim_id, user):
    try:
        alim = Aliment.objects.get(pk=alim_id)
        entry_to_del = Favorite.objects.get(user=user, aliment=alim)
        entry_to_del.delete()
        return "success"

    except Aliment.DoesNotExist:
        return "unkown"


def get_results_from_research(request):
    query = request.GET.get('search_alim')
    to_sort = request.GET.get('checkbox')
    try:
        best_match = find_best_match(query)
        better_alims = find_better_alims(
            Aliment.objects.get(name=best_match['name']), to_sort=to_sort)
        error = False
    except Aliment.DoesNotExist:
        better_alims, best_match = return_default_value()
        error = True

    context = {
        'alim': better_alims,
        'query_alim': best_match['product']
    }
    return context, error


def return_default_value():
    query = "petit beurre"
    best_match = find_best_match(query)
    better_alims = find_better_alims(Aliment.objects.get(
        name=best_match['name']))
    return better_alims, best_match


def get_user_favorite_alims(request):
    fav_alim_user = Favorite.objects.filter(
        user=User.objects.get(email=request.user.email))

    paginator = Paginator(fav_alim_user, 6)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        "alims": fav_alim_user,
        "len": len(fav_alim_user),
        "page_obj": page_object
    }
    return context


def manage_user_notation(alim_name, alim_notation):
    alim = Aliment.objects.get(name=alim_name)
    if alim_notation in range(1, 6):
        alim.count += 1
        if alim.notation is not None:
            alim.notation += alim_notation
        else:
            alim.notation = alim_notation
    alim.average = np.round(alim.notation / alim.count, 2)
    alim.save()
    return alim
