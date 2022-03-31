from django.test import Client
from django.urls import reverse


def test_home_view():
    client = Client()
    path = reverse('home:index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = '<title>Holiday Homes</title>'
    assert expected_content in content

