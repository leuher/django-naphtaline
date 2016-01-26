"""
naphtaline.views.home unit tests
"""
from django.core.urlresolvers import reverse
from django.test import TestCase


class HomeViewTests(TestCase):
    """
    Test the home view
    """

    def test_render(self):
        """
        Render the page
        """
        response = self.client.get(reverse('naphtaline:home'))
        self.assertEqual(response.status_code, 200)
