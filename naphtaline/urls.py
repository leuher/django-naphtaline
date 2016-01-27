"""
django-naphtaline URL configuration
"""
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

# pylint: disable=invalid-name
urlpatterns = [
    url(
        r'^login/$',
        auth_views.login,
        {'template_name': 'naphtaline/login.djhtml'},
        name='login',
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        {'next_page': 'naphtaline:home'},
        name='logout',
    ),
    url(r'^$', views.home, name='home'),
]
