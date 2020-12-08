from store.models import Aliment, Category
from django.test import TestCase


class TestAlimentsCategories(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category="Test Category")
        test_cat = Category.objects.get(category="Test Category")
        Aliment.objects.create(category=test_cat, name="Test alim",
                               nutriscore="X", image_url="https://image_url.org",
                               product_url="https://product_url.org", sugar="X",
                               fat="Y", salt="Z", energy="ABC")

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

    def test_str_alim_name_equals(self):
        self.assertEqual(self.test_alim.__str__(), self.test_alim.name)
