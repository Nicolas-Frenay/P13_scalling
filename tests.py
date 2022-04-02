from django.urls import reverse, resolve
from django.test import Client


def test_home():
    """
    test that check if home page uses the correct url path
    :return: test result
    """
    path = reverse('home:index')
    assert resolve(path).view_name == 'home:index'


def test_home_view():
    """
    test that check if home page use the correct template (by search for
    correct <title> in HTML)
    :return: test result
    """
    client = Client()
    path = reverse('home:index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = '<title>Holiday Homes</title>'
    assert expected_content in content
