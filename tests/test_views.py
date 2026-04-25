from django.test import TestCase
from django.urls import reverse


class TestLogin(TestCase):

    fixtures = ['users']

    def test_GET(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_user_login_success(self):
        data = {'username': "TestUser1", 'password': 'thisiscorrect'}
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)

    def test_good_login_redirect_to_landing(self):
        data = {'username': "TestUser1", 'password': 'thisiscorrect'}
        response = self.client.post(reverse('login'), data)
        self.assertRedirects(response, reverse('landing'))

    def test_user_login_fail(self):
        data = {'username': "TestUser1", 'password': 'thisiswrong'}
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)