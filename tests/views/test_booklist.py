"""
naphtaline.views.booklist unit tests
"""
from django.core.urlresolvers import reverse

from .utils import UserTestCase


class BooklistViewTests(UserTestCase):
    """
    Test the book list view
    """

    def test_render(self):
        """
        Render the page
        """
        self.client.login(username=self.user_name, password=self.user_password)
        response = self.client.get(reverse('naphtaline:list_books'))
        self.assertEqual(response.status_code, 200)
