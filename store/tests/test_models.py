from store.models import Aliment, Category, User, Favorite
from django.test import TestCase


class TestAlimentsCategories(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category="Test Category")
        test_cat = Category.objects.get(category="Test Category")
        Aliment.objects.create(category=test_cat, name="Test alim",
                               nutriscore="X",
                               image_url="https://image_url.org",
                               product_url="https://product_url.org",
                               sugar="X",
                               fat="Y", salt="Z", energy="ABC",
                               notation=10, count=2, average=5)

    def setUp(self):
        self.test_cat = Category.objects.get(category="Test Category")
        self.test_alim = Aliment.objects.get(name="Test alim")

    def test_cat_equals(self):
        self.assertEqual(self.test_cat.category, "Test Category")

    def test_str_cat_equals(self):
        self.assertEqual(self.test_cat.__str__(), self.test_cat.category)

    def test_alim_cat_equals(self):
        self.assertEqual(self.test_alim.category, self.test_cat)

    def test_alim_name_equals(self):
        self.assertEqual(self.test_alim.name, "Test alim")

    def test_alim_nutriscore_equals(self):
        self.assertEqual(self.test_alim.nutriscore, "X")

    def test_alim_img_url_equals(self):
        self.assertEqual(self.test_alim.image_url, "https://image_url.org")

    def test_alim_product_url_equals(self):
        self.assertEqual(self.test_alim.product_url, "https://product_url.org")

    def test_alim_sugar_equals(self):
        self.assertEqual(self.test_alim.sugar, "X")

    def test_alim_fat_equals(self):
        self.assertEqual(self.test_alim.fat, "Y")

    def test_alim_salt_equals(self):
        self.assertEqual(self.test_alim.salt, "Z")

    def test_alim_energy_equals(self):
        self.assertEqual(self.test_alim.energy, "ABC")

    def test_alim_notation_equals(self):
        self.assertEqual(self.test_alim.count, 2)
        self.assertEqual(self.test_alim.notation, 10)
        self.assertEqual(self.test_alim.average, 5)

    def test_str_alim_name_equals(self):
        self.assertEqual(self.test_alim.__str__(), self.test_alim.name)


class TestFavoriteCategory(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category="Biscuits et gâteaux")
        test_cat = Category.objects.get(category="Biscuits et gâteaux")
        Aliment.objects.create(category=test_cat, name="petit beurre",
                               nutriscore="D",
                               image_url="https://test1.jpg",
                               product_url="https://test1.fr",
                               sugar="23",
                               fat="12", salt="1.39", energy="1832")
        User.objects.create(email="test_user@test.com")

    def setUp(self):
        self.test_alim = Aliment.objects.get(name="petit beurre")
        self.test_user = User.objects.get(email="test_user@test.com")
        Favorite.objects.create(user=self.test_user, aliment=self.test_alim)

    def test_user_created(self):
        self.assertEqual(self.test_user.email, "test_user@test.com")

    def test_favorite_created(self):
        fav = Favorite.objects.get(user=self.test_user, aliment=self.test_alim)
        self.assertEqual(fav.aliment.name, "petit beurre")
