from django.test import TestCase

from store.models import Aliment, Category, User, Favorite
import store.services.db_lookup as db_lookup


class ServicesUnitsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category="Biscuits et gâteaux")
        Category.objects.create(category="Fruits")

        test_cat = Category.objects.get(category="Biscuits et gâteaux")
        test_cat_fruits = Category.objects.get(category="Fruits")
        Aliment.objects.create(category=test_cat, name="petit beurre",
                               nutriscore="D",
                               image_url="https://test1.jpg",
                               product_url="https://test1.fr",
                               sugar="23",
                               fat="12", salt="1.39", energy="1832")
        Aliment.objects.create(category=test_cat, name="bon petit biscuit",
                               nutriscore="A",
                               image_url="https://test2.jpg",
                               product_url="https://test2.fr",
                               sugar="23",
                               fat="12", salt="1.39", energy="1832")
        Aliment.objects.create(category=test_cat, name="mauvais gros gateau",
                               nutriscore="E",
                               image_url="https://test3.jpg",
                               product_url="https://test3.fr",
                               sugar="23",
                               fat="12", salt="1.39", energy="1832")
        Aliment.objects.create(category=test_cat_fruits, name="fruit",
                               nutriscore="A",
                               image_url="https://test4.jpg",
                               product_url="https://test4.fr",
                               sugar="1",
                               fat="2", salt="1", energy="18")
        User.objects.create(email="test_user@test.com")

        cls.test_cat = Category.objects.get(category="Biscuits et gâteaux")
        cls.test_alim = Aliment.objects.get(name="petit beurre")
        cls.test_alim_E = Aliment.objects.get(name="mauvais gros gateau")
        cls.test_alim_A = Aliment.objects.get(name="bon petit biscuit")
        cls.test_user = User.objects.get(email="test_user@test.com")

    def test_find_best_match_return_correct_alim(self):
        best_match = db_lookup.find_best_match("petit beurre")
        self.assertEqual(best_match['product'], self.test_alim)

    def test_find_better_alim_than_base(self):
        base_alim = self.test_alim
        better_alim = db_lookup.find_better_alims(base_alim)
        self.assertTrue(base_alim.nutriscore > better_alim[0].nutriscore)

    def test_better_alim_is_same_category_than_base(self):
        base_alim = self.test_alim
        better_alim = db_lookup.find_better_alims(base_alim)
        self.assertEqual(base_alim.category, better_alim[0].category)

    def test_favorite(self):
        alim_id = self.test_alim.pk
        db_lookup.add_aliment_in_favorite(alim_id, self.test_user)
        fav = Favorite.objects.filter(user=self.test_user)
        self.assertEqual(len(fav), 1)
        self.assertEqual(fav[0].aliment.name, "petit beurre")