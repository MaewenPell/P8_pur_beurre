from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from time import sleep
from django.urls import reverse
from store.models import Aliment, Category
from django.contrib.auth import get_user_model


class NewUserFormTest(LiveServerTestCase):
    def setUp(self):
        Category.objects.create(category="Test Category")
        test_cat = Category.objects.get(category="Test Category")
        Aliment.objects.create(category=test_cat, name="Test alim",
                               nutriscore="X",
                               image_url="https://image_url.org",
                               product_url="https://product_url.org",
                               sugar="X",
                               fat="Y", salt="Z", energy="ABC",
                               average=3)
        Aliment.objects.create(category=test_cat, name="Better Alim",
                               nutriscore="A", image_url="https://dsqd.org",
                               product_url="https://dqs.org", sugar="X",
                               fat="Y", salt="Z", energy="ABC",
                               average=5)
        User = get_user_model()
        user = User.objects.create_user('Testuser_2', password='abd1234@dsdq')
        user.is_superuser = False
        user.is_staff = False
        user.save()

        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=opts)

    def connect_user(self):
        self.driver.get(f'{self.live_server_url}{reverse("login")}')
        self.driver.find_element_by_xpath(
            '//*[@id="id_username"]').send_keys("Testuser_2")
        self.driver.find_element_by_xpath(
            '//*[@id="id_password"]').send_keys("abd1234@dsdq")
        sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id = "id_login_btn"]').click()

    def test_creation_user(self):
        self.driver.get(f'{self.live_server_url}{reverse("register")}')
        self.driver.find_element_by_id(
            "id_username").send_keys('TestUserSelenium')
        self.driver.find_element_by_id("id_email").send_keys(
            'testuser@testuserselenium.com')
        self.driver.find_element_by_id(
            "id_password1").send_keys('superpassword_1&')
        self.driver.find_element_by_id(
            "id_password2").send_keys('superpassword_1&')
        sleep(1)
        self.driver.find_element_by_id("id_sign_up").click()
        sleep(3)
        self.driver.find_element_by_id("id_profile").click()
        greetings = self.driver.find_element_by_id("greetings")
        self.assertEqual(self.driver.current_url,
                         f"{self.live_server_url}/user")
        self.assertEqual(greetings.text, "Bonjour TestUserSelenium")

    def test_connection(self):
        self.driver.get(f'{self.live_server_url}{reverse("login")}')
        self.driver.find_element_by_xpath(
            '//*[@id="id_username"]').send_keys("Testuser_2")
        self.driver.find_element_by_xpath(
            '//*[@id="id_password"]').send_keys("abd1234@dsdq")
        sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id = "id_login_btn"]').click()
        self.assertEqual(self.driver.current_url,
                         f'{self.live_server_url}{reverse("index")}')

    def test_search(self):
        # First we connect a user
        self.connect_user()

        # We look for a product
        self.driver.find_element_by_xpath("/html/body/nav/div/a").click()
        sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/header/div/div/div[2]/form/input").send_keys(
                'Test alim')
        self.driver.find_element_by_xpath(
            "/html/body/header/div/div/div[2]/form/button").click()

        nutriscore = self.driver.find_element_by_xpath(
            "/html/body/section/div/div/div/div/div/div/span").text
        button_add = self.driver.find_element_by_xpath(
            "/html/body/section/div/div/div/div/div/div/div/form/button")

        self.assertTrue(button_add.is_enabled)
        self.assertLess(nutriscore, "X")

    def test_assert_checkbox_is_present(self):
        # First we connect a user
        self.connect_user()

        a = self.driver.find_element_by_xpath("/html/body/nav/div/a")
        self.assertIsNotNone(a)

    def test_add_alim(self):
        # First we connect a user
        self.connect_user()

        # We look for a product
        self.driver.find_element_by_xpath("/html/body/nav/div/a").click()
        sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/header/div/div/div[2]/form/input").send_keys(
                'Test alim')
        self.driver.find_element_by_xpath(
            "/html/body/header/div/div/div[2]/form/button").click()

        # We add an alim
        btn_add = (
            "/html/body/section/div/div/div/\
                div/div/div/div/form/button")
        self.driver.find_element_by_xpath(btn_add.replace(" ", "")).click()

        # We check that it's displayed in my_alim
        self.driver.find_element_by_xpath(
            "/html/body/nav/div/div/ul/li[2]/a/i").click()
        title_alim = self.driver.find_element_by_xpath(
            "/html/body/section/div/div/div/div/div/div/div/a/h4"
        ).text

        self.assertEqual(title_alim, "Better Alim")

    def test_remove_alim(self):
        # First we connect a user
        self.connect_user()

        # We look for a product
        self.driver.find_element_by_xpath("/html/body/nav/div/a").click()
        sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/header/div/div/div[2]/form/input").send_keys(
                'Test alim')
        self.driver.find_element_by_xpath(
            "/html/body/header/div/div/div[2]/form/button").click()

        # We add an alim
        self.driver.find_element_by_xpath(
            "/html/body/section/div/div/div/div/\
                div/div/div/form/button").click()

        # We remove it from my alims
        self.driver.find_element_by_xpath(
            "/html/body/nav/div/div/ul/li[2]/a/i").click()

        self.driver.find_element_by_xpath(
            "/html/body/section/div/div/div/div/div[1]/div/div/form/button"
        ).click()

        message = self.driver.find_element_by_xpath(
            "/html/body/section/div/div/div/h2").text
        pop_up = self.driver.find_element_by_xpath(
            "/html/body/section/div/div/div/div[1]/p").text

        self.assertEqual(message, "Vous n'avez aucun aliment sauvegardé")
        self.assertEqual(pop_up, "Aliment retiré des favoris")

    def tearDown(self):
        self.driver.close()
