# -*- coding: utf-8 -*-
"""
django-naphtaline - models
"""
from django.contrib.auth import models as auth_models
from django.db import models


class ISBN13Field(models.CharField):
    """
    ISBN 13-digit string representation
    """

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 13
        kwargs['verbose_name'] = "ISBN-13"
        super(ISBN13Field, self).__init__(*args, **kwargs)


class Artist(models.Model):
    """
    Author/writer/illustrator/...
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Company(models.Model):
    """
    Edition/publication company
    """

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book information
    """

    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Artist)

    class Meta():
        ordering = ['title']

    def __str__(self):
        return self.title


class Publication(Book):
    """
    Publication-specific information
    """

    isbn13 = ISBN13Field()
    publisher = models.ForeignKey(Company)
    pub_date = models.DateField(blank=True)
    owners = models.ManyToManyField(auth_models.User)

    def __str__(self):
        return self.title
