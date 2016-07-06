# -*- coding: utf-8 -*-
"""
django-naphtaline - views
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import BookForm
from .models import Book


def home(request):
    """
    Home page
    """
    return render(request, 'naphtaline/home.djhtml')


@login_required
def add_book(request):
    """
    Add a new book
    """
    if request.method == 'POST':
        # TODO
        return
    form = BookForm()
    return render(request, 'naphtaline/add_book.djhtml', {'form': form})


@login_required
def list_books(request):
    """
    Lists all books owned by the current user
    """
    return render(
        request,
        'naphtaline/list_books.djhtml',
        {
            'books': Book.objects.filter(
                owners=request.user
            ).order_by('title')
        }
    )
