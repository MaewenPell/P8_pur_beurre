import requests
from store.services.parse_data_off import parse_categorie


def OFFRequester(categorie, nb_results):
    """Request the OFF API to fetch product for a category

    Args:
        categorie (str): Type of aliment to fetch
        nb_results (int): number of aliments wanted

    Returns:
        list: list of dict corresponding of the fetched and parsed alims
    """
    aliments_all = []
    req = (f'https://fr.openfoodfacts.org/categorie/{categorie}.json?\
           page_size={nb_results}')

    req = req.replace(" ", '')

    r = requests.get(req)
    r = r.json()

    aliment = parse_categorie(r)
    aliments_all.append(aliment)
    return aliments_all
