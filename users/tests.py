from django.test import TestCase
from django.urls import reverse
from django.contrib.sites.models import Site

from users.forms import User
from allauth.socialaccount.models import SocialApp


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:register')
        self.test_data = {
            'first_name': 'Егор',
            'last_name': 'Володин',
            'username': 'EgorVolodin1',
            'email': 'egorv@gmail.com',
            'password1': 'sosopopo',
            'password2': 'sosopopo',
        }

        site = Site.objects.get_current()
        app = SocialApp.objects.create(
            provider="github",
            name="GitHub",
            client_id="dummy_client_id",
            secret="dummy_secret",
        )
        app.sites.add(site)

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_post_success(self):
        username = self.test_data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.test_data)


        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())


