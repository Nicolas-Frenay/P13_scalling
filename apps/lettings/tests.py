import pytest
from django.urls import reverse, resolve
from django.test import Client
from .models import Letting, Address


def test_index_lettings():
    path = reverse('lettings:index')
    assert resolve(path).view_name == 'lettings:index'

@pytest.mark.django_db
def test_index_lettings_view():
    client = Client()
    path = reverse('lettings:index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = '<title>Lettings</title>'
    assert expected_content in content

@pytest.mark.django_db
def test_letting_view():
    address_dict = {
        'number': 42,
        'street': 'rue',
        'city': 'ville',
        'state': 'etat',
        'zip_code': 42,
        'country_iso_code': '+42'
    }
    address = Address.objects.create(**address_dict)
    letting = Letting.objects.create(title='titre', address=address)
    client = Client()
    path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(path)
    content = response.content.decode()
    expected_content = letting.title
    assert expected_content in content
