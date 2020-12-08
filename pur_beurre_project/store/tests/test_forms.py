from django.test import TestCase
from store.forms.forms import SignUpForm


class RegisterFromTest(TestCase):
    def setUp(self):
        self.form = SignUpForm()

    def test_forms_fields(self):
        self.assertIsNotNone(self.form.fields['username'])
        self.assertIsNotNone(self.form.fields['email'])
        self.assertIsNotNone(self.form.fields['password1'])
        self.assertIsNotNone(self.form.fields['password2'])
