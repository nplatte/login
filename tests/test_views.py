from django.test import TestCase
from django.urls import reverse


class TestLogin(TestCase):

    fixtures = ['users']

    def setUp(self):
        self.data = {'username': "testuser", 'password': 'thisiscorrect'}
        return super().setUp()
        
    def test_GET(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_user_login_success(self):
        response = self.client.post(reverse('login'), self.data)
        self.assertEqual(response.status_code, 302)

    def test_good_login_redirect_to_landing(self):
        response = self.client.post(reverse('login'), self.data)
        self.assertRedirects(response, reverse('landing'))

    def test_user_login_fail(self):
        self.data['password'] = 'wrong'
        response = self.client.post(reverse('login'), self.data)
        self.assertEqual(response.status_code, 200)