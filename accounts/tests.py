
from django.test import TestCase
from .models import Profile
from django.urls import reverse


class TestProfileModelCase(TestCase):

    def create_profile(self):
        return Profile.objects.create(username="testuser",email="user@test.com",last_name="user",first_name="user-first",country="Nigeria",phone="223345")

    def test_model_str(self):
        user = self.create_profile()
        self.assertTrue(isinstance(user,Profile))
        self.assertEqual(user.__str__(), user.username)


class Test_Profile_List_Views(TestCase):
    def setup(self):
        Profile.objects.create(username="testuser",email="user@test.com",last_name="user",first_name="user-first",country="Nigeria",phone="223345")

    def get_url(self):
        return self.client.get(reverse("accounts:users_list"))

    def test_url_not_admin(self):
        res = self.get_url()
        self.assertEqual(res.status_code, 401)