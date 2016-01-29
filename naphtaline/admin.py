# -*- coding: utf-8 -*-
"""
django-naphtaline - administration interface settings
"""
from django.contrib import admin

from .models import Artist, Book, Company, Publication


class ArtistAdmin(admin.ModelAdmin):
    """
    Artist display options
    """

    list_display = ('last_name', 'first_name')


class BookAdmin(admin.ModelAdmin):
    """
    Book display options
    """

    list_display = ('title', )


class PublicationAdmin(admin.ModelAdmin):
    """
    Publication display options
    """

    list_display = ('title', 'publisher', 'isbn13')


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Company)
admin.site.register(Publication, PublicationAdmin)
