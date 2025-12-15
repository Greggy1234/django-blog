from django.test import TestCase
from .forms import CollaborateForm


# Create your tests here.
class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Greg',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_is_not_valid_name(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="No name field given in test")

    def test_form_is_not_valid_email(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Greg',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="No email field given in test")

    def test_form_is_not_valid_message(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Greg',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="No message field given in test")
