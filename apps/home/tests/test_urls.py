import pytest
from django.urls import reverse, resolve


def test_home():
    path = reverse('home:index')
    assert resolve(path).view_name == 'home:index'