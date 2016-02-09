# -*- coding: utf-8 -*-
"""
django-naphtaline - views
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Publication


def home(request):
    """
    Home page
    """
    return render(request, 'naphtaline/home.djhtml')


@login_required
def booklist(request):
    """
    Book list
    """
    return render(
        request,
        'naphtaline/publication_list.djhtml',
        {
            'publications': Publication.objects.filter(
                owners=request.user
            ).order_by('book__title')
        }
    )
