import pytest
from django.urls import reverse, resolve
from django.test import Client
from .models import Letting, Address


@pytest.mark.django_db
class TestLetting:
    def create_address(self):
        address_dict = {
            'number': 42,
            'street': 'rue',
            'city': 'ville',
            'state': 'etat',
            'zip_code': 42,
            'country_iso_code': '+42'
        }
        address = Address.objects.create(**address_dict)
        return address

    def create_letting(self):
        address = self.create_address()
        letting = Letting.objects.create(title='titre', address=address)
        return letting

    def test_index_lettings(self):
        path = reverse('lettings:index')
        assert resolve(path).view_name == 'lettings:index'

    def test_index_lettings_view(self):
        client = Client()
        path = reverse('lettings:index')
        response = client.get(path)
        content = response.content.decode()
        expected_content = '<title>Lettings</title>'
        assert expected_content in content

    def test_letting_url(self):
        letting = self.create_letting()
        path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
        assert resolve(path).view_name == 'lettings:letting'

    def test_letting_view(self):
        letting = self.create_letting()
        client = Client()
        path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
        response = client.get(path)
        content = response.content.decode()
        expected_content = '<title>' + letting.title + '</title>'
        assert expected_content in content
