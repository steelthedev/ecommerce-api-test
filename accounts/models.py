
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(
            Q(**{self.model.USERNAME_FIELD: username}) |
            Q(**{self.model.EMAIL_FIELD: username})
        )


class Profile(AbstractUser):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD ="email"

    REQUIRED_FIELDS = []

    objects = CustomUserManager()   

    def __str__(self) -> str:
        return self.username

   
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance= None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)