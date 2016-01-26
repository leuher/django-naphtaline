"""
django-naphtaline URL configuration
"""
from django.conf.urls import url

from . import views

# pylint: disable=invalid-name
urlpatterns = [
    url(r'^$', views.home, name='home'),
]
