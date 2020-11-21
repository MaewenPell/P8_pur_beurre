from store.models import Aliment, Category
from django.test import TestCase


class CategoryAlimentTest(TestCase):
    def setUp(self):
        Category.objects.create(category='Test cat')
        Aliment.objects.create(category=self._get_category('Test cat'),
                               name='AlimName', nutriscore='A',
                               image_url='None', product_url='None',
                               sugar='1g', fat='2g', salt='3g', energy='4g')
        self.aliment = Aliment.objects.get(name='AlimName')

    def _get_category(self, category):
        return Category.objects.get(category=category)

    def test_aliment_create(self):
        self.assertIsNotNone(self.aliment)

    def test_aliment_caract(self):
        self.assertEqual(self.aliment.name, 'AlimName')
        self.assertEqual(self.aliment.nutriscore, 'A')
        self.assertEqual(self.aliment.category, self._get_category('Test cat'))
