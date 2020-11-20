from django.core.management.base import BaseCommand, CommandError
from store.store_settings import NB_RESULTS, CATEGORIES
from store.services.get_data_off import OFFRequester
from store.services.populate_aliment_table import NewAliment
from store.services.populate_category_table import NewCategory
from store.models import Category
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Populate the dabase with aliments and categories'

    def handle(self, *args, **kwargs):
        self.stdout.write('1 - Start filling Category table')
        for cat in CATEGORIES:
            try:
                NewCategory(cat).create_new_category()
                self.stdout.write(self.style.SUCCESS(f'\t Created {cat}'))
            except IntegrityError:
                self.stdout.write(self.style.ERROR(f'Passing creation of {cat} : already exist'))

            self.stdout.write(f'2 - Start fetching aliments informations for {cat}')
            current_cat = Category.objects.get(category=cat)
            alims_for_cat = OFFRequester(cat, NB_RESULTS)
            for alim in alims_for_cat[0]:
                NewAliment(alim, current_cat).create_aliment()

            self.stdout.write(self.style.SUCCESS(
                f'Fetching finished'))
