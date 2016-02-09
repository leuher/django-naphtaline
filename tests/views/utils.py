"""
napthaline view test utilities
"""
from django.contrib.auth.models import User
from django.test import TestCase


class UserTestCase(TestCase):
    """
    TestCase providing user credentials for @login_required view tests
    """

    @classmethod
    def setUpClass(cls):
        """
        Creates a user
        """
        super(UserTestCase, cls).setUpClass()
        cls.user_name = 'nemo'
        cls.user_email = 'nemo@nautil.us'
        cls.user_password = 'm0b1l15'
        cls.user = User.objects.create_user(
            username=cls.user_name,
            email=cls.user_email,
            password=cls.user_password
        )
