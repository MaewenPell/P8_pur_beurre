from django.test import TestCase
from selenium.webdriver import Firefox
from django.contrib.auth.models import User
from selenium.webdriver.common.keys import Keys
from django.contrib import auth
from time import sleep


class NewUserFormTest(TestCase):
    def setUp(self):
        self.driver = Firefox(executable_path='/usr/local/bin/geckodriver')
        self.driver.get("http://127.0.0.1:8000/accounts/register")

    def test_register_user(self):
        self.driver.find_element_by_id("id_username").send_keys('TestUserSelenium')
        self.driver.find_element_by_id("id_email").send_keys('testuser@testuserselenium.com')
        self.driver.find_element_by_id("id_password1").send_keys('superpassword_1&')
        self.driver.find_element_by_id("id_password2").send_keys('superpassword_1&')
        self.driver.find_element_by_id("id_sign_up").click()

        sleep(3)

        self.driver.find_element_by_id("id_profile").click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/user")
        greetings = self.driver.find_element_by_id("greetings")
        self.assertEqual(greetings.text, "Bonjour TestUserSelenium")

    def tearDown(self):
        self.driver.quit()


class UserStory(TestCase):
    def setUp(self):
        self.driver = Firefox(executable_path='/usr/local/bin/geckodriver')
        self.driver.get("http://127.0.0.1:8000/")

    def test_connect(self):
        self.driver.find_element_by_id("id_login").click()
        self.driver.find_element_by_id("id_username").send_keys('TestUserSelenium')
        self.driver.find_element_by_id("id_password").send_keys('superpassword_1&')
        self.driver.find_element_by_id("id_password").send_keys(Keys.RETURN)

        sleep(3)

        self.driver.find_element_by_id('id_profile').click()
        greetings = self.driver.find_element_by_id("greetings")
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/user")
        self.assertEqual(greetings.text, "Bonjour TestUserSelenium")

