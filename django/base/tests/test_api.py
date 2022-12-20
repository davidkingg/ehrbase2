from django.test import SimpleTestCase
from django.urls import reverse,resolve
from base.api.views import *


class TestUrls(SimpleTestCase):
    def test_login_url_is_resolved(self):
        url =reverse('api_users')
        print (resolve(url))
        self.assertEqual(resolve(url).func, getUsers)