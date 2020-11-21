import requests
from store.services.parse_data_off import parse_categorie
from store.store_settings import NB_CATEGORIES, NB_RESULTS


def categories_requester():
    final_categories = []
    req = ('https://fr.openfoodfacts.org/categories.json')

    r = requests.get(req)
    r = r.json()

    for i, elem in enumerate(r['tags']):
        if i < NB_CATEGORIES:
            final_categories.append(elem['name'])

    return final_categories


def aliments_requester(categorie):
    """Request the OFF API to fetch product for a category

    Args:
        categorie (str): Type of aliment to fetch
        nb_results (int): number of aliments wanted

    Returns:
        list: list of dict corresponding of the fetched and parsed alims
    """
    req = (f'https://fr.openfoodfacts.org/categorie/{categorie}.json?\
           page_size={NB_RESULTS}')

    req = req.replace(" ", '')

    r = requests.get(req)
    r = r.json()

    aliments = parse_categorie(r)
    return aliments
