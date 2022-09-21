
from django.test import TestCase
from .models import Profile
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .serializers import ProfileSerializer



class TestProfileModel(TestCase):

    def create_profile(self):
        return Profile.objects.create(username="testuser",email="user@test.com",last_name="user",first_name="user-first",country="Nigeria",phone="223345")

    def test_model_str(self):
        user = self.create_profile()
        self.assertTrue(isinstance(user,Profile))
        self.assertEqual(user.__str__(), user.username)


class Test_Profile_List_Views(APITestCase):

    def admin_user(self):
        return Profile.objects.create(username="testuser",
        email="user@test.com",
        last_name="user",
        first_name="user-first",
        country="Nigeria",
        phone="223345",
        is_staff=True,
        password="test1234@"
        )
    
    def non_admin_user(self):
        return Profile.objects.create(username="testuser1",
        email="user@test.com",
        last_name="user",
        first_name="user-first",
        country="Nigeria",
        phone="223345",
        is_staff=False,
        password="test1234@"
        )
        
        
    def setUp(self):
        self.profile = self.admin_user()
        self.token = Token.objects.get(user=self.profile)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def tearDown(self) -> None:
        return super().tearDown()

    def get_url(self):
        return self.client.get(reverse("accounts:users_list"))

    def getProfile(self):
        return Profile.objects.all()

    def test_url_user_not_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        res = self.get_url()
        self.assertEqual(res.status_code, 401)

    def test_url_user_not_admin(self):
        self.profile = self.non_admin_user()
        self.token = Token.objects.get(user=self.profile)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        res = self.get_url()
        self.assertEqual(res.status_code, 403)

    def test_url_is_admin(self):
        res = self.get_url()
        self.assertEqual(res.status_code, 200)


    def test_get_res(self):
        res = self.get_url()
        serializer = ProfileSerializer(self.getProfile(), many=True)
        self.assertEqual(res.data,serializer.data)


class Test_GetProfile_View(APITestCase):
    def setUp(self):
        self.profile = Profile.objects.create(username="testuser1",
        email="user@test.com",
        last_name="user",
        first_name="user-first",
        country="Nigeria",
        phone="223345",
        password="test1234@"
        )
        self.token = Token.objects.get(user=self.profile)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
    def tearDown(self) -> None:
        return super().tearDown()


    def get_url(self):
        return self.client.get(reverse("accounts:get_user"))


    def test_url(self):
        res = self.get_url()
        self.assertEqual(res.status_code,200)

    def test_url_user_not_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        res = self.get_url()
        self.assertEqual(res.status_code, 401)

    def test_get_method(self):
        res = self.get_url()
        serializer = ProfileSerializer(self.profile,many=False)
        self.assertEqual(res.data, serializer.data)


    def test_get_method_non_users(self):
        self.client.force_authenticate(user=None, token=None)
        res = self.get_url()
        serializer = ProfileSerializer(self.profile,many=False)
        self.assertNotEqual(res.data, serializer.data)

