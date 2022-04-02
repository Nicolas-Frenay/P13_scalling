import pytest
from django.urls import reverse, resolve
from django.test import Client
from django.contrib.auth.models import User
from .models import Profile


@pytest.mark.django_db
class TestProfile:
    """
    Test class for profiles
    """
    def create_profile(self):
        """
        Create a temporary profile for the tests
        :return: Profile object
        """
        user = User.objects.create(username='toto', password='totototo1')
        profile = Profile.objects.create(user=user, favorite_city='ville')
        return profile

    def test_index_profiles(self):
        """
        test that check if profiles index page uses the correct url path
        :return: test result
        """
        path = reverse('profiles:index')
        assert resolve(path).view_name == 'profiles:index'

    def test_index_profiles_view(self):
        """
        test that check if profiles index page use the correct template (by
        search for correct <title> in HTML)
        :return: test result
        """
        client = Client()
        path = reverse('profiles:index')
        response = client.get(path)
        content = response.content.decode()
        expected_content = '<title>Profiles</title>'
        assert expected_content in content

    def test_profile_url(self):
        """
        test that check if single profile page uses the correct url path
        :return: test result
        """
        profile = self.create_profile()
        path = reverse('profiles:profile', kwargs={
            'username': profile.user.username})
        assert resolve(path).view_name == 'profiles:profile'

    def test_profile_view(self):
        """
        test that check if single profile page use the correct template (by
        search for correct <title> in HTML)
        :return: test result
        """
        profile = self.create_profile()
        client = Client()
        path = reverse('profiles:profile',
                       kwargs={'username': profile.user.username})
        response = client.get(path)
        content = response.content.decode()
        expected_content = '<title>' + profile.user.username + '</title>'
        assert expected_content in content
