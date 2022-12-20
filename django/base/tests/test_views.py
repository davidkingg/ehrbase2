from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        self.home_url=reverse('home')
        self.login_url=reverse('login')
        self.logout_url=reverse('logout')
        self.register_url=reverse('register')
        self.userlist_url=reverse('userlist')
        self.new_user= User.objects.create(username='new_user',password='1234')
        self.profile_url=reverse('profile',args=[self.new_user.id])
        


        

    def test_home(self):
        response=self.client.get(self.home_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'base/home.html')

    def test_login_get(self):
        response=self.client.get(self.login_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'base/login_page.html')

    def test_login_post(self):
        response=self.client.post(self.login_url, {'username':'king','password':1122})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'base/login_page.html')


    def test_register_get(self):
        response=self.client.get(self.register_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'base/signup.html')

    def test_register_post(self):
        response=self.client.post(self.register_url,{'username':'king','password':1122})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'base/signup.html')

    def test_profile(self):
        response=self.client.get(self.profile_url)
        self.assertEquals(response.status_code,200)

    def test_userlist(self):
        response=self.client.get(self.userlist_url)
        self.assertEquals(response.status_code,302)


    
