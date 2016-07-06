# -*- coding: utf-8 -*-
"""
django-naphtaline - forms
"""
from django.forms import ModelForm

from .models import Artist, Book, Company


class ArtistForm(ModelForm):
    """
    Artist addition/edition form
    """

    class Meta:
        model = Artist
        fields = ['first_name', 'last_name']


class CompanyForm(ModelForm):
    """
    Company addition/edition form
    """

    class Meta:
        model = Company
        fields = ['name']


class BookForm(ModelForm):
    """
    Book addition/edition form
    """

    class Meta:
        model = Book
        fields = ['isbn13', 'title', 'pub_date']
