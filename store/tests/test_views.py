from django.test import TestCase
from store.models import Aliment, Category


class ViewsResponseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category="Biscuits et gâteaux")
        test_cat = Category.objects.get(category="Biscuits et gâteaux")
        Aliment.objects.create(category=test_cat, name="petit beurre",
                               nutriscore="X",
                               image_url="http://images/products/53.400.jpg",
                               product_url="https://produit/7622210476104/lu",
                               sugar="23",
                               fat="12", salt="1.39", energy="1832")

    def setUp(self):
        self.test_cat = Category.objects.get(category="Biscuits et gâteaux")
        self.test_alim = Aliment.objects.get(name="petit beurre")

    def test_default_url_exists_at_desired_location(self):
        self.assertEqual(self.client.get('').status_code, 200)

    def test_detail_url_exists_at_desired_location(self):
        self.assertEqual(
            self.client.get(f'/detail/{self.test_alim.pk}/').status_code, 200)

    def test_result_url_exists_at_desired_location(self):
        self.assertEqual(
            self.client.get(
                '/result?search_alim=petit+beurre').status_code, 200)

    def test_legal_url_exists_at_desired_location(self):
        self.assertEqual(self.client.get('/legal').status_code, 200)

    def test_contact_url_exists_at_desired_location(self):
        self.assertEqual(self.client.get('/contact').status_code, 200)

    def test_add_alim_url_exists_at_desired_location(self):
        self.assertEqual(self.client.get('/add_alim/').status_code, 302)

    def test_remove_url_exists_at_desired_location(self):
        self.assertEqual(self.client.get('/remove_alim/').status_code, 302)

    def test_account_register_url_exists_at_desired_location(self):
        self.assertEqual(
            self.client.get('/accounts/register').status_code, 200)

    def test_user_urls_redirects(self):
        self.assertEqual(self.client.get('/user').status_code, 302)

    def test_my_aliments_redirects(self):
        self.assertEqual(self.client.get('/my-aliments').status_code, 302)
