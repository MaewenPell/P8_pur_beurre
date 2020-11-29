from store.models import Aliment
from django.db.models import Q
from difflib import SequenceMatcher


def find_best_match(query: str):
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
                best_match['product'] = alim

    return best_match


def find_better_alims(alim: Aliment):
    db_query = Q(nutriscore__lte=alim.nutriscore)
    db_query.add(Q(category=alim.category), Q.AND)

    better_alim = Aliment.objects.filter(db_query).order_by("nutriscore")[0:6]

    return better_alim
