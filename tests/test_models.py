# -*- coding: utf-8 -*-
"""
naphtaline.models unit tests
"""
from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from naphtaline.models import Artist, Book, Company, Publication


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
        Book.objects.create(title="Gallifreyan Chronicles")

    def test_create(self):
        """
        Entry creation
        """
        self.assertEqual(Book.objects.get(pk=1).title, "Gallifreyan Chronicles")

    def test_str(self):
        """
        String representation
        """
        self.assertEqual(str(Book.objects.get(pk=1)), "Gallifreyan Chronicles")

    def test_add_single_author(self):
        """
        Add an author for a Book
        """
        book = Book.objects.get(pk=1)
        artist = Artist.objects.get(pk=1)
        book.authors.add(artist)
        self.assertQuerysetEqual(
            book.authors.all(),
            [repr(artist)]
        )
        self.assertQuerysetEqual(
            artist.book_set.all(),
            [repr(book)]
        )

    def test_add_multiple_authors(self):
        """
        Add several authors for a Book
        """
        book = Book.objects.get(pk=1)
        artist1 = Artist.objects.get(pk=1)
        artist2 = Artist.objects.get(pk=2)
        book.authors.add(artist1, artist2)
        self.assertQuerysetEqual(
            book.authors.all(),
            [repr(artist1), repr(artist2)],
            ordered=False
        )
        self.assertQuerysetEqual(
            artist1.book_set.all(),
            [repr(book)]
        )
        self.assertQuerysetEqual(
            artist2.book_set.all(),
            [repr(book)]
        )


class PublicationTests(TestCase):
    """
    Publication model unit tests
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
        publisher = Company.objects.create(name="Timey-Wimey, Inc.")
        Publication.objects.create(
            title="Gallifreyan Chronicles",
            isbn13='1234567891234',
            publisher=publisher,
            pub_date=datetime.now()
        )

    def test_create(self):
        """
        Entry creation
        """
        book = Publication.objects.get(pk=1)
        self.assertEqual(book.title, "Gallifreyan Chronicles")
        publication = Publication.objects.get(pk=1)
        self.assertEqual(publication.title, "Gallifreyan Chronicles")

    def test_str(self):
        """
        String representation
        """
        publication = Publication.objects.get(pk=1)
        self.assertEqual(publication.title, "Gallifreyan Chronicles")

    def test_add_single_author(self):
        """
        Add an author for a Book
        """
        book = Book.objects.get(pk=1)
        publication = Publication.objects.get(pk=1)
        artist = Artist.objects.get(pk=1)
        publication.authors.add(artist)
        self.assertQuerysetEqual(
            publication.authors.all(),
            [repr(artist)]
        )
        self.assertQuerysetEqual(
            artist.book_set.all(),
            [repr(book)]
        )

    def test_add_multiple_authors(self):
        """
        Add several authors for a Publication
        """
        book = Book.objects.get(pk=1)
        publication = Publication.objects.get(pk=1)
        artist1 = Artist.objects.get(pk=1)
        artist2 = Artist.objects.get(pk=2)
        publication.authors.add(artist1, artist2)
        self.assertQuerysetEqual(
            publication.authors.all(),
            [repr(artist1), repr(artist2)],
            ordered=False
        )
        self.assertQuerysetEqual(
            artist1.book_set.all(),
            [repr(book)]
        )
        self.assertQuerysetEqual(
            artist2.book_set.all(),
            [repr(book)]
        )

    def test_add_single_owner(self):
        """
        Add an owner for a Publication
        """
        # https://github.com/landscapeio/pylint-django/issues/53
        # pylint: disable=no-member
        publication = Publication.objects.get(pk=1)
        owner = User.objects.get(pk=1)
        publication.owners.add(owner)
        self.assertQuerysetEqual(
            publication.owners.all(),
            [repr(owner)]
        )
        self.assertQuerysetEqual(
            owner.publication_set.all(),
            [repr(publication)]
        )

    def test_add_multiple_owner(self):
        """
        Add several owners for a Publication
        """
        # https://github.com/landscapeio/pylint-django/issues/53
        # pylint: disable=no-member
        publication = Publication.objects.get(pk=1)
        owner1 = User.objects.get(pk=1)
        owner2 = User.objects.get(pk=2)
        publication.owners.add(owner1, owner2)
        self.assertQuerysetEqual(
            publication.owners.all(),
            [repr(owner1), repr(owner2)],
            ordered=False
        )
        self.assertQuerysetEqual(
            owner1.publication_set.all(),
            [repr(publication)]
        )
        self.assertQuerysetEqual(
            owner2.publication_set.all(),
            [repr(publication)]
        )
