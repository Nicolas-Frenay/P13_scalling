import pytest
from django.urls import reverse, resolve
from django.test import Client
from django.contrib.auth.models import User
from .models import Profile


def test_index_profiles():
    path = reverse('profiles:index')
    assert resolve(path).view_name == 'profiles:index'


# def test_profile():
#     pat = resolve()


@pytest.mark.django_db
def test_index_profiles_view():
    client = Client()
    path = reverse('profiles:index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = '<title>Profiles</title>'
    assert expected_content in content


@pytest.mark.django_db
def test_profile_view():
    user = User.objects.create(username='toto', password='totototo1')
    profile = Profile.objects.create(user=user, favorite_city='ville')
    client = Client()
    path = reverse('profiles:profile', kwargs={'username': user.username})
    response = client.get(path)
    content = response.content.decode()
    expected_content = profile.user.username
    assert expected_content in content
