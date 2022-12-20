from django.test import SimpleTestCase
from django.urls import reverse,resolve
from base.views import *

class TestUrls(SimpleTestCase):
    def test_login_url_is_resolved(self):
        url =reverse('login')
        print (resolve(url))
        self.assertEqual(resolve(url).func, Login)

    def test_home_url_is_resolved(self):
        url =reverse('home')
        print (resolve(url))
        self.assertEqual(resolve(url).func, home)

    def test_logout_url_is_resolved(self):
        url =reverse('logout')
        print (resolve(url))
        self.assertEqual(resolve(url).func, Logout)

    def test_register_url_is_resolved(self):
        url =reverse('register')
        print (resolve(url))
        self.assertEqual(resolve(url).func, register)

    def test_userlist_url_is_resolved(self):
        url =reverse('userlist')
        print (resolve(url))
        self.assertEqual(resolve(url).func, userlist)

    def test_profile_url_is_resolved(self):
        url =reverse('profile',args=['str'])
        print (resolve(url))
        self.assertEqual(resolve(url).func, profile)