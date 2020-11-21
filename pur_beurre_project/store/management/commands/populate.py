from django.core.management.base import BaseCommand
from store.store_settings import NB_RESULTS
from store.services.get_data_off import aliments_requester, categories_requester
from store.services.populate_aliment_table import NewAliment
from store.services.populate_category_table import NewCategory
from store.models import Category
from django.db.utils import IntegrityError, DataError


class Command(BaseCommand):
    help = 'Populate the dabase with aliments and categories'

    def handle(self, *args, **kwargs):
        self.stdout.write('1 - Start filling Category table')

        cat = categories_requester()
        for current_cat in cat:
            try:
                NewCategory(current_cat).create_new_category()
                self.stdout.write(self.style.SUCCESS(f'\tCreated {current_cat}'))

                self.stdout.write(f'2 - Requesting {NB_RESULTS} aliments for {current_cat} table')
                alims_for_cat = aliments_requester(current_cat)
            except IntegrityError:
                self.stdout.write(self.style.ERROR(f'\tPassing creation of {cat}'))
                continue

            self.stdout.write('3 - Start filling table')
            for alim in alims_for_cat:
                try:
                    cat_to_fill = Category.objects.get(category=current_cat)
                    NewAliment(alim, cat_to_fill).create_aliment()
                except IntegrityError:
                    self.stdout.write(self.style.ERROR(f'\tPassing creation of {alim}'))
                    continue
                except DataError as e:
                    self.stdout.write(self.style.ERROR(f'\tPassing creation of {alim}'))
            self.stdout.write(self.style.SUCCESS('\tFinish filling'))
