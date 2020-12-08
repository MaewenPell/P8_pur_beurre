from django.test import TestCase
from selenium.webdriver import Firefox
from django.contrib.auth.models import User
from django.contrib import auth


class NewUserFormTest(TestCase):
    def setUp(self):
        self.driver = Firefox()

    def test_FormRegister(self):
        self.driver.get("http://127.0.0.1:8000/accounts/register")
        self.driver.find_element_by_id("id_username").send_keys('TestUserSelenium')
        self.driver.find_element_by_id("id_email").send_keys('testuser@testuserselenium.com')
        self.driver.find_element_by_id("id_password1").send_keys('superpassword_1&')
        self.driver.find_element_by_id("id_password2").send_keys('superpassword_1&')
        self.driver.find_element_by_id("id_sign_up").click()

    # def test_new_user_name_equal_exepected(self):
    #     created_user = User.objects.get(username='TestUserSelenium')
    #     self.assertEqual(created_user.username, "TestUserSelenium")

    # def test_new_user_str_equal_expected(self):
    #     created_user = User.objects.get(username='TestUserSelenium')
    #     self.assertEqual(created_user.__str__(), "TestUserSelenium")

    # def test_new_user_email_equal_expected(self):
    #     created_user = User.objects.get(username='TestUserSelenium')
    #     self.assertEqual(created_user.email, "testuser@testuserselenium.com")

    def tearDown(self):
        self.driver.quit()


class NewUserAddFavorite(TestCase):
    def setUp(self):
        self.driver = Firefox(executable_path='/usr/local/bin/geckodriver')
        self.response = self.driver.get("http://127.0.0.1:8000/accounts/login/")
        self.driver.find_element_by_id("id_username").send_keys('TestUserSelenium')
        self.driver.find_element_by_id("id_password").send_keys('superpassword_1&')

    def test_redirection_index(self):
        self.driver.find_element_by_id("id_login").click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/")

    def tearDown(self):
        pass
        # self.driver.quit()
