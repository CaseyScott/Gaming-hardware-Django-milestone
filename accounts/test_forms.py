from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

class TestUserLoginForm(TestCase):

    def test_create_a_user_with_username_and_password(self):
        form = UserLoginForm({'username': 'testname',
                              'password': 'testpassword'})
        self.assertTrue(form.is_valid())

    def test_fail_to_create_a_user_without_required_values(self):
        form = UserLoginForm({'username': 'testname'})
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_correct_message_for_missing_password(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])


class TestRegistrationForm(TestCase):

    def test_can_create_user_with_required_values(self):
        form = UserRegistrationForm({'username': 'testname',
                                     'email': 'testemail@example.com',
                                     'password1': 'testpassword',
                                     'password2': 'testpassword'})
        self.assertTrue(form.is_valid())

    def test_cannot_create_a_user_without_matching_passwords(self):
        form = UserRegistrationForm({'username': 'testname',
                                     'email': 'testemail@example.com',
                                     'password1': 'testpassword',
                                     'password2': 'falsepassword'})
        self.assertFalse(form.is_valid())

    def test_cannot_register_a_user_without_required_values(self):
        form = UserLoginForm({'username': 'testname'})
        self.assertFalse(form.is_valid())
