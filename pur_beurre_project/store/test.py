from store.actions.populate_aliment_table import NewAliment
from store.actions.populate_category_table import NewCategory
from store.models import Aliment, Category
from django.test import TestCase


coca_cola = {
    'product': {
        'product_name': 'Coca Cola',
        'nutriscore_grade': 'E',
        'image_url': 'https://www.getgreenbewell.com/wp-content/\
            uploads/2020/05/Coca-Cola-Bottle-and-Can.jpg',
        'url': 'https://world.openfoodfacts.org/product\
            /5449000000996/coca-cola',
        'nutriments': {
            'fat': '100g',
            'sugar': '989g',
            'salt': '0g',
            'energy': '999Kcal'
        }
    }
}


class TestFillingDbAlimCat(TestCase):
    def setUp(self):
        cat_boisson = NewCategory('Boissons')
        cat_boisson = cat_boisson.create_new_category()
        # cat_boisson_2 = NewCategory('Nutella')
        # cat_boisson_2 = cat_boisson_2.create_new_category()
        self.cat = Category.objects.all()

        # alim_coca_cola = NewAliment(coca_cola, self.cat[0])
        # alim_coca_cola.create_aliment()
        #   self.new_alim = Aliment.objects.get(name='Coca Cola')

        print(type(self.cat[0]))

    def test_category(self):
        self.assertEqual(self.cat.category, 'Boissons')

    def test_alim_name(self):
        self.assertEqual(self.new_alim.name, 'Coca Cola')
        self.assertEqual(self.new_alim.fat, '100g')
