# -*- coding: utf-8 -*-
"""
naphtaline.models unit tests
"""
from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from naphtaline.models import Artist, Book, Company


class ArtistTests(TestCase):
    """
    Artist model unit tests
    """

    @classmethod
    def setUpTestData(cls):
        Artist.objects.create(
            first_name="Nyarla",
            last_name="Thotep",
        )
        Artist.objects.create(
            first_name="John",
            last_name="Smith",
        )
        Artist.objects.create(
            first_name="Grůdü",
            last_name="Æbër¢øłd",
        )

    def test_create(self):
        """
        Entry creation
        """
        artist = Artist.objects.get(pk=1)
        self.assertEqual(artist.first_name, "Nyarla")
        self.assertEqual(artist.last_name, "Thotep")

    def test_str(self):
        """
        String representation
        """
        artist = Artist.objects.get(pk=1)
        self.assertEqual(str(artist), "Nyarla Thotep")

    def test_unicode_str(self):
        """
        String representation (with funny Unicode chars)
        """
        artist = Artist.objects.get(pk=3)
        self.assertEqual(str(artist), "Grůdü Æbër¢øłd")


class CompanyTests(TestCase):
    """
    Company model unit tests
    """

    @classmethod
    def setUpTestData(cls):
        Company.objects.create(name="Flibidi, Inc.")
        Company.objects.create(name="")

    def test_create(self):
        """
        Entry creation
        """
        company = Company.objects.get(pk=1)
        self.assertEqual(company.name, "Flibidi, Inc.")

    def test_str(self):
        """
        String representation
        """
        company = Company.objects.get(pk=1)
        self.assertEqual(str(company), "Flibidi, Inc.")


class BookTests(TestCase):
    """
    Book model unit tests
    """

    @classmethod
    def setUpTestData(cls):
        Artist.objects.create(
            first_name="John",
            last_name="Smith",
        )
        Artist.objects.create(
            first_name="Ush",
            last_name="As",
        )

        publisher = Company.objects.create(name="Timey-Wimey, Inc.")

        cls.book = Book.objects.create(
            title="Gallifreyan Chronicles",
            isbn13='1234567891234',
            publisher=publisher,
            pub_date=datetime.now()
        )

        User.objects.create_user(
            username='the_silence',
            email='silence@the-library.com',
            password='shhhhttttt!'
        )
        User.objects.create_user(
            username='river_song',
            email='dr_song@the-library.com',
            password='m3l0dy§'
        )

    def test_create(self):
        """
        Entry creation
        """
        self.assertEqual(self.book.title, "Gallifreyan Chronicles")
        self.assertEqual(self.book.isbn13, '1234567891234')

    def test_str(self):
        """
        String representation
        """
        self.assertEqual(str(self.book), "Gallifreyan Chronicles")

    def test_add_single_author(self):
        """
        Add an author for a Book
        """
        artist = Artist.objects.get(pk=1)
        self.book.authors.add(artist)
        self.assertQuerysetEqual(
            self.book.authors.all(),
            [repr(artist)]
        )
        self.assertQuerysetEqual(
            artist.book_set.all(),
            [repr(self.book)]
        )

    def test_add_multiple_authors(self):
        """
        Add several authors for a Book
        """
        artist1 = Artist.objects.get(pk=1)
        artist2 = Artist.objects.get(pk=2)
        self.book.authors.add(artist1, artist2)
        self.assertQuerysetEqual(
            self.book.authors.all(),
            [repr(artist1), repr(artist2)],
            ordered=False
        )
        self.assertQuerysetEqual(
            artist1.book_set.all(),
            [repr(self.book)]
        )
        self.assertQuerysetEqual(
            artist2.book_set.all(),
            [repr(self.book)]
        )

    def test_add_single_owner(self):
        """
        Add an owner for a Book
        """
        # https://github.com/landscapeio/pylint-django/issues/53
        # pylint: disable=no-member
        owner = User.objects.get(pk=1)
        self.book.owners.add(owner)
        self.assertQuerysetEqual(
            self.book.owners.all(),
            [repr(owner)]
        )
        self.assertQuerysetEqual(
            owner.book_set.all(),
            [repr(self.book)]
        )

    def test_add_multiple_owners(self):
        """
        Add several owners for a Book
        """
        # https://github.com/landscapeio/pylint-django/issues/53
        # pylint: disable=no-member
        owner1 = User.objects.get(pk=1)
        owner2 = User.objects.get(pk=2)
        self.book.owners.add(owner1, owner2)
        self.assertQuerysetEqual(
            self.book.owners.all(),
            [repr(owner1), repr(owner2)],
            ordered=False
        )
        self.assertQuerysetEqual(
            owner1.book_set.all(),
            [repr(self.book)]
        )
        self.assertQuerysetEqual(
            owner2.book_set.all(),
            [repr(self.book)]
        )
