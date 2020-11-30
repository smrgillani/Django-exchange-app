from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Email must be set!')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)

class Users(AbstractBaseUser):
    password = models.CharField(max_length=128)
    last_login = models.CharField(max_length=200)
    is_superuser = models.SmallIntegerField()
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.SmallIntegerField()
    is_active = models.SmallIntegerField()
    date_joined = models.CharField(max_length=200)

    objects = UserAccountManager()

    USERNAME_FIELD = 'username'

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username