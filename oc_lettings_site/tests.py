from django.urls import reverse, resolve
from django.test import Client


def test_home():
    path = reverse('home:index')
    assert resolve(path).view_name == 'home:index'

def test_home_view():
    client = Client()
    path = reverse('home:index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = '<title>Holiday Homes</title>'
    assert expected_content in content
