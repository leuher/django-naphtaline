"""
naphtaline.views.login unit tests
"""
from django.core.urlresolvers import reverse
from django.test import TestCase


class LoginViewTests(TestCase):
    """
    Test the login view

    https://github.com/django/django/blob/master/tests/auth_tests/test_views.py
    """

    def test_render(self):
        """
        Display the login form
        """
        response = self.client.get(reverse('naphtaline:login'))
        self.assertEqual(response.status_code, 200)
