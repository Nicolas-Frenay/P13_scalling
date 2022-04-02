import pytest
from django.urls import reverse, resolve
from django.test import Client
from .models import Letting, Address


@pytest.mark.django_db
class TestLetting:
    """
    test class for lettings
    """
    def create_address(self):
        """
        Create a temporary address for the tests
        :return: Adress object
        """
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
        """
        Create a temporary letting for the tests
        :return: Letting object
        """
        address = self.create_address()
        letting = Letting.objects.create(title='titre', address=address)
        return letting

    def test_index_lettings(self):
        """
        test that check if lettings index page uses the correct url path
        :return: test result
        """
        path = reverse('lettings:index')
        assert resolve(path).view_name == 'lettings:index'

    def test_index_lettings_view(self):
        """
        test that check if lettings index page use the correct template (by
        search for correct <title> in HTML)
        :return: test result
        """
        client = Client()
        path = reverse('lettings:index')
        response = client.get(path)
        content = response.content.decode()
        expected_content = '<title>Lettings</title>'
        assert expected_content in content

    def test_letting_url(self):
        """
        test that check if single letting page uses the correct url path
        :return: test result
        """
        letting = self.create_letting()
        path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
        assert resolve(path).view_name == 'lettings:letting'

    def test_letting_view(self):
        """
        test that check if single letting page use the correct template (by
        search for correct <title> in HTML)
        :return: test result
        """
        letting = self.create_letting()
        client = Client()
        path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
        response = client.get(path)
        content = response.content.decode()
        expected_content = '<title>' + letting.title + '</title>'
        assert expected_content in content
