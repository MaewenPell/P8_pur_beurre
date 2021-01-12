def _pattern_alim():
    alim_pattern = {
        'name': None,
        'nutriscore': None,
        'image_url': None,
        'url': None,
        'fat': None,
        'sugars': None,
        'salt': None,
        'energy': None
    }
    return alim_pattern


def parse_categorie(data):
    """Parse a list of aliment to extract the informations

    Args:
        data (dict): dict of aliments

    Returns:
        list: Aliments with full data
    """
    aliments = data['products']
    all_alims_in_cat = []

    for fetched_alim in aliments:
        try:
            alim = _pattern_alim()
            # General informations
            alim['name'] = str(fetched_alim['product_name'])
            if alim['name'] == 'Chargement…':
                continue
            alim['nutriscore'] = str(fetched_alim['nutriscore_grade'])

            alim['image_url'] = str(fetched_alim['image_url'])
            alim['url'] = str(fetched_alim['url'])

            # Nutritionnals quantities
            nutriments = fetched_alim['nutriments']

            alim['fat'] = str(nutriments['fat'])
            alim['salt'] = str(nutriments['salt'])
            alim['energy'] = str(nutriments['energy'])
            alim['sugars'] = str(nutriments['sugars'])

            for results in alim.values():
                if results is None:
                    continue
            all_alims_in_cat.append(alim)

        except KeyError:
            continue

    return all_alims_in_cat
