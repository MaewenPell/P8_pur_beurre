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
                               fat="12", salt="1.39", energy="1832",
                               average=1)
        Aliment.objects.create(category=test_cat, name="bon petit biscuit",
                               nutriscore="A",
                               image_url="https://test2.jpg",
                               product_url="https://test2.fr",
                               sugar="23",
                               fat="12", salt="1.39", energy="1832",
                               average=2)
        Aliment.objects.create(category=test_cat, name="mauvais gros gateau",
                               nutriscore="A",
                               image_url="https://test3.jpg",
                               product_url="https://test3.fr",
                               sugar="23",
                               fat="12", salt="1.39", energy="1832",
                               average=3)
        Aliment.objects.create(category=test_cat, name="mauvais gateaux 2",
                               nutriscore="A",
                               image_url="https://f.jpg",
                               product_url="https://e.fr",
                               sugar="23",
                               fat="12", salt="1.39", energy="1832",
                               average=4)

        Aliment.objects.create(category=test_cat_fruits, name="fruit",
                               nutriscore="A",
                               image_url="https://test4.jpg",
                               product_url="https://test4.fr",
                               sugar="1",
                               fat="2", salt="1", energy="18",
                               average=4)
        Aliment.objects.create(category=test_cat_fruits, name="fruit3",
                               nutriscore="A",
                               image_url="https://fdsf.jpg",
                               product_url="https://errezr.fr",
                               sugar="1",
                               fat="2", salt="1", energy="18",
                               average=5)

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
        better_alim = db_lookup.find_better_alims(self.test_alim, None)
        self.assertTrue(self.test_alim.nutriscore > better_alim[0].nutriscore)

    def test_better_alim_is_same_category_than_base(self):
        base_alim = self.test_alim
        better_alim = db_lookup.find_better_alims(base_alim, None)
        self.assertEqual(base_alim.category, better_alim[0].category)

    def test_favorite(self):
        alim_id = self.test_alim.pk
        db_lookup.add_aliment_in_favorite(alim_id, self.test_user)
        fav = Favorite.objects.filter(user=self.test_user)
        self.assertEqual(len(fav), 1)
        self.assertEqual(fav[0].aliment.name, "petit beurre")

    def test_average(self):
        alim = db_lookup.manage_user_notation(self.test_alim.name, 5)
        alim = db_lookup.manage_user_notation(self.test_alim.name, 2)

        self.assertEqual(alim.count, 2)
        self.assertEqual(alim.average, 3.5)

    def test_aliments_are_sorted(self):
        a = Aliment.objects.get(name='petit beurre')
        better_alims = db_lookup.find_better_alims(a, to_sort="Checked")
        self.assertTrue(better_alims[0].average
                        > better_alims[1].average
                        > better_alims[2].average)
