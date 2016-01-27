"""
naphtaline.views.logout unit tests
"""
from django.core.urlresolvers import reverse
from django.test import TestCase


class LogoutViewTests(TestCase):
    """
    Test the logout view
    """

    def test_redirect_after_logout(self):
        """
        Rendirect to the home page after logout
        """
        response = self.client.get(reverse('naphtaline:logout'))
        self.assertEqual(response.status_code, 302)
